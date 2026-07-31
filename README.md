# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2281**
- Today's entries: **7**
- Today's note: `notes/2026-07-31.md`

### Latest Entry

- Timestamp: `2026-07-31T22:06:12+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 115
- `Testing`: 115
- `APIs`: 114
- `Accessibility`: 114
- `Architecture`: 114

### Recent Timeline

- `2026-07-31T22:06:12+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-31T19:48:20+08:00` | **Write one behavior per test** (Testing)
- `2026-07-31T17:33:30+08:00` | **Use virtual environments by default** (Python)
- `2026-07-31T14:43:21+08:00` | **Prefer small focused commits** (Git)
- `2026-07-31T11:49:35+08:00` | **Write decisions down** (Leadership)
- `2026-07-31T08:01:21+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-31T06:46:25+08:00` | **Measure before tuning** (Performance)
- `2026-07-30T21:15:05+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-30T19:33:56+08:00` | **Retry only safe operations** (Networking)
- `2026-07-30T17:43:15+08:00` | **Batch similar tasks** (Productivity)
