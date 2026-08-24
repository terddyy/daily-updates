# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2813**
- Today's entries: **4**
- Today's note: `notes/2026-08-25.md`

### Latest Entry

- Timestamp: `2026-08-25T07:46:36+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 141
- `Architecture`: 141
- `Backend`: 141
- `Code Quality`: 141
- `Databases`: 141

### Recent Timeline

- `2026-08-25T07:46:36+08:00` | **Retry only safe operations** (Networking)
- `2026-08-25T07:21:34+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-25T06:54:05+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-25T06:26:12+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-24T22:41:12+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-24T21:51:52+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-24T20:55:27+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-24T19:56:19+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-24T19:28:00+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-24T18:53:07+08:00` | **Log with stable keys** (Observability)
