# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2921**
- Today's entries: **5**
- Today's note: `notes/2026-09-07.md`

### Latest Entry

- Timestamp: `2026-09-07T07:09:21+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 147
- `Testing`: 147
- `APIs`: 146
- `Accessibility`: 146
- `Architecture`: 146

### Recent Timeline

- `2026-09-07T07:09:21+08:00` | **Rotate credentials on schedule** (Security)
- `2026-09-07T06:48:09+08:00` | **Write one behavior per test** (Testing)
- `2026-09-07T06:34:43+08:00` | **Use virtual environments by default** (Python)
- `2026-09-07T06:22:00+08:00` | **Prefer small focused commits** (Git)
- `2026-09-07T06:10:03+08:00` | **Write decisions down** (Leadership)
- `2026-09-06T22:35:06+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-09-06T22:22:04+08:00` | **Measure before tuning** (Performance)
- `2026-09-06T21:21:17+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-09-06T21:09:54+08:00` | **Retry only safe operations** (Networking)
- `2026-09-06T19:48:12+08:00` | **Batch similar tasks** (Productivity)
