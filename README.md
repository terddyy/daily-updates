# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **153**
- Today's entries: **17**
- Today's note: `notes/2026-04-23.md`

### Latest Entry

- Timestamp: `2026-04-23T16:34:56+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 8
- `Architecture`: 8
- `Backend`: 8
- `Code Quality`: 8
- `Databases`: 8

### Recent Timeline

- `2026-04-23T16:34:56+08:00` | **Retry only safe operations** (Networking)
- `2026-04-23T16:12:17+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-23T15:33:41+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-23T14:36:47+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-23T13:50:49+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-23T12:59:16+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-23T11:02:36+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-23T09:33:38+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-23T08:26:14+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-23T07:17:01+08:00` | **Log with stable keys** (Observability)
