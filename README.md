# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2517**
- Today's entries: **2**
- Today's note: `notes/2026-08-13.md`

### Latest Entry

- Timestamp: `2026-08-13T06:46:22+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 126
- `Accessibility`: 126
- `Architecture`: 126
- `Backend`: 126
- `CI/CD`: 126

### Recent Timeline

- `2026-08-13T06:46:22+08:00` | **Write decisions down** (Leadership)
- `2026-08-13T06:16:28+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-08-12T22:52:21+08:00` | **Measure before tuning** (Performance)
- `2026-08-12T22:28:01+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-08-12T21:47:04+08:00` | **Retry only safe operations** (Networking)
- `2026-08-12T21:09:33+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-12T20:31:56+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-12T20:00:38+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-12T19:31:18+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-12T19:07:12+08:00` | **Automate rollback paths** (DevOps)
