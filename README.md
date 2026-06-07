# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1582**
- Today's entries: **1**
- Today's note: `notes/2026-06-08.md`

### Latest Entry

- Timestamp: `2026-06-08T06:13:26+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 80
- `Security`: 80
- `Testing`: 80
- `APIs`: 79
- `Accessibility`: 79

### Recent Timeline

- `2026-06-08T06:13:26+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-07T22:26:16+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-07T20:48:45+08:00` | **Write one behavior per test** (Testing)
- `2026-06-07T19:22:02+08:00` | **Use virtual environments by default** (Python)
- `2026-06-07T17:39:28+08:00` | **Prefer small focused commits** (Git)
- `2026-06-07T16:24:32+08:00` | **Write decisions down** (Leadership)
- `2026-06-07T15:09:01+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-07T08:09:04+08:00` | **Measure before tuning** (Performance)
- `2026-06-07T07:37:36+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-07T07:08:54+08:00` | **Retry only safe operations** (Networking)
