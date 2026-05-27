# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1442**
- Today's entries: **3**
- Today's note: `notes/2026-05-28.md`

### Latest Entry

- Timestamp: `2026-05-28T07:30:58+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 73
- `Security`: 73
- `Testing`: 73
- `APIs`: 72
- `Accessibility`: 72

### Recent Timeline

- `2026-05-28T07:30:58+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-28T06:49:35+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-28T06:10:11+08:00` | **Write one behavior per test** (Testing)
- `2026-05-27T22:45:25+08:00` | **Use virtual environments by default** (Python)
- `2026-05-27T21:34:14+08:00` | **Prefer small focused commits** (Git)
- `2026-05-27T20:07:01+08:00` | **Write decisions down** (Leadership)
- `2026-05-27T18:53:14+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-27T17:28:15+08:00` | **Measure before tuning** (Performance)
- `2026-05-27T16:09:13+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-27T14:32:21+08:00` | **Retry only safe operations** (Networking)
