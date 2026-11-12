"""GOAL: Give the rest of the backend a safe way to talk to Postgres.

CONSTRAINTS
  - Each request gets its own session, and it's always cleaned up, even on errors.
  - Code that runs outside a request (agent tools, the ingest script) also needs a way to get a session.
  - Models elsewhere need a shared declarative base to inherit from.

DONE WHEN
  - From a REPL you can open a session, run a trivial query and close it.

FRAMEWORK HINTS (only the parts that would otherwise block you)
  - Plain synchronous SQLAlchemy is fine today. FastAPI runs sync dependencies in a threadpool. The LangGraph checkpointer manages its own async connection separately.

LOOK UP
  - SQLAlchemy 2.0 engine and sessions
  - FastAPI dependencies with yield
"""
