# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2553**
- Today's entries: **10**
- Today's note: `notes/2026-08-14.md`

### Latest Entry

- Timestamp: `2026-08-14T12:17:29+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 128
- `Architecture`: 128
- `Backend`: 128
- `Code Quality`: 128
- `Databases`: 128

### Recent Timeline

- `2026-08-14T12:17:29+08:00` | **Retry only safe operations** (Networking)
- `2026-08-14T11:30:07+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-14T10:36:49+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-14T09:34:15+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-14T08:53:07+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-14T08:27:26+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-14T07:46:17+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-14T07:16:29+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-14T06:46:20+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-14T06:16:47+08:00` | **Log with stable keys** (Observability)
