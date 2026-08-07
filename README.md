# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2361**
- Today's entries: **15**
- Today's note: `notes/2026-08-07.md`

### Latest Entry

- Timestamp: `2026-08-07T17:49:07+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 119
- `Testing`: 119
- `APIs`: 118
- `Accessibility`: 118
- `Architecture`: 118

### Recent Timeline

- `2026-08-07T17:49:07+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-07T17:23:40+08:00` | **Write one behavior per test** (Testing)
- `2026-08-07T16:48:34+08:00` | **Use virtual environments by default** (Python)
- `2026-08-07T16:16:12+08:00` | **Prefer small focused commits** (Git)
- `2026-08-07T15:44:55+08:00` | **Write decisions down** (Leadership)
- `2026-08-07T15:10:18+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-07T14:32:16+08:00` | **Measure before tuning** (Performance)
- `2026-08-07T13:58:23+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-07T13:19:56+08:00` | **Retry only safe operations** (Networking)
- `2026-08-07T12:33:07+08:00` | **Batch similar tasks** (Productivity)
