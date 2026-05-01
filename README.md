# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **762**
- Today's entries: **490**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:11:37+08:00`
- Title: **Add indexes for real query patterns**
- Category: `Databases`
- Source: https://use-the-index-luke.com/
- Summary: Measure slow queries first, then index based on predicates and sort order. Over-indexing harms write performance.

### Top Categories

- `Databases`: 39
- `Security`: 39
- `Testing`: 39
- `APIs`: 38
- `Accessibility`: 38

### Recent Timeline

- `2026-05-01T09:11:37+08:00` | **Add indexes for real query patterns** (Databases)
- `2026-05-01T09:11:36+08:00` | **Rotate credentials on schedule** (Security)
- `2026-05-01T09:11:35+08:00` | **Write one behavior per test** (Testing)
- `2026-05-01T09:11:34+08:00` | **Use virtual environments by default** (Python)
- `2026-05-01T09:11:33+08:00` | **Prefer small focused commits** (Git)
- `2026-05-01T09:11:32+08:00` | **Write decisions down** (Leadership)
- `2026-05-01T09:11:31+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-01T09:11:30+08:00` | **Measure before tuning** (Performance)
- `2026-05-01T09:11:29+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-01T09:11:28+08:00` | **Retry only safe operations** (Networking)
