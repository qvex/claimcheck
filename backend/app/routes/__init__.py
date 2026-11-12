"""HTTP route modules.

Each module defines one APIRouter, and main.py includes them all. Routes stay thin: validate input,
call the repository or the graph, and shape the response. No business logic.
"""
