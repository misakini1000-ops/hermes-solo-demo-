# INVENTORY · 채워진 예시

> 이건 참고용 샘플이다. 실제 자산을 어떻게 기재하는지 감 잡으라고 둠.

```yaml
- id: yt-main-channel
  type: content
  path_or_url: https://youtube.com/@example
  last_verified: 2026-05-20
  purpose: 메인 YT 채널 — 주 3회 자동 업로드

- id: ig-reels-pipeline
  type: cron
  path_or_url: launchd/com.example.ig-reels-daily
  last_verified: 2026-05-21
  purpose: IG Reels 매일 1편 자동 발행

- id: newsletter-archive
  type: data
  path_or_url: ~/newsletter/archive/
  last_verified: 2026-05-18
  purpose: 발송한 뉴스레터 백업 (Markdown)

- id: gumroad-product-monthly-report
  type: account
  path_or_url: https://example.com/your-product  # 예시: 본인 결제/판매 페이지 URL
  last_verified: 2026-05-14
  purpose: 월간 운영 리포트 $9 구독 상품

- id: t9-backup-script
  type: script
  path_or_url: ~/scripts/backup_t9.sh
  last_verified: 2026-05-08
  purpose: 주간 외장 백업 — 🔴 13일 됨, 곧 STALE 경고 뜸
```
