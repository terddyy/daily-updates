# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2702**
- Today's entries: **13**
- Today's note: `notes/2026-08-19.md`

### Latest Entry

- Timestamp: `2026-08-19T15:43:25+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 136
- `Security`: 136
- `Testing`: 136
- `APIs`: 135
- `Accessibility`: 135

### Recent Timeline

- `2026-08-19T15:43:25+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-19T14:57:17+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-19T13:58:33+08:00` | **Write one behavior per test** (Testing)
- `2026-08-19T13:29:29+08:00` | **Use virtual environments by default** (Python)
- `2026-08-19T12:51:55+08:00` | **Prefer small focused commits** (Git)
- `2026-08-19T12:10:31+08:00` | **Write decisions down** (Leadership)
- `2026-08-19T11:29:23+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-19T10:32:23+08:00` | **Measure before tuning** (Performance)
- `2026-08-19T09:14:03+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-19T07:47:12+08:00` | **Retry only safe operations** (Networking)
