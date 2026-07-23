# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2221**
- Today's entries: **3**
- Today's note: `notes/2026-07-23.md`

### Latest Entry

- Timestamp: `2026-07-23T09:13:23+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 112
- `Testing`: 112
- `APIs`: 111
- `Accessibility`: 111
- `Architecture`: 111

### Recent Timeline

- `2026-07-23T09:13:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-23T07:41:25+08:00` | **Write one behavior per test** (Testing)
- `2026-07-23T06:33:07+08:00` | **Use virtual environments by default** (Python)
- `2026-07-22T22:00:13+08:00` | **Prefer small focused commits** (Git)
- `2026-07-22T19:55:52+08:00` | **Write decisions down** (Leadership)
- `2026-07-22T17:58:52+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-22T15:21:51+08:00` | **Measure before tuning** (Performance)
- `2026-07-22T12:34:00+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-22T09:08:19+08:00` | **Retry only safe operations** (Networking)
- `2026-07-22T07:41:20+08:00` | **Batch similar tasks** (Productivity)
