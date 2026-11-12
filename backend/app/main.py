"""GOAL: Assemble the application. Every router, middleware and startup task gets wired up here.

CONSTRAINTS
  - No business logic or queries in this file.
  - Expensive things (DB setup, the compiled agent graph) are created once at startup and reused, never per request.
  - The React dev server must be able to call the API from the browser.
  - Grows in stages: health only -> + tables -> + checkpointer and graph (see the build order).

DONE WHEN
  - `uvicorn app.main:app --reload` starts cleanly, and /docs lists every route.
  - Restarting the server doesn't lose data or duplicate setup.

LOOK UP
  - FastAPI lifespan events
  - FastAPI CORS middleware
  - FastAPI app.state
"""
