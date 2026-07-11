# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2061**
- Today's entries: **2**
- Today's note: `notes/2026-07-12.md`

### Latest Entry

- Timestamp: `2026-07-12T06:31:34+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 104
- `Testing`: 104
- `APIs`: 103
- `Accessibility`: 103
- `Architecture`: 103

### Recent Timeline

- `2026-07-12T06:31:34+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-12T06:04:31+08:00` | **Write one behavior per test** (Testing)
- `2026-07-11T22:38:47+08:00` | **Use virtual environments by default** (Python)
- `2026-07-11T21:32:42+08:00` | **Prefer small focused commits** (Git)
- `2026-07-11T20:49:20+08:00` | **Write decisions down** (Leadership)
- `2026-07-11T20:22:12+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-11T19:48:43+08:00` | **Measure before tuning** (Performance)
- `2026-07-11T18:53:45+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-11T18:28:18+08:00` | **Retry only safe operations** (Networking)
- `2026-07-11T17:03:59+08:00` | **Batch similar tasks** (Productivity)
