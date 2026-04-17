# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **22**
- Today's entries: **18**
- Today's note: `notes/2026-04-17.md`

### Latest Entry

- Timestamp: `2026-04-17T23:22:49+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 2
- `Security`: 2
- `Testing`: 2
- `APIs`: 1
- `Accessibility`: 1

### Recent Timeline

- `2026-04-17T23:22:49+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-17T22:26:53+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-17T21:31:27+08:00` | **Write one behavior per test** (Testing)
- `2026-04-17T20:17:53+08:00` | **Use virtual environments by default** (Python)
- `2026-04-17T19:19:12+08:00` | **Prefer small focused commits** (Git)
- `2026-04-17T18:25:34+08:00` | **Write decisions down** (Leadership)
- `2026-04-17T17:31:23+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-17T16:32:45+08:00` | **Measure before tuning** (Performance)
- `2026-04-17T15:33:15+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-17T14:35:56+08:00` | **Retry only safe operations** (Networking)
