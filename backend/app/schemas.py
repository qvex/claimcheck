"""GOAL: Define the API's data contract: what the server accepts and returns.

CONTRACT
  the "ClaimCheck - Spec Sheet" note: the categories (section 5), the API spec (section 7), and the resume decisions (approve / reject / edit).

CONSTRAINTS
  - Invalid input is rejected with a 422 before any business logic runs.
  - Business rules a client could violate (positive amounts, known categories, non-empty text, sensible dates) are validated here.
  - An 'edit' decision without the edited expense must be rejected.
  - Reuse shapes instead of duplicating them. The agent's add-expense tool should share the same input model.

DONE WHEN
  - Bad payloads sent from /docs produce clear 422 errors, and good ones round-trip unchanged.

LOOK UP
  - Pydantic v2 field constraints and validators
  - Pydantic from_attributes
"""
