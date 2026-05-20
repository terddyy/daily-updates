# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1333**
- Today's entries: **12**
- Today's note: `notes/2026-05-20.md`

### Latest Entry

- Timestamp: `2026-05-20T18:36:26+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 67
- `Architecture`: 67
- `Backend`: 67
- `Code Quality`: 67
- `Databases`: 67

### Recent Timeline

- `2026-05-20T18:36:26+08:00` | **Retry only safe operations** (Networking)
- `2026-05-20T17:30:07+08:00` | **Batch similar tasks** (Productivity)
- `2026-05-20T16:12:54+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-05-20T14:49:42+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-05-20T13:26:21+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-05-20T11:47:20+08:00` | **Automate rollback paths** (DevOps)
- `2026-05-20T10:22:43+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-05-20T09:19:37+08:00` | **Optimize first contentful view** (Frontend)
- `2026-05-20T08:09:45+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-05-20T07:40:15+08:00` | **Log with stable keys** (Observability)
