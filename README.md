# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1593**
- Today's entries: **12**
- Today's note: `notes/2026-06-08.md`

### Latest Entry

- Timestamp: `2026-06-08T18:55:11+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 80
- `Architecture`: 80
- `Backend`: 80
- `Code Quality`: 80
- `Databases`: 80

### Recent Timeline

- `2026-06-08T18:55:11+08:00` | **Retry only safe operations** (Networking)
- `2026-06-08T17:07:45+08:00` | **Batch similar tasks** (Productivity)
- `2026-06-08T15:16:58+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-06-08T13:39:54+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-06-08T11:49:25+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-06-08T10:26:09+08:00` | **Automate rollback paths** (DevOps)
- `2026-06-08T09:26:25+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-06-08T08:09:45+08:00` | **Optimize first contentful view** (Frontend)
- `2026-06-08T07:38:21+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-06-08T07:10:13+08:00` | **Log with stable keys** (Observability)
