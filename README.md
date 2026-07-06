# Daily Knowledge Repo MVP

Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.

## AI Trend Source

- Optional daily live trend fetch uses Gemini API with Google Search grounding.
- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.
- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.

## Dashboard

- Total archive entries: **1973**
- Today's entries: **2**
- Today's note: `notes/2026-07-07.md`

### Latest Entry

- Timestamp: `2026-07-07T07:09:20+08:00`
- Title: **Retry only safe operations**
- Category: `Networking`
- Source: https://www.rfc-editor.org/rfc/rfc9110
- Summary: Not all requests should be retried blindly; non-idempotent calls need safeguards or idempotency keys.

### Top Categories

- `APIs`: 99
- `Architecture`: 99
- `Backend`: 99
- `Code Quality`: 99
- `Databases`: 99

### Recent Timeline

- `2026-07-07T07:09:20+08:00` | **Retry only safe operations** (Networking)
- `2026-07-07T06:33:26+08:00` | **Batch similar tasks** (Productivity)
- `2026-07-06T22:45:30+08:00` | **Keep runbooks close to code** (Documentation)
- `2026-07-06T21:32:20+08:00` | **Use exponential backoff with jitter** (Reliability)
- `2026-07-06T20:08:49+08:00` | **Name intent, not mechanics** (Code Quality)
- `2026-07-06T18:36:48+08:00` | **Automate rollback paths** (DevOps)
- `2026-07-06T16:45:26+08:00` | **Set realistic timeouts everywhere** (Backend)
- `2026-07-06T15:13:14+08:00` | **Optimize first contentful view** (Frontend)
- `2026-07-06T13:42:28+08:00` | **Keep boundaries explicit** (Architecture)
- `2026-07-06T12:09:38+08:00` | **Log with stable keys** (Observability)
