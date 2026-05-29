# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1457**
- Today's entries: **4**
- Today's note: `notes/2026-05-29.md`

### Latest Entry

- Timestamp: `2026-05-29T08:10:26+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 73
- `Accessibility`: 73
- `Architecture`: 73
- `Backend`: 73
- `CI/CD`: 73

### Recent Timeline

- `2026-05-29T08:10:26+08:00` | **Write decisions down** (Leadership)
- `2026-05-29T07:36:10+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-29T06:58:59+08:00` | **Measure before tuning** (Performance)
- `2026-05-29T06:21:15+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-28T21:50:32+08:00` | **Retry only safe operations** (Networking)
- `2026-05-28T20:26:07+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-28T19:02:46+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-28T17:33:23+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-28T16:08:22+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-28T14:31:58+08:00` | **Automate rollback paths** (DevOps)
