# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1363**
- Today's entries: **11**
- Today's note: `notes/2026-05-22.md`

### Latest Entry

- Timestamp: `2026-05-22T17:26:19+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 69
- `Databases`: 69
- `Security`: 69
- `Testing`: 69
- `Accessibility`: 68

### Recent Timeline

- `2026-05-22T17:26:19+08:00` | **Design for idempotency** (APIs)
- `2026-05-22T16:10:47+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-22T14:49:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-22T13:26:07+08:00` | **Write one behavior per test** (Testing)
- `2026-05-22T11:47:27+08:00` | **Use virtual environments by default** (Python)
- `2026-05-22T10:22:47+08:00` | **Prefer small focused commits** (Git)
- `2026-05-22T09:18:36+08:00` | **Write decisions down** (Leadership)
- `2026-05-22T08:09:22+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-22T07:36:55+08:00` | **Measure before tuning** (Performance)
- `2026-05-22T07:09:03+08:00` | **Fail fast on lint and tests** (CI/CD)
