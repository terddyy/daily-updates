# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2482**
- Today's entries: **28**
- Today's note: `notes/2026-08-11.md`

### Latest Entry

- Timestamp: `2026-08-11T19:59:49+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 125
- `Security`: 125
- `Testing`: 125
- `APIs`: 124
- `Accessibility`: 124

### Recent Timeline

- `2026-08-11T19:59:49+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-11T19:31:15+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-11T19:03:36+08:00` | **Write one behavior per test** (Testing)
- `2026-08-11T18:32:51+08:00` | **Use virtual environments by default** (Python)
- `2026-08-11T18:06:58+08:00` | **Prefer small focused commits** (Git)
- `2026-08-11T17:35:42+08:00` | **Write decisions down** (Leadership)
- `2026-08-11T17:08:02+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-11T16:35:39+08:00` | **Measure before tuning** (Performance)
- `2026-08-11T16:11:53+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-11T15:42:29+08:00` | **Retry only safe operations** (Networking)
