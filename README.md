# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **113**
- Today's entries: **23**
- Today's note: `notes/2026-04-21.md`

### Latest Entry

- Timestamp: `2026-04-21T23:28:11+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 6
- `Architecture`: 6
- `Backend`: 6
- `Code Quality`: 6
- `Databases`: 6

### Recent Timeline

- `2026-04-21T23:28:11+08:00` | **Retry only safe operations** (Networking)
- `2026-04-21T22:33:54+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-21T21:32:55+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-21T20:20:01+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-21T19:25:20+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-21T18:29:17+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-21T17:32:24+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-21T16:35:36+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-21T15:33:05+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-21T14:36:11+08:00` | **Log with stable keys** (Observability)
