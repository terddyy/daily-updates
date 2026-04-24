# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **182**
- Today's entries: **21**
- Today's note: `notes/2026-04-24.md`

### Latest Entry

- Timestamp: `2026-04-24T23:26:23+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 10
- `Security`: 10
- `Testing`: 10
- `APIs`: 9
- `Accessibility`: 9

### Recent Timeline

- `2026-04-24T23:26:23+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-24T22:32:50+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-24T21:31:45+08:00` | **Write one behavior per test** (Testing)
- `2026-04-24T20:19:25+08:00` | **Use virtual environments by default** (Python)
- `2026-04-24T19:24:48+08:00` | **Prefer small focused commits** (Git)
- `2026-04-24T18:31:00+08:00` | **Write decisions down** (Leadership)
- `2026-04-24T17:33:06+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-24T16:40:10+08:00` | **Measure before tuning** (Performance)
- `2026-04-24T15:35:45+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-24T14:37:44+08:00` | **Retry only safe operations** (Networking)
