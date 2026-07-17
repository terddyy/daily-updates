# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2177**
- Today's entries: **20**
- Today's note: `notes/2026-07-17.md`

### Latest Entry

- Timestamp: `2026-07-17T20:44:20+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 109
- `Accessibility`: 109
- `Architecture`: 109
- `Backend`: 109
- `CI/CD`: 109

### Recent Timeline

- `2026-07-17T20:44:20+08:00` | **Write decisions down** (Leadership)
- `2026-07-17T20:14:11+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-17T19:43:57+08:00` | **Measure before tuning** (Performance)
- `2026-07-17T19:03:07+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-17T18:21:35+08:00` | **Retry only safe operations** (Networking)
- `2026-07-17T17:37:20+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-17T16:49:35+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-17T15:55:57+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-17T15:02:47+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-17T14:03:08+08:00` | **Automate rollback paths** (DevOps)
