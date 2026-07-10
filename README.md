# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2037**
- Today's entries: **13**
- Today's note: `notes/2026-07-10.md`

### Latest Entry

- Timestamp: `2026-07-10T18:35:10+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 102
- `Accessibility`: 102
- `Architecture`: 102
- `Backend`: 102
- `CI/CD`: 102

### Recent Timeline

- `2026-07-10T18:35:10+08:00` | **Write decisions down** (Leadership)
- `2026-07-10T17:28:15+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-07-10T16:12:06+08:00` | **Measure before tuning** (Performance)
- `2026-07-10T14:57:56+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-07-10T13:39:27+08:00` | **Retry only safe operations** (Networking)
- `2026-07-10T12:10:41+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-10T10:44:34+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-10T09:42:57+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-10T08:58:27+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-10T08:10:55+08:00` | **Automate rollback paths** (DevOps)
