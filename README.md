# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1842**
- Today's entries: **2**
- Today's note: `notes/2026-06-28.md`

### Latest Entry

- Timestamp: `2026-06-28T06:50:35+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 93
- `Security`: 93
- `Testing`: 93
- `APIs`: 92
- `Accessibility`: 92

### Recent Timeline

- `2026-06-28T06:50:35+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-28T06:25:41+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-27T22:51:50+08:00` | **Write one behavior per test** (Testing)
- `2026-06-27T22:08:13+08:00` | **Use virtual environments by default** (Python)
- `2026-06-27T21:17:55+08:00` | **Prefer small focused commits** (Git)
- `2026-06-27T20:09:18+08:00` | **Write decisions down** (Leadership)
- `2026-06-27T19:33:18+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-27T15:10:41+08:00` | **Measure before tuning** (Performance)
- `2026-06-27T13:48:30+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-27T10:45:15+08:00` | **Retry only safe operations** (Networking)
