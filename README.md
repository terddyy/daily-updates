# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1902**
- Today's entries: **5**
- Today's note: `notes/2026-07-02.md`

### Latest Entry

- Timestamp: `2026-07-02T09:45:41+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 96
- `Security`: 96
- `Testing`: 96
- `APIs`: 95
- `Accessibility`: 95

### Recent Timeline

- `2026-07-02T09:45:41+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-07-02T08:54:23+08:00` | **Rotate credentials on schedule** (Security)
- `2026-07-02T07:46:08+08:00` | **Write one behavior per test** (Testing)
- `2026-07-02T07:10:34+08:00` | **Use virtual environments by default** (Python)
- `2026-07-02T06:32:21+08:00` | **Prefer small focused commits** (Git)
- `2026-07-01T22:19:22+08:00` | **Write decisions down** (Leadership)
- `2026-07-01T21:25:33+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-01T20:24:04+08:00` | **Measure before tuning** (Performance)
- `2026-07-01T19:24:48+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-01T18:07:14+08:00` | **Retry only safe operations** (Networking)
