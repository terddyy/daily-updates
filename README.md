# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **93**
- Today's entries: **3**
- Today's note: `notes/2026-04-21.md`

### Latest Entry

- Timestamp: `2026-04-21T02:19:05+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 5
- `Architecture`: 5
- `Backend`: 5
- `Code Quality`: 5
- `Databases`: 5

### Recent Timeline

- `2026-04-21T02:19:05+08:00` | **Retry only safe operations** (Networking)
- `2026-04-21T01:22:36+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-21T00:25:40+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-20T23:29:14+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-20T22:34:00+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-20T21:33:20+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-20T20:22:31+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-20T19:29:58+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-20T18:33:28+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-20T17:35:06+08:00` | **Log with stable keys** (Observability)
