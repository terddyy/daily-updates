# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1413**
- Today's entries: **2**
- Today's note: `notes/2026-05-26.md`

### Latest Entry

- Timestamp: `2026-05-26T06:55:44+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 71
- `Architecture`: 71
- `Backend`: 71
- `Code Quality`: 71
- `Databases`: 71

### Recent Timeline

- `2026-05-26T06:55:44+08:00` | **Retry only safe operations** (Networking)
- `2026-05-26T06:29:59+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-25T22:23:53+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-25T21:15:49+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-25T19:48:47+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-25T18:15:33+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-25T16:43:54+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-25T15:11:20+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-25T13:37:32+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-25T11:47:45+08:00` | **Log with stable keys** (Observability)
