# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **637**
- Today's entries: **365**
- Today's note: `notes/2026-05-01.md`

### Latest Entry

- Timestamp: `2026-05-01T09:09:32+08:00`
- Title: **Write decisions down**
- Category: `Leadership`
- Source: https://adr.github.io/
- Summary: Lightweight decision records preserve context, reduce repeated debates, and accelerate onboarding for new contributors.

### Top Categories

- `APIs`: 32
- `Accessibility`: 32
- `Architecture`: 32
- `Backend`: 32
- `CI/CD`: 32

### Recent Timeline

- `2026-05-01T09:09:32+08:00` | **Write decisions down** (Leadership)
- `2026-05-01T09:09:31+08:00` | **Keyboard support is a baseline** (Accessibility)
- `2026-05-01T09:09:30+08:00` | **Measure before tuning** (Performance)
- `2026-05-01T09:09:29+08:00` | **Fail fast on lint and tests** (CI/CD)
- `2026-05-01T09:09:28+08:00` | **Retry only safe operations** (Networking)
- `2026-05-01T09:09:27+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-01T09:09:26+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-01T09:09:25+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-01T09:09:24+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-01T09:09:23+08:00` | **Automate rollback paths** (DevOps)
