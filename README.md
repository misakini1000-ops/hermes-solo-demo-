# hermes-solo-ops · free demo pack

> 1인 메이커를 위한 **자가검증 운영 시스템** 미니 데모.
> 외부 화폐(결제·다운로드)만 통과 기준으로 두는 운영 패턴을 한 조각만 떼서 공개한다.

이건 풀세트가 아니다. "이런 식으로 돌아간다"를 5분 안에 확인해 보고, 필요하면 풀세트 출시 알림을 받는 입구다.

> 풀세트(Template Pack) 출시 예정 2026-07. 가격은 출시 직전 공개. [알림 받기](#알림-받기) 폼은 아래.

---

## 무엇이 들어있나

```
demo-pack/
├── README.md             ← 지금 읽는 파일
├── INVENTORY.md          ← 빈 자산 인벤토리 템플릿
├── examples/
│   └── inventory_full.md ← 채워진 예시 (참고용)
└── scripts/
    └── daily_check.py    ← 매일 1번 돌아가는 자가검증 cron 1개 (축약본)
```

총 4파일. 의존성: Python 3.10+ 표준 라이브러리만.

---

## 5분 설치

```bash
git clone https://github.com/misakini1000-ops/hermes-solo-demo-
cd hermes-solo-ops-demo

# 1) 인벤토리 만들기 (자산 무엇을 가졌는지 명시)
cp INVENTORY.md ~/my-inventory.md
# 편집기로 열어 자기 자산 채우기

# 2) 자가검증 1회 실행
python scripts/daily_check.py ~/my-inventory.md

# 3) (선택) cron / launchd 로 매일 09:00 자동 실행
# macOS launchd 예시는 scripts/daily_check.py 상단 주석 참고
```

---

## 이 데모가 보여주는 한 가지 원칙

> **"존재 ≠ 동작"**.
> 자산을 가지고 있다고 자동으로 가치가 되는 건 아니다.
> 매일 점검해서 "오늘도 살아있나"를 외부 신호로 검증해야 부패하지 않는다.

`daily_check.py` 는 인벤토리 항목마다 *마지막 검증 시각* 을 보고, 7일 이상 안 만진 것에 `🔴 STALE` 표시를 붙인다. 그게 전부다. 작지만 이게 풀세트의 척추다.

---

## 풀세트에는 뭐가 더 있나 (Template Pack · 출시 예정)

- 게이트 시스템 (PAY → COMPETE → DELIVER, 외부 화폐만 통과)
- 운영 패턴 모음 — 실제로 매일 돌고 있는 cron 알림 침묵, INVENTORY 강제 점검, pre-build-gate 등
- 실패 케이스 회고 — 망친 시도들과 왜 망했는지 (출시 시점까지 정리된 항목 수 공개)
- Hermes Agent 설치 가이드 (5분, MIT 오픈소스)
- 환불 정책: 7일 100% (설치 실패 포함)

가격·출시일·구체 항목 수는 출시 직전 확정.

### 알림 받기

GitHub 이슈 #1 에 코멘트만 남기면 출시 시 멘션. 이메일·뉴스레터 X.

---

## 누가 만들었나

이 진 (Lee Jin). 1인 메이커, 자동화 우선주의자.
콘텐츠: [@misakini1000](https://www.youtube.com/@misakini1000) (YT)
한국어 글: [Disquiet 프로필](https://disquiet.io)

---

## 라이선스

MIT. 마음대로 베껴 써도 됨. 출처 표시도 강제 안 함.
