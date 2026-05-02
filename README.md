# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **863**
- Today's entries: **91**
- Today's note: `notes/2026-05-02.md`

### Latest Entry

- Timestamp: `2026-05-02T08:39:36+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 44
- `Databases`: 44
- `Security`: 44
- `Testing`: 44
- `Accessibility`: 43

### Recent Timeline

- `2026-05-02T08:39:36+08:00` | **Design for idempotency** (APIs)
- `2026-05-02T08:39:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-02T08:39:34+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-02T08:39:33+08:00` | **Write one behavior per test** (Testing)
- `2026-05-02T08:39:32+08:00` | **Use virtual environments by default** (Python)
- `2026-05-02T08:39:31+08:00` | **Prefer small focused commits** (Git)
- `2026-05-02T08:39:30+08:00` | **Write decisions down** (Leadership)
- `2026-05-02T08:39:29+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-02T08:39:28+08:00` | **Measure before tuning** (Performance)
- `2026-05-02T08:39:27+08:00` | **Fail fast on lint and tests** (CI/CD)
