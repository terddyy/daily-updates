# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2401**
- Today's entries: **4**
- Today's note: `notes/2026-08-09.md`

### Latest Entry

- Timestamp: `2026-08-09T07:11:07+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 121
- `Testing`: 121
- `APIs`: 120
- `Accessibility`: 120
- `Architecture`: 120

### Recent Timeline

- `2026-08-09T07:11:07+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-09T06:57:44+08:00` | **Write one behavior per test** (Testing)
- `2026-08-09T06:24:53+08:00` | **Use virtual environments by default** (Python)
- `2026-08-09T06:07:55+08:00` | **Prefer small focused commits** (Git)
- `2026-08-08T22:30:18+08:00` | **Write decisions down** (Leadership)
- `2026-08-08T21:46:44+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-08T21:20:29+08:00` | **Measure before tuning** (Performance)
- `2026-08-08T20:49:43+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-08T20:27:05+08:00` | **Retry only safe operations** (Networking)
- `2026-08-08T19:40:25+08:00` | **Batch similar tasks** (Productivity)
