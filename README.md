# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2802**
- Today's entries: **13**
- Today's note: `notes/2026-08-24.md`

### Latest Entry

- Timestamp: `2026-08-24T17:04:18+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 141
- `Security`: 141
- `Testing`: 141
- `APIs`: 140
- `Accessibility`: 140

### Recent Timeline

- `2026-08-24T17:04:18+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-24T16:10:33+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-24T15:20:14+08:00` | **Write one behavior per test** (Testing)
- `2026-08-24T14:03:08+08:00` | **Use virtual environments by default** (Python)
- `2026-08-24T13:24:58+08:00` | **Prefer small focused commits** (Git)
- `2026-08-24T12:43:29+08:00` | **Write decisions down** (Leadership)
- `2026-08-24T11:53:52+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-24T10:45:15+08:00` | **Measure before tuning** (Performance)
- `2026-08-24T09:16:22+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-24T07:45:45+08:00` | **Retry only safe operations** (Networking)
