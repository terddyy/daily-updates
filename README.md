# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1622**
- Today's entries: **12**
- Today's note: `notes/2026-06-10.md`

### Latest Entry

- Timestamp: `2026-06-10T20:24:55+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 82
- `Security`: 82
- `Testing`: 82
- `APIs`: 81
- `Accessibility`: 81

### Recent Timeline

- `2026-06-10T20:24:55+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-10T19:03:17+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-10T17:31:56+08:00` | **Write one behavior per test** (Testing)
- `2026-06-10T16:10:06+08:00` | **Use virtual environments by default** (Python)
- `2026-06-10T14:32:49+08:00` | **Prefer small focused commits** (Git)
- `2026-06-10T12:51:03+08:00` | **Write decisions down** (Leadership)
- `2026-06-10T11:13:18+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-10T09:50:14+08:00` | **Measure before tuning** (Performance)
- `2026-06-10T08:58:52+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-10T07:46:08+08:00` | **Retry only safe operations** (Networking)
