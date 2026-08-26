# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2837**
- Today's entries: **7**
- Today's note: `notes/2026-08-26.md`

### Latest Entry

- Timestamp: `2026-08-26T11:52:56+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 142
- `Accessibility`: 142
- `Architecture`: 142
- `Backend`: 142
- `CI/CD`: 142

### Recent Timeline

- `2026-08-26T11:52:56+08:00` | **Write decisions down** (Leadership)
- `2026-08-26T10:46:58+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-26T09:17:11+08:00` | **Measure before tuning** (Performance)
- `2026-08-26T07:49:33+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-26T07:26:29+08:00` | **Retry only safe operations** (Networking)
- `2026-08-26T06:56:14+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-26T06:26:39+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-25T22:21:19+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-25T21:27:35+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-25T20:15:52+08:00` | **Automate rollback paths** (DevOps)
