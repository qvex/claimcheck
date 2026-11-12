"""Data-access layer for expenses: the ONLY place that queries the expenses table.

Both the REST routes and the agent tools call these functions, so there's one tested path to the data.

SHOULD CONTAIN
- `add_expense(db, data: ExpenseCreate, source)` -> the created Expense.
- `list_expenses(db, start=None, end=None, category=None)` -> list, newest first.
- `delete_expense(db, expense_id)` -> bool (False if not found, so the route can return 404).
- `summarize(db, start, end, category=None, group_by="category" | "day")` -> totals, computed in SQL
  (GROUP BY + SUM), not by looping in Python.
- A helper converting "YYYY-MM" into a (first_day, last_day) date range.

AVOID
- Raw SQL strings built with f-strings. Use the ORM / bound parameters only.
- Committing inside list/summary functions (they're read-only).

CONCEPTS PRACTICED: repository pattern, parameterized queries, SQL aggregation.
"""
