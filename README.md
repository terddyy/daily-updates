# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2601**
- Today's entries: **30**
- Today's note: `notes/2026-08-15.md`

### Latest Entry

- Timestamp: `2026-08-15T19:50:53+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 131
- `Testing`: 131
- `APIs`: 130
- `Accessibility`: 130
- `Architecture`: 130

### Recent Timeline

- `2026-08-15T19:50:53+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-15T19:37:12+08:00` | **Write one behavior per test** (Testing)
- `2026-08-15T18:51:49+08:00` | **Use virtual environments by default** (Python)
- `2026-08-15T18:39:25+08:00` | **Prefer small focused commits** (Git)
- `2026-08-15T18:06:22+08:00` | **Write decisions down** (Leadership)
- `2026-08-15T17:51:55+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-15T17:24:36+08:00` | **Measure before tuning** (Performance)
- `2026-08-15T16:56:18+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-15T16:24:41+08:00` | **Retry only safe operations** (Networking)
- `2026-08-15T15:55:55+08:00` | **Batch similar tasks** (Productivity)
