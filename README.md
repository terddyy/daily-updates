# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2381**
- Today's entries: **10**
- Today's note: `notes/2026-08-08.md`

### Latest Entry

- Timestamp: `2026-08-08T12:15:32+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 120
- `Testing`: 120
- `APIs`: 119
- `Accessibility`: 119
- `Architecture`: 119

### Recent Timeline

- `2026-08-08T12:15:32+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-08T11:45:07+08:00` | **Write one behavior per test** (Testing)
- `2026-08-08T11:05:11+08:00` | **Use virtual environments by default** (Python)
- `2026-08-08T10:26:13+08:00` | **Prefer small focused commits** (Git)
- `2026-08-08T09:33:19+08:00` | **Write decisions down** (Leadership)
- `2026-08-08T08:49:03+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-08T07:46:52+08:00` | **Measure before tuning** (Performance)
- `2026-08-08T07:13:02+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-08T06:50:12+08:00` | **Retry only safe operations** (Networking)
- `2026-08-08T06:13:10+08:00` | **Batch similar tasks** (Productivity)
