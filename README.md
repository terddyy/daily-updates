# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **601**
- Today's entries: **329**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:08:56+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 31
- `Testing`: 31
- `APIs`: 30
- `Accessibility`: 30
- `Architecture`: 30

### Recent Timeline

- `2026-05-01T09:08:56+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-01T09:08:55+08:00` | **Write one behavior per test** (Testing)
- `2026-05-01T09:08:54+08:00` | **Use virtual environments by default** (Python)
- `2026-05-01T09:08:53+08:00` | **Prefer small focused commits** (Git)
- `2026-05-01T09:08:52+08:00` | **Write decisions down** (Leadership)
- `2026-05-01T09:08:51+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-01T09:08:50+08:00` | **Measure before tuning** (Performance)
- `2026-05-01T09:08:49+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-01T09:08:48+08:00` | **Retry only safe operations** (Networking)
- `2026-05-01T09:08:47+08:00` | **Batch similar tasks** (Productivity)
