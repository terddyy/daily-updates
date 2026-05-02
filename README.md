# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1199**
- Today's entries: **427**
- Today's note: `notes/2026-05-02.md`

### Latest Entry

- Timestamp: `2026-05-02T08:45:12+08:00`
- Title: **Use virtual environments by default**
- Category: `Python`
- Source: https://docs.python.org/3/library/venv.html
- Summary: Project-specific virtual environments prevent dependency leaks across projects and make builds more reproducible on CI.

### Top Categories

- `APIs`: 60
- `Accessibility`: 60
- `Architecture`: 60
- `Backend`: 60
- `CI/CD`: 60

### Recent Timeline

- `2026-05-02T08:45:12+08:00` | **Use virtual environments by default** (Python)
- `2026-05-02T08:45:11+08:00` | **Prefer small focused commits** (Git)
- `2026-05-02T08:45:10+08:00` | **Write decisions down** (Leadership)
- `2026-05-02T08:45:09+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-02T08:45:08+08:00` | **Measure before tuning** (Performance)
- `2026-05-02T08:45:07+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-02T08:45:06+08:00` | **Retry only safe operations** (Networking)
- `2026-05-02T08:45:05+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-02T08:45:04+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-02T08:45:03+08:00` | **Use exponential backoff with jitter** (Reliability)
