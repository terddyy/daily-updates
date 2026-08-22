# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2762**
- Today's entries: **5**
- Today's note: `notes/2026-08-22.md`

### Latest Entry

- Timestamp: `2026-08-22T11:25:17+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 139
- `Security`: 139
- `Testing`: 139
- `APIs`: 138
- `Accessibility`: 138

### Recent Timeline

- `2026-08-22T11:25:17+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-22T10:40:16+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-22T09:42:56+08:00` | **Write one behavior per test** (Testing)
- `2026-08-22T07:32:22+08:00` | **Use virtual environments by default** (Python)
- `2026-08-22T06:33:01+08:00` | **Prefer small focused commits** (Git)
- `2026-08-21T22:42:36+08:00` | **Write decisions down** (Leadership)
- `2026-08-21T21:58:03+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-21T21:10:21+08:00` | **Measure before tuning** (Performance)
- `2026-08-21T20:02:05+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-21T19:33:28+08:00` | **Retry only safe operations** (Networking)
