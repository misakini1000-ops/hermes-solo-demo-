#!/usr/bin/env python3
"""
daily_check.py — hermes-solo-ops 자가검증 데모 (축약본)

매일 한 번 실행해서 INVENTORY.md 의 자산들이 최근 7일 안에
검증되었는지 확인하고, 오래된(STALE) 항목을 콘솔에 표시한다.

이게 풀세트의 척추다. 풀세트는 cron 자동 등록 + 텔레그램/이메일 알림 +
외부 화폐 게이트(Gumroad 매출 폴링)까지 포함한다.

## 사용법

    python daily_check.py path/to/INVENTORY.md

## macOS launchd 자동 실행 (선택)

    # ~/Library/LaunchAgents/com.example.solo-ops-daily.plist 생성 후
    # 매일 09:00 트리거하도록 등록하면 끝.
    # 풀세트(Template Pack)에 plist 템플릿 포함.

라이선스: MIT
"""

from __future__ import annotations
import re
import sys
from datetime import date, datetime
from pathlib import Path

STALE_DAYS = 7

# 매우 단순한 YAML-블록 추출 — 외부 의존성 없이 동작하기 위해
# 정규식으로 `- id: ... last_verified: YYYY-MM-DD ... purpose: ...` 패턴만 본다.
BLOCK_RE = re.compile(
    r"-\s+id:\s*(?P<id>\S+).*?"
    r"type:\s*(?P<type>\S+).*?"
    r"last_verified:\s*(?P<lv>\d{4}-\d{2}-\d{2}).*?"
    r"purpose:\s*(?P<purpose>[^\n]+)",
    re.DOTALL,
)


def parse_inventory(text: str) -> list[dict]:
    """INVENTORY.md 텍스트에서 자산 블록을 추출한다."""
    items = []
    for m in BLOCK_RE.finditer(text):
        items.append({
            "id": m.group("id"),
            "type": m.group("type"),
            "last_verified": m.group("lv"),
            "purpose": m.group("purpose").strip(),
        })
    return items


def check_freshness(item: dict, today: date) -> tuple[str, int]:
    """상태 이모지와 경과일 반환."""
    lv = datetime.strptime(item["last_verified"], "%Y-%m-%d").date()
    age = (today - lv).days
    if age > STALE_DAYS:
        return "🔴 STALE", age
    if age > STALE_DAYS // 2:
        return "🟡 AGING", age
    return "🟢 FRESH", age


def render_report(items: list[dict]) -> str:
    if not items:
        return (
            "⚠️  자산이 0개다. INVENTORY.md 에 항목을 채워야 검증할 게 생긴다.\n"
            "    examples/inventory_full.md 를 참고."
        )
    today = date.today()
    lines = [f"# 자가검증 리포트 — {today.isoformat()}\n"]
    counts = {"🟢 FRESH": 0, "🟡 AGING": 0, "🔴 STALE": 0}
    for item in items:
        status, age = check_freshness(item, today)
        counts[status] += 1
        lines.append(f"{status}  [{age:3d}d]  {item['id']:30s}  {item['purpose']}")
    lines.append("")
    lines.append("---")
    lines.append(
        f"FRESH {counts['🟢 FRESH']}  /  AGING {counts['🟡 AGING']}  /  STALE {counts['🔴 STALE']}"
    )
    if counts["🔴 STALE"]:
        lines.append("")
        lines.append("🔴 STALE 항목은 즉시 점검하거나 삭제하라. 존재 ≠ 동작.")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python daily_check.py path/to/INVENTORY.md", file=sys.stderr)
        return 2
    p = Path(argv[1]).expanduser()
    if not p.exists():
        print(f"❌ 파일 없음: {p}", file=sys.stderr)
        return 1
    items = parse_inventory(p.read_text(encoding="utf-8"))
    print(render_report(items))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
