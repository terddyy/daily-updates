# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2081**
- Today's entries: **7**
- Today's note: `notes/2026-07-13.md`

### Latest Entry

- Timestamp: `2026-07-13T10:18:31+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 105
- `Testing`: 105
- `APIs`: 104
- `Accessibility`: 104
- `Architecture`: 104

### Recent Timeline

- `2026-07-13T10:18:31+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-13T09:15:18+08:00` | **Write one behavior per test** (Testing)
- `2026-07-13T08:40:04+08:00` | **Use virtual environments by default** (Python)
- `2026-07-13T07:48:00+08:00` | **Prefer small focused commits** (Git)
- `2026-07-13T07:19:54+08:00` | **Write decisions down** (Leadership)
- `2026-07-13T06:47:15+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-13T06:19:04+08:00` | **Measure before tuning** (Performance)
- `2026-07-12T21:50:32+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-12T20:33:51+08:00` | **Retry only safe operations** (Networking)
- `2026-07-12T18:34:02+08:00` | **Batch similar tasks** (Productivity)
