# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1742**
- Today's entries: **12**
- Today's note: `notes/2026-06-20.md`

### Latest Entry

- Timestamp: `2026-06-20T21:37:18+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 88
- `Security`: 88
- `Testing`: 88
- `APIs`: 87
- `Accessibility`: 87

### Recent Timeline

- `2026-06-20T21:37:18+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-20T19:27:31+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-20T18:38:09+08:00` | **Write one behavior per test** (Testing)
- `2026-06-20T17:40:12+08:00` | **Use virtual environments by default** (Python)
- `2026-06-20T16:23:44+08:00` | **Prefer small focused commits** (Git)
- `2026-06-20T15:06:09+08:00` | **Write decisions down** (Leadership)
- `2026-06-20T13:33:59+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-20T10:22:02+08:00` | **Measure before tuning** (Performance)
- `2026-06-20T08:09:30+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-20T07:38:30+08:00` | **Retry only safe operations** (Networking)
