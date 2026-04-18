# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **33**
- Today's entries: **11**
- Today's note: `notes/2026-04-18.md`

### Latest Entry

- Timestamp: `2026-04-18T11:02:07+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 2
- `Architecture`: 2
- `Backend`: 2
- `Code Quality`: 2
- `Databases`: 2

### Recent Timeline

- `2026-04-18T11:02:07+08:00` | **Retry only safe operations** (Networking)
- `2026-04-18T09:33:45+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-18T08:20:45+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-18T07:13:22+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-18T06:12:35+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-18T05:14:42+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-18T04:13:35+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-18T03:24:27+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-18T02:17:13+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-18T01:17:17+08:00` | **Log with stable keys** (Observability)
