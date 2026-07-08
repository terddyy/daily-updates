# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2002**
- Today's entries: **15**
- Today's note: `notes/2026-07-08.md`

### Latest Entry

- Timestamp: `2026-07-08T18:30:41+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 101
- `Security`: 101
- `Testing`: 101
- `APIs`: 100
- `Accessibility`: 100

### Recent Timeline

- `2026-07-08T18:30:41+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-08T17:33:53+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-08T16:38:31+08:00` | **Write one behavior per test** (Testing)
- `2026-07-08T15:37:25+08:00` | **Use virtual environments by default** (Python)
- `2026-07-08T14:36:28+08:00` | **Prefer small focused commits** (Git)
- `2026-07-08T13:41:28+08:00` | **Write decisions down** (Leadership)
- `2026-07-08T12:36:16+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-08T11:23:35+08:00` | **Measure before tuning** (Performance)
- `2026-07-08T10:01:37+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-08T09:13:47+08:00` | **Retry only safe operations** (Networking)
