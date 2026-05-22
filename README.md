# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1362**
- Today's entries: **10**
- Today's note: `notes/2026-05-22.md`

### Latest Entry

- Timestamp: `2026-05-22T16:10:47+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 69
- `Security`: 69
- `Testing`: 69
- `APIs`: 68
- `Accessibility`: 68

### Recent Timeline

- `2026-05-22T16:10:47+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-22T14:49:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-22T13:26:07+08:00` | **Write one behavior per test** (Testing)
- `2026-05-22T11:47:27+08:00` | **Use virtual environments by default** (Python)
- `2026-05-22T10:22:47+08:00` | **Prefer small focused commits** (Git)
- `2026-05-22T09:18:36+08:00` | **Write decisions down** (Leadership)
- `2026-05-22T08:09:22+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-22T07:36:55+08:00` | **Measure before tuning** (Performance)
- `2026-05-22T07:09:03+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-22T06:32:18+08:00` | **Retry only safe operations** (Networking)
