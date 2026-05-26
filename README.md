# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1422**
- Today's entries: **11**
- Today's note: `notes/2026-05-26.md`

### Latest Entry

- Timestamp: `2026-05-26T17:17:05+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 72
- `Security`: 72
- `Testing`: 72
- `APIs`: 71
- `Accessibility`: 71

### Recent Timeline

- `2026-05-26T17:17:05+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-26T15:48:36+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-26T14:25:33+08:00` | **Write one behavior per test** (Testing)
- `2026-05-26T12:53:00+08:00` | **Use virtual environments by default** (Python)
- `2026-05-26T11:21:18+08:00` | **Prefer small focused commits** (Git)
- `2026-05-26T09:57:05+08:00` | **Write decisions down** (Leadership)
- `2026-05-26T09:03:51+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-26T07:56:02+08:00` | **Measure before tuning** (Performance)
- `2026-05-26T07:29:34+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-26T06:55:44+08:00` | **Retry only safe operations** (Networking)
