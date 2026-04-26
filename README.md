# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **233**
- Today's entries: **6**
- Today's note: `notes/2026-04-27.md`

### Latest Entry

- Timestamp: `2026-04-27T05:11:20+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 12
- `Architecture`: 12
- `Backend`: 12
- `Code Quality`: 12
- `Databases`: 12

### Recent Timeline

- `2026-04-27T05:11:20+08:00` | **Retry only safe operations** (Networking)
- `2026-04-27T04:11:10+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-27T03:18:12+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-27T02:13:11+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-27T01:14:16+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-27T00:13:07+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-26T23:14:30+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-26T22:15:51+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-26T21:28:41+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-26T20:13:04+08:00` | **Log with stable keys** (Observability)
