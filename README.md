# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **202**
- Today's entries: **20**
- Today's note: `notes/2026-04-25.md`

### Latest Entry

- Timestamp: `2026-04-25T20:11:53+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 11
- `Security`: 11
- `Testing`: 11
- `APIs`: 10
- `Accessibility`: 10

### Recent Timeline

- `2026-04-25T20:11:53+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-25T19:15:16+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-25T18:14:33+08:00` | **Write one behavior per test** (Testing)
- `2026-04-25T17:18:22+08:00` | **Use virtual environments by default** (Python)
- `2026-04-25T16:18:48+08:00` | **Prefer small focused commits** (Git)
- `2026-04-25T15:29:45+08:00` | **Write decisions down** (Leadership)
- `2026-04-25T14:29:27+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-25T13:34:57+08:00` | **Measure before tuning** (Performance)
- `2026-04-25T12:48:44+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-25T11:02:02+08:00` | **Retry only safe operations** (Networking)
