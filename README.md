# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **142**
- Today's entries: **6**
- Today's note: `notes/2026-04-23.md`

### Latest Entry

- Timestamp: `2026-04-23T05:17:05+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 8
- `Security`: 8
- `Testing`: 8
- `APIs`: 7
- `Accessibility`: 7

### Recent Timeline

- `2026-04-23T05:17:05+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-04-23T04:19:06+08:00` | **Rotate credentials on schedule** (Security)
- `2026-04-23T03:28:48+08:00` | **Write one behavior per test** (Testing)
- `2026-04-23T02:21:54+08:00` | **Use virtual environments by default** (Python)
- `2026-04-23T01:20:57+08:00` | **Prefer small focused commits** (Git)
- `2026-04-23T00:23:15+08:00` | **Write decisions down** (Leadership)
- `2026-04-22T23:27:50+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-22T22:33:38+08:00` | **Measure before tuning** (Performance)
- `2026-04-22T21:32:23+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-22T20:19:38+08:00` | **Retry only safe operations** (Networking)
