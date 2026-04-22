# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **123**
- Today's entries: **10**
- Today's note: `notes/2026-04-22.md`

### Latest Entry

- Timestamp: `2026-04-22T09:33:36+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 7
- `Databases`: 7
- `Security`: 7
- `Testing`: 7
- `Accessibility`: 6

### Recent Timeline

- `2026-04-22T09:33:36+08:00` | **Design for idempotency** (APIs)
- `2026-04-22T08:20:57+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-22T07:13:36+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-22T06:14:26+08:00` | **Write one behavior per test** (Testing)
- `2026-04-22T05:15:33+08:00` | **Use virtual environments by default** (Python)
- `2026-04-22T04:17:38+08:00` | **Prefer small focused commits** (Git)
- `2026-04-22T03:27:45+08:00` | **Write decisions down** (Leadership)
- `2026-04-22T02:21:32+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-22T01:22:19+08:00` | **Measure before tuning** (Performance)
- `2026-04-22T00:24:00+08:00` | **Fail fast on lint and tests** (CI/CD)
