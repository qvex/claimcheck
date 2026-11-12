"""Database plumbing: engine, sessions and the FastAPI session dependency.

SHOULD CONTAIN
- `engine`: a SQLAlchemy 2.0 engine created from settings.DATABASE_URL (psycopg driver).
- `SessionLocal`: a sessionmaker bound to the engine.
- `Base`: the DeclarativeBase that all ORM models in models.py inherit from.
- `get_db()`: a generator dependency that yields a session and always closes it (try/finally).
  Routes receive it via `Depends(get_db)`.
- (Optional) a small helper that opens a session outside a request, for agent tools and ingest scripts.

DESIGN NOTE
- Use the plain synchronous ORM today; FastAPI runs sync dependencies in a threadpool, which is fine.
  The LangGraph checkpointer uses its own async connection, set up in main.py, and that's OK.

AVOID
- A global session shared across requests (sessions are not thread-safe).

CONCEPTS PRACTICED: connection management, dependency injection, unit-of-work sessions.
"""
