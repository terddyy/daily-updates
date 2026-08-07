# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2362**
- Today's entries: **16**
- Today's note: `notes/2026-08-07.md`

### Latest Entry

- Timestamp: `2026-08-07T18:20:27+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 119
- `Security`: 119
- `Testing`: 119
- `APIs`: 118
- `Accessibility`: 118

### Recent Timeline

- `2026-08-07T18:20:27+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-07T17:49:07+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-07T17:23:40+08:00` | **Write one behavior per test** (Testing)
- `2026-08-07T16:48:34+08:00` | **Use virtual environments by default** (Python)
- `2026-08-07T16:16:12+08:00` | **Prefer small focused commits** (Git)
- `2026-08-07T15:44:55+08:00` | **Write decisions down** (Leadership)
- `2026-08-07T15:10:18+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-07T14:32:16+08:00` | **Measure before tuning** (Performance)
- `2026-08-07T13:58:23+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-07T13:19:56+08:00` | **Retry only safe operations** (Networking)
