# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **297**
- Today's entries: **25**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:03:52+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 15
- `Accessibility`: 15
- `Architecture`: 15
- `Backend`: 15
- `CI/CD`: 15

### Recent Timeline

- `2026-05-01T09:03:52+08:00` | **Write decisions down** (Leadership)
- `2026-05-01T09:03:51+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-01T09:03:50+08:00` | **Measure before tuning** (Performance)
- `2026-05-01T09:03:49+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-01T09:03:48+08:00` | **Retry only safe operations** (Networking)
- `2026-05-01T09:03:47+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-01T09:03:46+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-01T09:03:45+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-01T09:03:44+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-01T09:03:43+08:00` | **Automate rollback paths** (DevOps)
