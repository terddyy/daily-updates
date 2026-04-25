# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **213**
- Today's entries: **8**
- Today's note: `notes/2026-04-26.md`

### Latest Entry

- Timestamp: `2026-04-26T07:11:53+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 11
- `Architecture`: 11
- `Backend`: 11
- `Code Quality`: 11
- `Databases`: 11

### Recent Timeline

- `2026-04-26T07:11:53+08:00` | **Retry only safe operations** (Networking)
- `2026-04-26T06:08:45+08:00` | **Batch similar tasks** (Productivity)
- `2026-04-26T05:11:25+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-04-26T04:10:55+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-04-26T03:17:06+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-04-26T02:12:27+08:00` | **Automate rollback paths** (DevOps)
- `2026-04-26T01:14:03+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-04-26T00:11:47+08:00` | **Optimize first contentful view** (Frontend)
- `2026-04-25T23:14:17+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-04-25T22:16:17+08:00` | **Log with stable keys** (Observability)
