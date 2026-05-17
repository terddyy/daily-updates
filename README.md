# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1281**
- Today's entries: **3**
- Today's note: `notes/2026-05-17.md`

### Latest Entry

- Timestamp: `2026-05-17T09:17:00+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 65
- `Testing`: 65
- `APIs`: 64
- `Accessibility`: 64
- `Architecture`: 64

### Recent Timeline

- `2026-05-17T09:17:00+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-17T07:04:50+08:00` | **Write one behavior per test** (Testing)
- `2026-05-17T06:30:52+08:00` | **Use virtual environments by default** (Python)
- `2026-05-16T21:11:13+08:00` | **Prefer small focused commits** (Git)
- `2026-05-16T20:39:06+08:00` | **Write decisions down** (Leadership)
- `2026-05-16T20:03:48+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-16T19:36:19+08:00` | **Measure before tuning** (Performance)
- `2026-05-16T18:43:24+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-16T18:11:01+08:00` | **Retry only safe operations** (Networking)
- `2026-05-02T08:46:25+08:00` | **Batch similar tasks** (Productivity)
