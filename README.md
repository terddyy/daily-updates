# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **100**
- Today's entries: **10**
- Today's note: `notes/2026-04-21.md`

### Latest Entry

- Timestamp: `2026-04-21T09:33:37+08:00`
- Title: **Write one behavior per test**
- Category: `Testing`
- Source: https://martinfowler.com/bliki/UnitTest.html
- Summary: Single-purpose tests fail with clearer intent and reduce time spent diagnosing what actually regressed.

### Top Categories

- `Testing`: 6
- `APIs`: 5
- `Accessibility`: 5
- `Architecture`: 5
- `Backend`: 5

### Recent Timeline

- `2026-04-21T09:33:37+08:00` | **Write one behavior per test** (Testing)
- `2026-04-21T08:23:39+08:00` | **Use virtual environments by default** (Python)
- `2026-04-21T07:15:15+08:00` | **Prefer small focused commits** (Git)
- `2026-04-21T06:14:45+08:00` | **Write decisions down** (Leadership)
- `2026-04-21T05:15:54+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-21T04:14:29+08:00` | **Measure before tuning** (Performance)
- `2026-04-21T03:24:50+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-21T02:19:05+08:00` | **Retry only safe operations** (Networking)
- `2026-04-21T01:22:36+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-21T00:25:40+08:00` | **Keep runbooks close to code** (Documentation)
