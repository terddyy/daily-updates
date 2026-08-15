# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2613**
- Today's entries: **4**
- Today's note: `notes/2026-08-16.md`

### Latest Entry

- Timestamp: `2026-08-16T07:37:06+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 131
- `Architecture`: 131
- `Backend`: 131
- `Code Quality`: 131
- `Databases`: 131

### Recent Timeline

- `2026-08-16T07:37:06+08:00` | **Retry only safe operations** (Networking)
- `2026-08-16T07:05:37+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-16T06:51:40+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-16T06:23:56+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-15T22:52:05+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-15T22:39:06+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-15T22:23:52+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-15T22:06:32+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-15T21:43:54+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-15T21:28:48+08:00` | **Log with stable keys** (Observability)
