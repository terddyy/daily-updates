# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1781**
- Today's entries: **15**
- Today's note: `notes/2026-06-23.md`

### Latest Entry

- Timestamp: `2026-06-23T22:19:47+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 90
- `Testing`: 90
- `APIs`: 89
- `Accessibility`: 89
- `Architecture`: 89

### Recent Timeline

- `2026-06-23T22:19:47+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-23T21:16:29+08:00` | **Write one behavior per test** (Testing)
- `2026-06-23T20:02:56+08:00` | **Use virtual environments by default** (Python)
- `2026-06-23T18:48:49+08:00` | **Prefer small focused commits** (Git)
- `2026-06-23T17:31:54+08:00` | **Write decisions down** (Leadership)
- `2026-06-23T16:14:18+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-23T14:48:49+08:00` | **Measure before tuning** (Performance)
- `2026-06-23T13:25:37+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-23T11:46:56+08:00` | **Retry only safe operations** (Networking)
- `2026-06-23T10:21:23+08:00` | **Batch similar tasks** (Productivity)
