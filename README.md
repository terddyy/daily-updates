# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2342**
- Today's entries: **16**
- Today's note: `notes/2026-08-06.md`

### Latest Entry

- Timestamp: `2026-08-06T19:06:12+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 118
- `Security`: 118
- `Testing`: 118
- `APIs`: 117
- `Accessibility`: 117

### Recent Timeline

- `2026-08-06T19:06:12+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-06T18:12:41+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-06T17:13:33+08:00` | **Write one behavior per test** (Testing)
- `2026-08-06T16:04:52+08:00` | **Use virtual environments by default** (Python)
- `2026-08-06T15:10:55+08:00` | **Prefer small focused commits** (Git)
- `2026-08-06T14:09:47+08:00` | **Write decisions down** (Leadership)
- `2026-08-06T13:05:35+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-06T11:51:52+08:00` | **Measure before tuning** (Performance)
- `2026-08-06T10:39:29+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-06T09:36:07+08:00` | **Retry only safe operations** (Networking)
