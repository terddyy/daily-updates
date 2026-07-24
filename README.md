# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2233**
- Today's entries: **7**
- Today's note: `notes/2026-07-24.md`

### Latest Entry

- Timestamp: `2026-07-24T19:41:52+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 112
- `Architecture`: 112
- `Backend`: 112
- `Code Quality`: 112
- `Databases`: 112

### Recent Timeline

- `2026-07-24T19:41:52+08:00` | **Retry only safe operations** (Networking)
- `2026-07-24T17:54:34+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-24T15:17:44+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-24T12:32:26+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-24T09:09:32+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-24T07:39:22+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-24T06:32:40+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-23T21:59:31+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-23T19:55:01+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-23T17:57:45+08:00` | **Log with stable keys** (Observability)
