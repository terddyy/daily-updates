# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1879**
- Today's entries: **14**
- Today's note: `notes/2026-06-30.md`

### Latest Entry

- Timestamp: `2026-06-30T19:46:19+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 94
- `Accessibility`: 94
- `Architecture`: 94
- `Backend`: 94
- `CI/CD`: 94

### Recent Timeline

- `2026-06-30T19:46:19+08:00` | **Use virtual environments by default** (Python)
- `2026-06-30T18:44:51+08:00` | **Prefer small focused commits** (Git)
- `2026-06-30T17:31:50+08:00` | **Write decisions down** (Leadership)
- `2026-06-30T16:14:30+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-30T14:52:30+08:00` | **Measure before tuning** (Performance)
- `2026-06-30T13:27:49+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-30T11:46:57+08:00` | **Retry only safe operations** (Networking)
- `2026-06-30T10:22:05+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-30T09:18:06+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-30T08:09:00+08:00` | **Use exponential backoff with jitter** (Reliability)
