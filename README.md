# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2662**
- Today's entries: **19**
- Today's note: `notes/2026-08-17.md`

### Latest Entry

- Timestamp: `2026-08-17T19:59:18+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 134
- `Security`: 134
- `Testing`: 134
- `APIs`: 133
- `Accessibility`: 133

### Recent Timeline

- `2026-08-17T19:59:18+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-17T19:40:24+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-17T19:02:03+08:00` | **Write one behavior per test** (Testing)
- `2026-08-17T18:36:22+08:00` | **Use virtual environments by default** (Python)
- `2026-08-17T17:57:05+08:00` | **Prefer small focused commits** (Git)
- `2026-08-17T17:00:18+08:00` | **Write decisions down** (Leadership)
- `2026-08-17T16:06:36+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-17T15:15:37+08:00` | **Measure before tuning** (Performance)
- `2026-08-17T14:04:33+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-17T13:34:08+08:00` | **Retry only safe operations** (Networking)
