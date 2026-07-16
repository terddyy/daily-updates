# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2153**
- Today's entries: **18**
- Today's note: `notes/2026-07-16.md`

### Latest Entry

- Timestamp: `2026-07-16T19:53:17+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 108
- `Architecture`: 108
- `Backend`: 108
- `Code Quality`: 108
- `Databases`: 108

### Recent Timeline

- `2026-07-16T19:53:17+08:00` | **Retry only safe operations** (Networking)
- `2026-07-16T19:13:42+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-16T18:29:21+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-16T17:44:11+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-16T16:53:53+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-16T15:56:23+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-16T15:05:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-16T14:03:29+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-16T13:04:50+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-16T11:50:15+08:00` | **Log with stable keys** (Observability)
