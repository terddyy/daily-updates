# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1817**
- Today's entries: **4**
- Today's note: `notes/2026-06-26.md`

### Latest Entry

- Timestamp: `2026-06-26T08:09:33+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 91
- `Accessibility`: 91
- `Architecture`: 91
- `Backend`: 91
- `CI/CD`: 91

### Recent Timeline

- `2026-06-26T08:09:33+08:00` | **Write decisions down** (Leadership)
- `2026-06-26T07:32:01+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-06-26T06:48:57+08:00` | **Measure before tuning** (Performance)
- `2026-06-26T06:12:38+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-06-25T22:18:45+08:00` | **Retry only safe operations** (Networking)
- `2026-06-25T21:17:26+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-25T20:20:51+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-25T19:27:30+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-25T18:28:01+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-25T17:25:13+08:00` | **Automate rollback paths** (DevOps)
