# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1579**
- Today's entries: **7**
- Today's note: `notes/2026-06-07.md`

### Latest Entry

- Timestamp: `2026-06-07T19:22:02+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 79
- `Accessibility`: 79
- `Architecture`: 79
- `Backend`: 79
- `CI/CD`: 79

### Recent Timeline

- `2026-06-07T19:22:02+08:00` | **Use virtual environments by default** (Python)
- `2026-06-07T17:39:28+08:00` | **Prefer small focused commits** (Git)
- `2026-06-07T16:24:32+08:00` | **Write decisions down** (Leadership)
- `2026-06-07T15:09:01+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-07T08:09:04+08:00` | **Measure before tuning** (Performance)
- `2026-06-07T07:37:36+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-07T07:08:54+08:00` | **Retry only safe operations** (Networking)
- `2026-06-06T22:37:53+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-06T21:11:31+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-06T20:33:24+08:00` | **Use exponential backoff with jitter** (Reliability)
