# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1562**
- Today's entries: **4**
- Today's note: `notes/2026-06-06.md`

### Latest Entry

- Timestamp: `2026-06-06T11:47:02+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 79
- `Security`: 79
- `Testing`: 79
- `APIs`: 78
- `Accessibility`: 78

### Recent Timeline

- `2026-06-06T11:47:02+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-06T10:21:27+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-06T08:09:26+08:00` | **Write one behavior per test** (Testing)
- `2026-06-06T06:29:13+08:00` | **Use virtual environments by default** (Python)
- `2026-06-05T22:41:07+08:00` | **Prefer small focused commits** (Git)
- `2026-06-05T21:35:33+08:00` | **Write decisions down** (Leadership)
- `2026-06-05T20:26:52+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-05T19:25:49+08:00` | **Measure before tuning** (Performance)
- `2026-06-05T18:08:04+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-05T16:33:22+08:00` | **Retry only safe operations** (Networking)
