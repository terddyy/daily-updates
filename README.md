# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1862**
- Today's entries: **10**
- Today's note: `notes/2026-06-29.md`

### Latest Entry

- Timestamp: `2026-06-29T16:41:22+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 94
- `Security`: 94
- `Testing`: 94
- `APIs`: 93
- `Accessibility`: 93

### Recent Timeline

- `2026-06-29T16:41:22+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-29T14:53:54+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-29T13:05:57+08:00` | **Write one behavior per test** (Testing)
- `2026-06-29T11:15:25+08:00` | **Use virtual environments by default** (Python)
- `2026-06-29T09:51:54+08:00` | **Prefer small focused commits** (Git)
- `2026-06-29T08:57:51+08:00` | **Write decisions down** (Leadership)
- `2026-06-29T07:54:12+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-29T07:27:06+08:00` | **Measure before tuning** (Performance)
- `2026-06-29T06:49:53+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-29T06:25:19+08:00` | **Retry only safe operations** (Networking)
