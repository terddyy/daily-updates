# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **2773**
- Today's entries: **16**
- Today's note: `notes/2026-08-22.md`

### Latest Entry

- Timestamp: `2026-08-22T22:47:50+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 139
- `Architecture`: 139
- `Backend`: 139
- `Code Quality`: 139
- `Databases`: 139

### Recent Timeline

- `2026-08-22T22:47:50+08:00` | **Retry only safe operations** (Networking)
- `2026-08-22T22:20:30+08:00` | **Batch similar tasks** (Productivity)
- `2026-08-22T21:18:49+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-08-22T20:37:49+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-08-22T18:32:33+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-08-22T17:59:27+08:00` | **Automate rollback paths** (DevOps)
- `2026-08-22T17:34:55+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-08-22T16:59:25+08:00` | **Optimize first contentful view** (Frontend)
- `2026-08-22T16:29:17+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-08-22T12:48:58+08:00` | **Log with stable keys** (Observability)
