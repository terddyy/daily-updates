# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **157**
- Today's entries: **21**
- Today's note: `notes/2026-04-23.md`

### Latest Entry

- Timestamp: `2026-04-23T19:24:58+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 8
- `Accessibility`: 8
- `Architecture`: 8
- `Backend`: 8
- `CI/CD`: 8

### Recent Timeline

- `2026-04-23T19:24:58+08:00` | **Write decisions down** (Leadership)
- `2026-04-23T18:30:24+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-23T17:33:17+08:00` | **Measure before tuning** (Performance)
- `2026-04-23T16:45:19+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-23T16:34:56+08:00` | **Retry only safe operations** (Networking)
- `2026-04-23T16:12:17+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-23T15:33:41+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-23T14:36:47+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-23T13:50:49+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-23T12:59:16+08:00` | **Automate rollback paths** (DevOps)
