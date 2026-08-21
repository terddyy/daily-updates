# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2753**
- Today's entries: **18**
- Today's note: `notes/2026-08-21.md`

### Latest Entry

- Timestamp: `2026-08-21T19:33:28+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 138
- `Architecture`: 138
- `Backend`: 138
- `Code Quality`: 138
- `Databases`: 138

### Recent Timeline

- `2026-08-21T19:33:28+08:00` | **Retry only safe operations** (Networking)
- `2026-08-21T18:59:18+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-21T18:29:43+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-21T17:51:52+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-21T17:07:08+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-21T16:19:42+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-21T15:41:55+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-21T14:45:23+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-21T13:47:38+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-21T13:04:19+08:00` | **Log with stable keys** (Observability)
