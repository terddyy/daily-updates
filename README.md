# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **262**
- Today's entries: **13**
- Today's note: `notes/2026-04-28.md`

### Latest Entry

- Timestamp: `2026-04-28T14:52:42+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 14
- `Security`: 14
- `Testing`: 14
- `APIs`: 13
- `Accessibility`: 13

### Recent Timeline

- `2026-04-28T14:52:42+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-28T13:07:05+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-28T11:04:02+08:00` | **Write one behavior per test** (Testing)
- `2026-04-28T09:34:31+08:00` | **Use virtual environments by default** (Python)
- `2026-04-28T08:27:19+08:00` | **Prefer small focused commits** (Git)
- `2026-04-28T07:18:18+08:00` | **Write decisions down** (Leadership)
- `2026-04-28T06:16:24+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-28T05:22:05+08:00` | **Measure before tuning** (Performance)
- `2026-04-28T04:23:13+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-28T03:31:28+08:00` | **Retry only safe operations** (Networking)
