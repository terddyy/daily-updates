# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1979**
- Today's entries: **8**
- Today's note: `notes/2026-07-07.md`

### Latest Entry

- Timestamp: `2026-07-07T12:47:54+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 99
- `Accessibility`: 99
- `Architecture`: 99
- `Backend`: 99
- `CI/CD`: 99

### Recent Timeline

- `2026-07-07T12:47:54+08:00` | **Use virtual environments by default** (Python)
- `2026-07-07T11:15:23+08:00` | **Prefer small focused commits** (Git)
- `2026-07-07T09:56:45+08:00` | **Write decisions down** (Leadership)
- `2026-07-07T09:03:29+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-07T08:09:15+08:00` | **Measure before tuning** (Performance)
- `2026-07-07T07:38:46+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-07T07:09:20+08:00` | **Retry only safe operations** (Networking)
- `2026-07-07T06:33:26+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-06T22:45:30+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-06T21:32:20+08:00` | **Use exponential backoff with jitter** (Reliability)
