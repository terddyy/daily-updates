# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1385**
- Today's entries: **17**
- Today's note: `notes/2026-05-23.md`

### Latest Entry

- Timestamp: `2026-05-23T22:35:38+08:00`
- Title: **Keep boundaries explicit**
- Category: `Architecture`
- Source: https://12factor.net/
- Summary: Defining module boundaries early reduces accidental coupling and keeps refactors local instead of system-wide.

### Top Categories

- `APIs`: 70
- `Architecture`: 70
- `Databases`: 70
- `Observability`: 70
- `Security`: 70

### Recent Timeline

- `2026-05-23T22:35:38+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-23T21:55:18+08:00` | **Log with stable keys** (Observability)
- `2026-05-23T21:11:15+08:00` | **Design for idempotency** (APIs)
- `2026-05-23T20:38:18+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-23T19:33:13+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-23T18:58:44+08:00` | **Write one behavior per test** (Testing)
- `2026-05-23T18:17:26+08:00` | **Use virtual environments by default** (Python)
- `2026-05-23T15:12:12+08:00` | **Prefer small focused commits** (Git)
- `2026-05-23T14:04:58+08:00` | **Write decisions down** (Leadership)
- `2026-05-23T12:46:23+08:00` | **Keyboard support is a baseline** (Accessibility)
