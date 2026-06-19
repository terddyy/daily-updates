# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1722**
- Today's entries: **4**
- Today's note: `notes/2026-06-19.md`

### Latest Entry

- Timestamp: `2026-06-19T09:39:07+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 87
- `Security`: 87
- `Testing`: 87
- `APIs`: 86
- `Accessibility`: 86

### Recent Timeline

- `2026-06-19T09:39:07+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-19T08:15:37+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-19T07:36:22+08:00` | **Write one behavior per test** (Testing)
- `2026-06-19T06:46:14+08:00` | **Use virtual environments by default** (Python)
- `2026-06-18T22:33:17+08:00` | **Prefer small focused commits** (Git)
- `2026-06-18T21:28:58+08:00` | **Write decisions down** (Leadership)
- `2026-06-18T20:10:32+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-18T18:47:33+08:00` | **Measure before tuning** (Performance)
- `2026-06-18T17:02:47+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-18T15:19:31+08:00` | **Retry only safe operations** (Networking)
