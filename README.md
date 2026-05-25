# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1402**
- Today's entries: **6**
- Today's note: `notes/2026-05-25.md`

### Latest Entry

- Timestamp: `2026-05-25T09:21:22+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 71
- `Security`: 71
- `Testing`: 71
- `APIs`: 70
- `Accessibility`: 70

### Recent Timeline

- `2026-05-25T09:21:22+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-25T08:08:43+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-25T07:37:31+08:00` | **Write one behavior per test** (Testing)
- `2026-05-25T07:07:22+08:00` | **Use virtual environments by default** (Python)
- `2026-05-25T06:36:27+08:00` | **Prefer small focused commits** (Git)
- `2026-05-25T06:06:16+08:00` | **Write decisions down** (Leadership)
- `2026-05-24T22:34:18+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-24T21:11:13+08:00` | **Measure before tuning** (Performance)
- `2026-05-24T20:40:07+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-24T20:07:23+08:00` | **Retry only safe operations** (Networking)
