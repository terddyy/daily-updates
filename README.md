# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1639**
- Today's entries: **2**
- Today's note: `notes/2026-06-12.md`

### Latest Entry

- Timestamp: `2026-06-12T07:13:25+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 82
- `Accessibility`: 82
- `Architecture`: 82
- `Backend`: 82
- `CI/CD`: 82

### Recent Timeline

- `2026-06-12T07:13:25+08:00` | **Use virtual environments by default** (Python)
- `2026-06-12T06:41:08+08:00` | **Prefer small focused commits** (Git)
- `2026-06-11T22:48:39+08:00` | **Write decisions down** (Leadership)
- `2026-06-11T21:26:27+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-11T19:48:54+08:00` | **Measure before tuning** (Performance)
- `2026-06-11T18:11:40+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-11T16:35:37+08:00` | **Retry only safe operations** (Networking)
- `2026-06-11T14:54:20+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-11T13:04:34+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-11T11:20:02+08:00` | **Use exponential backoff with jitter** (Reliability)
