# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2317**
- Today's entries: **11**
- Today's note: `notes/2026-08-05.md`

### Latest Entry

- Timestamp: `2026-08-05T14:36:53+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 116
- `Accessibility`: 116
- `Architecture`: 116
- `Backend`: 116
- `CI/CD`: 116

### Recent Timeline

- `2026-08-05T14:36:53+08:00` | **Write decisions down** (Leadership)
- `2026-08-05T13:31:00+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-05T12:22:36+08:00` | **Measure before tuning** (Performance)
- `2026-08-05T11:11:19+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-05T09:58:48+08:00` | **Retry only safe operations** (Networking)
- `2026-08-05T09:12:18+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-05T08:36:06+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-05T07:49:36+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-05T07:24:14+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-05T06:54:13+08:00` | **Automate rollback paths** (DevOps)
