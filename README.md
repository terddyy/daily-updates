# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2862**
- Today's entries: **2**
- Today's note: `notes/2026-08-31.md`

### Latest Entry

- Timestamp: `2026-08-31T08:50:59+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 144
- `Security`: 144
- `Testing`: 144
- `APIs`: 143
- `Accessibility`: 143

### Recent Timeline

- `2026-08-31T08:50:59+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-08-31T06:39:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-08-30T21:08:09+08:00` | **Write one behavior per test** (Testing)
- `2026-08-30T15:16:31+08:00` | **Use virtual environments by default** (Python)
- `2026-08-30T07:20:13+08:00` | **Prefer small focused commits** (Git)
- `2026-08-29T18:04:24+08:00` | **Write decisions down** (Leadership)
- `2026-08-29T11:10:01+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-28T17:54:46+08:00` | **Measure before tuning** (Performance)
- `2026-08-28T07:54:01+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-27T22:27:48+08:00` | **Retry only safe operations** (Networking)
