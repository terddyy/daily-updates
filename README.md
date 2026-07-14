# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2097**
- Today's entries: **6**
- Today's note: `notes/2026-07-14.md`

### Latest Entry

- Timestamp: `2026-07-14T08:49:15+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 105
- `Accessibility`: 105
- `Architecture`: 105
- `Backend`: 105
- `CI/CD`: 105

### Recent Timeline

- `2026-07-14T08:49:15+08:00` | **Write decisions down** (Leadership)
- `2026-07-14T08:04:04+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-14T07:33:20+08:00` | **Measure before tuning** (Performance)
- `2026-07-14T07:06:21+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-14T06:33:48+08:00` | **Retry only safe operations** (Networking)
- `2026-07-14T06:05:07+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-13T22:18:33+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-13T21:18:07+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-13T20:16:45+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-13T19:06:01+08:00` | **Automate rollback paths** (DevOps)
