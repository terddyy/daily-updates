# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2101**
- Today's entries: **10**
- Today's note: `notes/2026-07-14.md`

### Latest Entry

- Timestamp: `2026-07-14T13:02:45+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 106
- `Testing`: 106
- `APIs`: 105
- `Accessibility`: 105
- `Architecture`: 105

### Recent Timeline

- `2026-07-14T13:02:45+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-14T11:47:34+08:00` | **Write one behavior per test** (Testing)
- `2026-07-14T10:39:05+08:00` | **Use virtual environments by default** (Python)
- `2026-07-14T09:36:00+08:00` | **Prefer small focused commits** (Git)
- `2026-07-14T08:49:15+08:00` | **Write decisions down** (Leadership)
- `2026-07-14T08:04:04+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-14T07:33:20+08:00` | **Measure before tuning** (Performance)
- `2026-07-14T07:06:21+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-14T06:33:48+08:00` | **Retry only safe operations** (Networking)
- `2026-07-14T06:05:07+08:00` | **Batch similar tasks** (Productivity)
