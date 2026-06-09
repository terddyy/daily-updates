# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1602**
- Today's entries: **7**
- Today's note: `notes/2026-06-09.md`

### Latest Entry

- Timestamp: `2026-06-09T11:46:45+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 81
- `Security`: 81
- `Testing`: 81
- `APIs`: 80
- `Accessibility`: 80

### Recent Timeline

- `2026-06-09T11:46:45+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-09T10:21:58+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-09T09:17:45+08:00` | **Write one behavior per test** (Testing)
- `2026-06-09T08:11:57+08:00` | **Use virtual environments by default** (Python)
- `2026-06-09T07:42:38+08:00` | **Prefer small focused commits** (Git)
- `2026-06-09T07:10:42+08:00` | **Write decisions down** (Leadership)
- `2026-06-09T06:35:05+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-08T22:10:04+08:00` | **Measure before tuning** (Performance)
- `2026-06-08T20:32:29+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-08T18:55:11+08:00` | **Retry only safe operations** (Networking)
