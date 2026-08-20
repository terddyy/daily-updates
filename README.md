# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2733**
- Today's entries: **21**
- Today's note: `notes/2026-08-20.md`

### Latest Entry

- Timestamp: `2026-08-20T21:10:32+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 137
- `Architecture`: 137
- `Backend`: 137
- `Code Quality`: 137
- `Databases`: 137

### Recent Timeline

- `2026-08-20T21:10:32+08:00` | **Retry only safe operations** (Networking)
- `2026-08-20T20:03:29+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-20T19:42:27+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-20T19:03:35+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-20T18:38:59+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-20T17:59:47+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-20T17:16:56+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-20T16:37:49+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-20T15:48:50+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-20T14:58:48+08:00` | **Log with stable keys** (Observability)
