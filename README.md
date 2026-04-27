# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **242**
- Today's entries: **15**
- Today's note: `notes/2026-04-27.md`

### Latest Entry

- Timestamp: `2026-04-27T16:49:43+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 13
- `Security`: 13
- `Testing`: 13
- `APIs`: 12
- `Accessibility`: 12

### Recent Timeline

- `2026-04-27T16:49:43+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-27T15:46:54+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-27T14:50:55+08:00` | **Write one behavior per test** (Testing)
- `2026-04-27T13:04:24+08:00` | **Use virtual environments by default** (Python)
- `2026-04-27T11:04:03+08:00` | **Prefer small focused commits** (Git)
- `2026-04-27T09:34:17+08:00` | **Write decisions down** (Leadership)
- `2026-04-27T08:24:14+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-27T07:12:56+08:00` | **Measure before tuning** (Performance)
- `2026-04-27T06:10:06+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-27T05:11:20+08:00` | **Retry only safe operations** (Networking)
