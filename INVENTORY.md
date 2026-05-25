# INVENTORY · 자산 목록 (템플릿)

> 매일 `daily_check.py` 가 이 파일을 읽고 각 항목의 신선도를 점검한다.
> 형식만 지키면 항목 수는 자유.

## 사용법

각 항목은 아래 5필드 한 블록.

- **id**: 영문 소문자/하이픈, 유일
- **type**: `script` | `cron` | `content` | `data` | `account` | `other`
- **path_or_url**: 위치 (로컬 경로 / URL / cron job_id 등)
- **last_verified**: ISO 날짜 `YYYY-MM-DD` — 마지막으로 "동작함" 확인한 날
- **purpose**: 한 줄 설명

`last_verified` 가 오늘 기준 7일 넘으면 `daily_check.py` 가 🔴 STALE 표시.

---

## 예시 (지우고 자기 자산으로 채우기)

```yaml
- id: example-cron-daily-report
  type: cron
  path_or_url: launchd/com.example.daily-report
  last_verified: 2026-05-21
  purpose: 매일 09:00 매출/구독 리포트 텔레그램 발송

- id: example-script-backup
  type: script
  path_or_url: ~/scripts/backup_t9.sh
  last_verified: 2026-05-15
  purpose: T9 외장 드라이브 주간 백업

- id: example-content-yt-channel
  type: content
  path_or_url: https://youtube.com/@yourhandle
  last_verified: 2026-05-20
  purpose: 메인 YT 채널, 주 3회 업로드
```

---

## 내 자산

(여기부터 채우세요)

```yaml
- id: 
  type: 
  path_or_url: 
  last_verified: 
  purpose: 
```
