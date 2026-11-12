"""Pydantic models: the API contract (what goes in and out over HTTP and to the agent tools).

SHOULD CONTAIN
- `Category`: a string Enum - food, travel, lodging, supplies, software, other.
- `ExpenseCreate`: amount (Decimal, > 0), currency (default "INR", 3 letters), category (Category),
  description (non-empty, length-limited), spent_on (date; consider rejecting future dates).
- `Expense`: ExpenseCreate + id, source, created_at; configured to read from ORM objects (from_attributes).
- `ExpenseFilters` (or plain query params): from/to dates, optional category.
- `SummaryResponse`: month + totals per category (+ grand total).
- `ChatRequest`: thread_id (str), message (non-empty str).
- `ResumeRequest`: thread_id, decision ("approve" | "reject" | "edit"), optional `expense: ExpenseCreate`,
  with a validator that requires `expense` when decision == "edit".

AVOID
- Returning ORM objects directly from routes without a response model.
- Duplicating these shapes by hand in tools. Reuse ExpenseCreate as the add_expense tool's args schema.

CONCEPTS PRACTICED: request/response validation, enums, custom validators, schema reuse.
"""
