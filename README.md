# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **117**
- Today's entries: **4**
- Today's note: `notes/2026-04-22.md`

### Latest Entry

- Timestamp: `2026-04-22T03:27:45+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 6
- `Accessibility`: 6
- `Architecture`: 6
- `Backend`: 6
- `CI/CD`: 6

### Recent Timeline

- `2026-04-22T03:27:45+08:00` | **Write decisions down** (Leadership)
- `2026-04-22T02:21:32+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-04-22T01:22:19+08:00` | **Measure before tuning** (Performance)
- `2026-04-22T00:24:00+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-04-21T23:28:11+08:00` | **Retry only safe operations** (Networking)
- `2026-04-21T22:33:54+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-21T21:32:55+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-21T20:20:01+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-21T19:25:20+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-21T18:29:17+08:00` | **Automate rollback paths** (DevOps)
