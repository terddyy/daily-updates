# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1642**
- Today's entries: **5**
- Today's note: `notes/2026-06-12.md`

### Latest Entry

- Timestamp: `2026-06-12T10:00:47+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 83
- `Security`: 83
- `Testing`: 83
- `APIs`: 82
- `Accessibility`: 82

### Recent Timeline

- `2026-06-12T10:00:47+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-06-12T09:01:51+08:00` | **Rotate credentials on schedule** (Security)
- `2026-06-12T07:53:08+08:00` | **Write one behavior per test** (Testing)
- `2026-06-12T07:13:25+08:00` | **Use virtual environments by default** (Python)
- `2026-06-12T06:41:08+08:00` | **Prefer small focused commits** (Git)
- `2026-06-11T22:48:39+08:00` | **Write decisions down** (Leadership)
- `2026-06-11T21:26:27+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-11T19:48:54+08:00` | **Measure before tuning** (Performance)
- `2026-06-11T18:11:40+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-11T16:35:37+08:00` | **Retry only safe operations** (Networking)
