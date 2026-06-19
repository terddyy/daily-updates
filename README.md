# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1721**
- Today's entries: **3**
- Today's note: `notes/2026-06-19.md`

### Latest Entry

- Timestamp: `2026-06-19T08:15:37+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 87
- `Testing`: 87
- `APIs`: 86
- `Accessibility`: 86
- `Architecture`: 86

### Recent Timeline

- `2026-06-19T08:15:37+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-19T07:36:22+08:00` | **Write one behavior per test** (Testing)
- `2026-06-19T06:46:14+08:00` | **Use virtual environments by default** (Python)
- `2026-06-18T22:33:17+08:00` | **Prefer small focused commits** (Git)
- `2026-06-18T21:28:58+08:00` | **Write decisions down** (Leadership)
- `2026-06-18T20:10:32+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-18T18:47:33+08:00` | **Measure before tuning** (Performance)
- `2026-06-18T17:02:47+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-18T15:19:31+08:00` | **Retry only safe operations** (Networking)
- `2026-06-18T13:41:03+08:00` | **Batch similar tasks** (Productivity)
