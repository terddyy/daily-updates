# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1999**
- Today's entries: **12**
- Today's note: `notes/2026-07-08.md`

### Latest Entry

- Timestamp: `2026-07-08T15:37:25+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 100
- `Accessibility`: 100
- `Architecture`: 100
- `Backend`: 100
- `CI/CD`: 100

### Recent Timeline

- `2026-07-08T15:37:25+08:00` | **Use virtual environments by default** (Python)
- `2026-07-08T14:36:28+08:00` | **Prefer small focused commits** (Git)
- `2026-07-08T13:41:28+08:00` | **Write decisions down** (Leadership)
- `2026-07-08T12:36:16+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-08T11:23:35+08:00` | **Measure before tuning** (Performance)
- `2026-07-08T10:01:37+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-08T09:13:47+08:00` | **Retry only safe operations** (Networking)
- `2026-07-08T08:38:33+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-08T07:48:44+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-08T07:22:13+08:00` | **Use exponential backoff with jitter** (Reliability)
