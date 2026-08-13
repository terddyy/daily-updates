# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2521**
- Today's entries: **6**
- Today's note: `notes/2026-08-13.md`

### Latest Entry

- Timestamp: `2026-08-13T08:52:09+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 127
- `Testing`: 127
- `APIs`: 126
- `Accessibility`: 126
- `Architecture`: 126

### Recent Timeline

- `2026-08-13T08:52:09+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-13T08:27:01+08:00` | **Write one behavior per test** (Testing)
- `2026-08-13T07:46:27+08:00` | **Use virtual environments by default** (Python)
- `2026-08-13T07:16:25+08:00` | **Prefer small focused commits** (Git)
- `2026-08-13T06:46:22+08:00` | **Write decisions down** (Leadership)
- `2026-08-13T06:16:28+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-12T22:52:21+08:00` | **Measure before tuning** (Performance)
- `2026-08-12T22:28:01+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-12T21:47:04+08:00` | **Retry only safe operations** (Networking)
- `2026-08-12T21:09:33+08:00` | **Batch similar tasks** (Productivity)
