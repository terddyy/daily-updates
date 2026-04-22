# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **137**
- Today's entries: **1**
- Today's note: `notes/2026-04-23.md`

### Latest Entry

- Timestamp: `2026-04-23T00:23:15+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 7
- `Accessibility`: 7
- `Architecture`: 7
- `Backend`: 7
- `CI/CD`: 7

### Recent Timeline

- `2026-04-23T00:23:15+08:00` | **Write decisions down** (Leadership)
- `2026-04-22T23:27:50+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-22T22:33:38+08:00` | **Measure before tuning** (Performance)
- `2026-04-22T21:32:23+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-22T20:19:38+08:00` | **Retry only safe operations** (Networking)
- `2026-04-22T19:24:23+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-22T18:29:11+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-22T17:31:32+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-22T16:33:39+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-22T15:33:13+08:00` | **Automate rollback paths** (DevOps)
