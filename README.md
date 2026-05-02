# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1143**
- Today's entries: **371**
- Today's note: `notes/2026-05-02.md`

### Latest Entry

- Timestamp: `2026-05-02T08:44:16+08:00`
- Title: **Design for idempotency**
- Category: `APIs`
- Source: https://www.rfc-editor.org/rfc/rfc7231
- Summary: Idempotent create/update endpoints make retries safe under network failures and reduce accidental duplicate operations.

### Top Categories

- `APIs`: 58
- `Databases`: 58
- `Security`: 58
- `Testing`: 58
- `Accessibility`: 57

### Recent Timeline

- `2026-05-02T08:44:16+08:00` | **Design for idempotency** (APIs)
- `2026-05-02T08:44:15+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-02T08:44:14+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-02T08:44:13+08:00` | **Write one behavior per test** (Testing)
- `2026-05-02T08:44:12+08:00` | **Use virtual environments by default** (Python)
- `2026-05-02T08:44:11+08:00` | **Prefer small focused commits** (Git)
- `2026-05-02T08:44:10+08:00` | **Write decisions down** (Leadership)
- `2026-05-02T08:44:09+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-02T08:44:08+08:00` | **Measure before tuning** (Performance)
- `2026-05-02T08:44:07+08:00` | **Fail fast on lint and tests** (CI/CD)
