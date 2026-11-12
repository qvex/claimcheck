"""GOAL: Be the single gateway to the expenses table. The REST routes and the agent tools both go through it.

CONTRACT
  Supports everything the API (spec section 7) and the agent tools (spec section 5) need: add, list with filters, delete, and totals.

CONSTRAINTS
  - Queries are parameterized. No SQL built from strings.
  - Totals are computed by the database, not by summing in Python.
  - Deleting something that doesn't exist is distinguishable from success.
  - Read operations never commit.

DONE WHEN
  - Repository tests pass, including month boundaries and exact decimal sums.
  - Neither routes/ nor agent/ contains a direct query on expenses.

LOOK UP
  - SQLAlchemy 2.0 select() with group_by and func.sum
"""
