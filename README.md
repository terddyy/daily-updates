# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2477**
- Today's entries: **23**
- Today's note: `notes/2026-08-11.md`

### Latest Entry

- Timestamp: `2026-08-11T17:35:42+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 124
- `Accessibility`: 124
- `Architecture`: 124
- `Backend`: 124
- `CI/CD`: 124

### Recent Timeline

- `2026-08-11T17:35:42+08:00` | **Write decisions down** (Leadership)
- `2026-08-11T17:08:02+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-11T16:35:39+08:00` | **Measure before tuning** (Performance)
- `2026-08-11T16:11:53+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-11T15:42:29+08:00` | **Retry only safe operations** (Networking)
- `2026-08-11T15:09:11+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-11T14:33:21+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-11T14:02:45+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-11T13:39:49+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-11T13:13:55+08:00` | **Automate rollback paths** (DevOps)
