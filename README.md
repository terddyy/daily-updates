# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1681**
- Today's entries: **2**
- Today's note: `notes/2026-06-16.md`

### Latest Entry

- Timestamp: `2026-06-16T06:56:32+08:00`
- Title: **Rotate credentials on schedule**
- Category: `Security`
- Source: https://owasp.org/www-project-top-ten/
- Summary: Regular credential rotation limits blast radius if a secret leaks and encourages teams to maintain key management hygiene.

### Top Categories

- `Security`: 85
- `Testing`: 85
- `APIs`: 84
- `Accessibility`: 84
- `Architecture`: 84

### Recent Timeline

- `2026-06-16T06:56:32+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-16T06:04:16+08:00` | **Write one behavior per test** (Testing)
- `2026-06-15T20:52:05+08:00` | **Use virtual environments by default** (Python)
- `2026-06-15T18:40:50+08:00` | **Prefer small focused commits** (Git)
- `2026-06-15T16:28:47+08:00` | **Write decisions down** (Leadership)
- `2026-06-15T14:07:59+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-15T12:13:02+08:00` | **Measure before tuning** (Performance)
- `2026-06-15T10:42:04+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-15T09:31:44+08:00` | **Retry only safe operations** (Networking)
- `2026-06-15T08:12:30+08:00` | **Batch similar tasks** (Productivity)
