# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2459**
- Today's entries: **5**
- Today's note: `notes/2026-08-11.md`

### Latest Entry

- Timestamp: `2026-08-11T07:44:38+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 123
- `Accessibility`: 123
- `Architecture`: 123
- `Backend`: 123
- `CI/CD`: 123

### Recent Timeline

- `2026-08-11T07:44:38+08:00` | **Use virtual environments by default** (Python)
- `2026-08-11T07:16:41+08:00` | **Prefer small focused commits** (Git)
- `2026-08-11T06:59:11+08:00` | **Write decisions down** (Leadership)
- `2026-08-11T06:31:25+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-11T06:14:12+08:00` | **Measure before tuning** (Performance)
- `2026-08-10T22:39:10+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-10T22:11:58+08:00` | **Retry only safe operations** (Networking)
- `2026-08-10T21:31:37+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-10T20:48:36+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-10T20:19:29+08:00` | **Use exponential backoff with jitter** (Reliability)
