# Authentication and Permissions

## Admin Token Test

```bash
python auth_script.py
# Enter your token: (Admin token)
```

| Endpoint | Method | Status | Result |
|---|---|---|---|
| No Token | GET | 401 | Authentication credentials were not provided |
| /books/ | GET | 200 | Success |
| /book_all/ | POST | 201 | Created |
| /book_all/8/ | PATCH | 200 | Updated |
| /book_all/13/ | DELETE | 204 | Deleted |

#### No Token — 401 Unauthorized
```json
{"detail": "Authentication credentials were not provided."}
```

#### GET /books/ — 200 OK
```json
[
    {"id": 6,  "title": "tell my son to hold on to his gun", "author": "scarino",        "created_at": "2026-02-22 06:55:42", "published_date": "2001-02-10"},
    {"id": 7,  "title": "gideon",                           "author": "scarino",        "created_at": "2026-02-22 19:10:56", "published_date": "2026-01-13"},
    {"id": 8,  "title": "Updated Book Title",               "author": "Ama Atta Aidoo", "created_at": "2026-02-22 19:11:41", "published_date": "2002-01-13"},
    {"id": 10, "title": "New API Book",                     "author": "System Script",  "created_at": "2026-02-22 19:22:07", "published_date": "2010-01-13"},
    {"id": 11, "title": "New API Book",                     "author": "System Script",  "created_at": "2026-02-22 19:25:35", "published_date": "2010-01-13"},
    {"id": 12, "title": "New API Book",                     "author": "System Script",  "created_at": "2026-02-22 19:26:20", "published_date": "2010-01-13"},
    {"id": 13, "title": "New API Book",                     "author": "System Script",  "created_at": "2026-02-22 19:28:57", "published_date": "2010-01-13"}
]
```

#### POST /book_all/ — 201 Created
```json
{"id": 14, "title": "New API Book", "author": "System Script", "created_at": "2026-02-22 19:31:50", "published_date": "2010-01-13"}
```

#### PATCH /book_all/8/ — 200 OK
```json
{"id": 8, "title": "Updated Book Title", "author": "Ama Atta Aidoo", "created_at": "2026-02-22 19:11:41", "published_date": "2002-01-13"}
```

#### DELETE /book_all/13/ — 204 No Content
```
No response body
```

---

## Non-Admin Token Test

```bash
python auth_script.py
# Enter your token: (Non-admin token)
```

| Endpoint | Method | Status | Result |
|---|---|---|---|
| No Token | GET | 401 | Authentication credentials were not provided |
| /books/ | GET | 200 | Success |
| /book_all/ | POST | 403 | Permission denied |
| /book_all/8/ | PATCH | 403 | Permission denied |
| /book_all/13/ | DELETE | 403 | Permission denied |

#### No Token — 401 Unauthorized
```json
{"detail": "Authentication credentials were not provided."}
```

#### GET /books/ — 200 OK
```json
[
    {"id": 6,  "title": "tell my son to hold on to his gun", "author": "scarino",        "created_at": "2026-02-22 06:55:42", "published_date": "2001-02-10"},
    {"id": 7,  "title": "gideon",                           "author": "scarino",        "created_at": "2026-02-22 19:10:56", "published_date": "2026-01-13"},
    {"id": 8,  "title": "Updated Book Title",               "author": "Ama Atta Aidoo", "created_at": "2026-02-22 19:11:41", "published_date": "2002-01-13"},
    {"id": 10, "title": "New API Book",                     "author": "System Script",  "created_at": "2026-02-22 19:22:07", "published_date": "2010-01-13"},
    {"id": 11, "title": "New API Book",                     "author": "System Script",  "created_at": "2026-02-22 19:25:35", "published_date": "2010-01-13"},
    {"id": 12, "title": "New API Book",                     "author": "System Script",  "created_at": "2026-02-22 19:26:20", "published_date": "2010-01-13"},
    {"id": 14, "title": "New API Book",                     "author": "System Script",  "created_at": "2026-02-22 19:31:50", "published_date": "2010-01-13"}
]
```

#### POST /book_all/ — 403 Forbidden
```json
{"detail": "You do not have permission to perform this action."}
```

#### PATCH /book_all/8/ — 403 Forbidden
```json
{"detail": "You do not have permission to perform this action."}
```

#### DELETE /book_all/13/ — 403 Forbidden
```json
{"detail": "You do not have permission to perform this action."}
```

---

## Summary

| Action | No Token | Non-Admin | Admin |
|---|---|---|---|
| GET /books/ | 401 | 200 ✅ | 200 ✅ |
| POST /book_all/ | 401 | 403 ❌ | 201 ✅ |
| PATCH /book_all/{id}/ | 401 | 403 ❌ | 200 ✅ |
| DELETE /book_all/{id}/ | 401 | 403 ❌ | 204 ✅ |

> **401 Unauthorized** — No token provided. Identity is unknown.
>
> **403 Forbidden** — Valid token provided but user lacks admin privileges.
>
> **200 / 201 / 204** — Admin token grants full read and write access.
