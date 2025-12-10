# Playbook: migrating from raw SQL strings to SQLAlchemy (Core + ORM)

This repository (`austrian-code-wizard/c3po`) currently does not include a database layer or any raw SQL usage. This playbook is therefore forward-looking guidance for when you add persistence or analytics storage to the project, or when you reuse this document in a codebase that already has DB-API style SQL calls.

The goal is to move from ad-hoc SQL string execution to SQLAlchemy 2.x-style usage with explicit transaction boundaries, safe parameter binding, and consistent result handling. The recommended approach is incremental: first wrap existing SQL using SQLAlchemy’s `Engine` and `text()` so behavior stays stable, and only then translate high-value queries to SQLAlchemy Core / ORM constructs.

Primary references from the SQLAlchemy project are linked throughout, especially the unified tutorial on `select()` and result handling, session lifecycle guidance, engine/connection patterns, and the SQLAlchemy 2.0 migration notes.

## 1. Prerequisites and conventions

Pick SQLAlchemy 2.x and consistently use the 2.0-style APIs (the unified tutorial + `Session.execute(select(...))` patterns). If you copy snippets from older blog posts, you’ll frequently see legacy patterns like `session.query(...)` or “connectionless execution”; avoid them because they don’t match SQLAlchemy’s current recommended style.

You’ll also need a DBAPI driver appropriate to your database (for example `psycopg`/`psycopg2` for Postgres, `pymysql` for MySQL, etc.). This playbook does not prescribe a specific database.

Useful starting points in the official docs:

- Using SELECT statements (Core and ORM share the `select()` construct): https://docs.sqlalchemy.org/en/latest/tutorial/data_select.html
- Session lifecycle and transaction scoping: https://docs.sqlalchemy.org/en/latest/orm/session_basics.html
- Engine/connection patterns and transactions: https://docs.sqlalchemy.org/en/latest/core/connections.html
- SQLAlchemy 2.0 migration notes (helps avoid legacy APIs and autocommit assumptions): https://docs.sqlalchemy.org/en/latest/changelog/migration_20.html

## 2. Inventory and migration strategy

Before refactoring code, inventory all places where SQL is executed. In a typical codebase, these show up as DB-API calls like `cursor.execute(...)`, as string literals containing `SELECT` / `INSERT`, or as helper modules like `db.py` / `storage.py`. Classify each callsite as “read only”, “write”, or “multi-step transaction”, and flag any that are performance-sensitive or correctness-critical.

A practical migration strategy is:

First, replace direct DB-API connection management with an SQLAlchemy `Engine`, but keep SQL text unchanged (bridge phase). Second, for new code, prefer SQLAlchemy Core or ORM immediately. Third, iteratively translate existing raw SQL callsites into Core/ORM equivalents when it pays off (maintainability, type safety, composability, portability), while allowing vendor-specific textual SQL to remain when translation would be risky.

## 3. Phase 1 (bridge): keep SQL text, but execute it via SQLAlchemy

This phase is intentionally boring. The point is to get safe parameter binding, consistent transaction scoping, and consistent results without rewriting the SQL itself.

### 3.1 Replace DB-API cursors with `Engine` + `Connection`

Raw DB-API style:

```python
# illustrative example (DB-API)
cur.execute(
    "SELECT id, name FROM users WHERE id = %s",
    (user_id,),
)
row = cur.fetchone()
```

SQLAlchemy Core bridge style (textual SQL):

```python
from sqlalchemy import create_engine, text

engine = create_engine(DB_URL)

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT id, name FROM users WHERE id = :user_id"),
        {"user_id": user_id},
    )
    row = result.mappings().first()
```

The `Connection` pattern and transaction scoping recommendations are covered in “Working with Engines and Connections” (and the related “Using Transactions” subsections): https://docs.sqlalchemy.org/en/latest/core/connections.html

### 3.2 Always bind parameters; never format values into SQL strings

Even if you stay with textual SQL long-term, SQLAlchemy’s `text()` construct exists specifically so you can bind parameters instead of interpolating. The API-level documentation for `text()` is here: https://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.text

Bad (unsafe; defeats DB-API parameter binding):

```python
sql = f"SELECT * FROM users WHERE email = '{email}'"  # don’t do this
conn.execute(text(sql))
```

Good (bind parameter):

```python
conn.execute(
    text("SELECT * FROM users WHERE email = :email"),
    {"email": email},
)
```

### 3.3 Put each unit of work inside an explicit transaction

With SQLAlchemy 2.x style, aim to have an explicit transaction scope for writes and for multi-step reads that must be consistent. A simple default is to use `engine.begin()` for Core or `session.begin()` for ORM, which will commit on success and roll back on error.

Core example:

```python
with engine.begin() as conn:
    conn.execute(text("UPDATE users SET name = :name WHERE id = :id"), {"id": user_id, "name": name})
```

ORM example:

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    with session.begin():
        session.execute(text("UPDATE users SET name = :name WHERE id = :id"), {"id": user_id, "name": name})
```

For transaction and session lifecycle patterns, see the “Session Basics” section that explains how a `Session` acquires connections and manages transactions: https://docs.sqlalchemy.org/en/latest/orm/session_basics.html

## 4. Phase 2: translate textual SQL to SQLAlchemy Core

Core is a good “next step” when you want to keep thinking in tables/columns and SQL operations, but want composability and safer refactors.

### 4.1 Simple SELECT

Raw SQL:

```sql
SELECT id, name FROM users WHERE id = :user_id
```

Core:

```python
from sqlalchemy import Table, Column, Integer, String, MetaData, select

metadata = MetaData()
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

stmt = select(users.c.id, users.c.name).where(users.c.id == user_id)

with engine.connect() as conn:
    row = conn.execute(stmt).mappings().first()
```

The `select()` construct is introduced in the unified tutorial: https://docs.sqlalchemy.org/en/latest/tutorial/data_select.html

### 4.2 INSERT / UPDATE / DELETE

Core provides `insert()`, `update()`, and `delete()` constructs that you execute via a `Connection` within a transaction. For most projects, the consistent rule is “DML happens under `engine.begin()`”.

## 5. Phase 3: translate Core patterns to the ORM

Use the ORM when you want a domain model (mapped classes), relationship loading, and a unit-of-work approach for writes. SQLAlchemy 2.x encourages using the same `select()` construct for ORM queries and then executing it via `Session.execute()`.

ORM quick start: https://docs.sqlalchemy.org/orm/quickstart.html

ORM query guide (2.0-style querying): https://docs.sqlalchemy.org/en/latest/orm/queryguide/

### 5.1 ORM SELECT

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

stmt = select(User).where(User.id == user_id)

with Session(engine) as session:
    user = session.execute(stmt).scalars().first()
```

Note that selecting ORM entities yields `Row` objects by default; using `.scalars()` extracts the entity stream.

## 6. Result handling: map DB-API fetches to SQLAlchemy `Result`

DB-API patterns like `fetchone()` / `fetchall()` map to SQLAlchemy’s `Result` API. Prefer `.mappings()` when you want dict-like access by column name, and prefer `.scalars()` when selecting a single column or when selecting ORM entities and you want instances rather than `Row` wrappers. The unified tutorial illustrates execution and result iteration around `select()`: https://docs.sqlalchemy.org/en/latest/tutorial/data_select.html

## 7. Common pitfalls to avoid

Avoid mixing old and new SQLAlchemy styles. In particular, don’t introduce legacy `session.query(...)` or “connectionless execution” patterns if your target is SQLAlchemy 2.x.

Avoid implicit transaction assumptions and driver-level autocommit behavior. SQLAlchemy 2.0 tightened execution semantics and removed library-level autocommit patterns; the migration guide is a useful checklist of behaviors to avoid inheriting from older codebases: https://docs.sqlalchemy.org/en/latest/changelog/migration_20.html

Avoid sharing a single `Session` across threads or unrelated units of work. Keep sessions short-lived and scoped to a logical operation (a request, a job step, etc.), using context managers as shown in the session basics guide: https://docs.sqlalchemy.org/en/latest/orm/session_basics.html

## 8. Review checklist (per migrated callsite)

When converting a raw SQL callsite, verify that dynamic values are passed as bound parameters (not interpolated into SQL text), that execution runs under an explicit transaction scope appropriate for the operation, that connections/sessions are closed via context managers, that result handling returns the same shape (scalar vs row vs mapping vs ORM entity) as before, and that there is a regression test covering both success and failure/rollback behavior.

## 9. References

- SQLAlchemy Unified Tutorial: Using SELECT statements: https://docs.sqlalchemy.org/en/latest/tutorial/data_select.html
- SQLAlchemy ORM: Session Basics: https://docs.sqlalchemy.org/en/latest/orm/session_basics.html
- SQLAlchemy Core: Working with Engines and Connections: https://docs.sqlalchemy.org/en/latest/core/connections.html
- SQLAlchemy Core API: `text()` construct: https://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.text
- SQLAlchemy 2.0 Migration Guide: https://docs.sqlalchemy.org/en/latest/changelog/migration_20.html
