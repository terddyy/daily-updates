# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2462**
- Today's entries: **8**
- Today's note: `notes/2026-08-11.md`

### Latest Entry

- Timestamp: `2026-08-11T09:10:49+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 124
- `Security`: 124
- `Testing`: 124
- `APIs`: 123
- `Accessibility`: 123

### Recent Timeline

- `2026-08-11T09:10:49+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-11T08:32:33+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-11T08:00:39+08:00` | **Write one behavior per test** (Testing)
- `2026-08-11T07:44:38+08:00` | **Use virtual environments by default** (Python)
- `2026-08-11T07:16:41+08:00` | **Prefer small focused commits** (Git)
- `2026-08-11T06:59:11+08:00` | **Write decisions down** (Leadership)
- `2026-08-11T06:31:25+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-11T06:14:12+08:00` | **Measure before tuning** (Performance)
- `2026-08-10T22:39:10+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-10T22:11:58+08:00` | **Retry only safe operations** (Networking)
