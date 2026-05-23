# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1381**
- Today's entries: **13**
- Today's note: `notes/2026-05-23.md`

### Latest Entry

- Timestamp: `2026-05-23T19:33:13+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 70
- `Testing`: 70
- `APIs`: 69
- `Accessibility`: 69
- `Architecture`: 69

### Recent Timeline

- `2026-05-23T19:33:13+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-23T18:58:44+08:00` | **Write one behavior per test** (Testing)
- `2026-05-23T18:17:26+08:00` | **Use virtual environments by default** (Python)
- `2026-05-23T15:12:12+08:00` | **Prefer small focused commits** (Git)
- `2026-05-23T14:04:58+08:00` | **Write decisions down** (Leadership)
- `2026-05-23T12:46:23+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-23T11:24:47+08:00` | **Measure before tuning** (Performance)
- `2026-05-23T10:03:07+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-23T09:14:20+08:00` | **Retry only safe operations** (Networking)
- `2026-05-23T08:09:37+08:00` | **Batch similar tasks** (Productivity)
