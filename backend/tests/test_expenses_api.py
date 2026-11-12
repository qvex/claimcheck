"""API tests for /expenses.

SHOULD COVER
- POST a valid expense -> 201, response echoes the fields, source == "manual".
- POST with amount <= 0, an unknown category, or an empty description -> 422.
- GET returns created expenses; date and category filters work.
- DELETE an existing id -> 204, then it's gone. DELETE an unknown id -> 404.
- GET /expenses/summary?month=... -> correct per-category totals. A bad month format -> 422.
"""
