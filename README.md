# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2273**
- Today's entries: **7**
- Today's note: `notes/2026-07-30.md`

### Latest Entry

- Timestamp: `2026-07-30T19:33:56+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 114
- `Architecture`: 114
- `Backend`: 114
- `Code Quality`: 114
- `Databases`: 114

### Recent Timeline

- `2026-07-30T19:33:56+08:00` | **Retry only safe operations** (Networking)
- `2026-07-30T17:43:15+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-30T15:12:19+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-30T12:20:17+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-30T09:02:29+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-30T07:42:12+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-30T06:39:21+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-29T21:24:01+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-29T19:39:40+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-29T17:21:29+08:00` | **Log with stable keys** (Observability)
