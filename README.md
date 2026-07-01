# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1899**
- Today's entries: **2**
- Today's note: `notes/2026-07-02.md`

### Latest Entry

- Timestamp: `2026-07-02T07:10:34+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 95
- `Accessibility`: 95
- `Architecture`: 95
- `Backend`: 95
- `CI/CD`: 95

### Recent Timeline

- `2026-07-02T07:10:34+08:00` | **Use virtual environments by default** (Python)
- `2026-07-02T06:32:21+08:00` | **Prefer small focused commits** (Git)
- `2026-07-01T22:19:22+08:00` | **Write decisions down** (Leadership)
- `2026-07-01T21:25:33+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-01T20:24:04+08:00` | **Measure before tuning** (Performance)
- `2026-07-01T19:24:48+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-01T18:07:14+08:00` | **Retry only safe operations** (Networking)
- `2026-07-01T16:37:46+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-01T15:10:22+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-01T13:37:23+08:00` | **Use exponential backoff with jitter** (Reliability)
