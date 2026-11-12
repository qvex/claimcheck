"""Application entry point: creates and wires the FastAPI app.

Run with: uvicorn app.main:app --reload   (from the backend/ directory)

SHOULD CONTAIN
- Creating the FastAPI instance (a title/version shows up nicely in /docs).
- CORS middleware allowing `settings.FRONTEND_ORIGIN` (the Vite dev server), so the browser can call the API.
- Including every router from `app.routes` (health, expenses, chat, policy).
- A lifespan handler (startup/shutdown) that:
    1. ensures the `vector` extension exists and creates ORM tables (Base.metadata.create_all),
    2. opens the async Postgres connection used by the LangGraph checkpointer and calls its `setup()`
       (creates checkpoint tables),
    3. builds the compiled graph once via `app.agent.graph.build_graph(checkpointer)` and stores it on
       `app.state` so routes can reuse it,
    4. closes connections on shutdown.

AVOID
- Business logic or SQL here. This file only assembles pieces.
- Building the graph per request. Build it once at startup.

CONCEPTS PRACTICED: app factory/wiring, middleware, lifespan events, shared app state.
"""
