# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2303**
- Today's entries: **4**
- Today's note: `notes/2026-08-04.md`

### Latest Entry

- Timestamp: `2026-08-04T12:30:32+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 116
- `Databases`: 116
- `Security`: 116
- `Testing`: 116
- `Accessibility`: 115

### Recent Timeline

- `2026-08-04T12:30:32+08:00` | **Design for idempotency** (APIs)
- `2026-08-04T09:06:21+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-04T07:35:33+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-04T06:17:30+08:00` | **Write one behavior per test** (Testing)
- `2026-08-03T21:40:44+08:00` | **Use virtual environments by default** (Python)
- `2026-08-03T18:54:29+08:00` | **Prefer small focused commits** (Git)
- `2026-08-03T15:26:28+08:00` | **Write decisions down** (Leadership)
- `2026-08-03T11:54:04+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-03T08:05:10+08:00` | **Measure before tuning** (Performance)
- `2026-08-03T06:58:21+08:00` | **Fail fast on lint and tests** (CI/CD)
