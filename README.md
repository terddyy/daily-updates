# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2882**
- Today's entries: **3**
- Today's note: `notes/2026-09-06.md`

### Latest Entry

- Timestamp: `2026-09-06T06:34:34+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 145
- `Security`: 145
- `Testing`: 145
- `APIs`: 144
- `Accessibility`: 144

### Recent Timeline

- `2026-09-06T06:34:34+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-09-06T06:20:56+08:00` | **Rotate credentials on schedule** (Security)
- `2026-09-06T06:09:45+08:00` | **Write one behavior per test** (Testing)
- `2026-09-05T22:48:14+08:00` | **Use virtual environments by default** (Python)
- `2026-09-05T22:34:55+08:00` | **Prefer small focused commits** (Git)
- `2026-09-05T22:21:42+08:00` | **Write decisions down** (Leadership)
- `2026-09-05T22:10:14+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-09-05T21:34:27+08:00` | **Measure before tuning** (Performance)
- `2026-09-05T21:21:16+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-09-05T21:09:51+08:00` | **Retry only safe operations** (Networking)
