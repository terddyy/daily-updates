# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2777**
- Today's entries: **4**
- Today's note: `notes/2026-08-23.md`

### Latest Entry

- Timestamp: `2026-08-23T10:44:26+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 139
- `Accessibility`: 139
- `Architecture`: 139
- `Backend`: 139
- `CI/CD`: 139

### Recent Timeline

- `2026-08-23T10:44:26+08:00` | **Write decisions down** (Leadership)
- `2026-08-23T09:18:30+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-23T07:45:30+08:00` | **Measure before tuning** (Performance)
- `2026-08-23T06:20:57+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-22T22:47:50+08:00` | **Retry only safe operations** (Networking)
- `2026-08-22T22:20:30+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-22T21:18:49+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-22T20:37:49+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-22T18:32:33+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-22T17:59:27+08:00` | **Automate rollback paths** (DevOps)
