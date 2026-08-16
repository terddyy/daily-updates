# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2622**
- Today's entries: **13**
- Today's note: `notes/2026-08-16.md`

### Latest Entry

- Timestamp: `2026-08-16T15:54:09+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 132
- `Security`: 132
- `Testing`: 132
- `APIs`: 131
- `Accessibility`: 131

### Recent Timeline

- `2026-08-16T15:54:09+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-16T14:47:13+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-16T14:09:49+08:00` | **Write one behavior per test** (Testing)
- `2026-08-16T13:54:18+08:00` | **Use virtual environments by default** (Python)
- `2026-08-16T12:44:52+08:00` | **Prefer small focused commits** (Git)
- `2026-08-16T12:26:01+08:00` | **Write decisions down** (Leadership)
- `2026-08-16T12:00:40+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-16T11:08:56+08:00` | **Measure before tuning** (Performance)
- `2026-08-16T08:48:30+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-16T07:37:06+08:00` | **Retry only safe operations** (Networking)
