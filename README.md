# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2597**
- Today's entries: **26**
- Today's note: `notes/2026-08-15.md`

### Latest Entry

- Timestamp: `2026-08-15T18:06:22+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 130
- `Accessibility`: 130
- `Architecture`: 130
- `Backend`: 130
- `CI/CD`: 130

### Recent Timeline

- `2026-08-15T18:06:22+08:00` | **Write decisions down** (Leadership)
- `2026-08-15T17:51:55+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-15T17:24:36+08:00` | **Measure before tuning** (Performance)
- `2026-08-15T16:56:18+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-15T16:24:41+08:00` | **Retry only safe operations** (Networking)
- `2026-08-15T15:55:55+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-15T15:43:52+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-15T13:53:25+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-15T13:25:00+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-15T12:43:14+08:00` | **Automate rollback paths** (DevOps)
