"""REST endpoints for expenses (used by the table, summary bar and manual form).

SHOULD CONTAIN (APIRouter with prefix "/expenses", tag "expenses")
- GET    /expenses            ?from=&to=&category=  -> list[Expense]
- POST   /expenses            body ExpenseCreate     -> Expense, status 201, source="manual"
- DELETE /expenses/{id}                               -> 204, or 404 if missing
- GET    /expenses/summary    ?month=YYYY-MM         -> SummaryResponse (validate the month format)
- Every handler takes `db = Depends(get_db)` and delegates to repository.py.
- Explicit `response_model` and `status_code` on each route, so /docs is accurate.

AVOID
- Querying the DB directly in handlers.
- Returning 200 with an error message in the body. Use proper HTTP status codes (HTTPException).

CONCEPTS PRACTICED: REST resource design, status codes, query/path params, response models.
"""
