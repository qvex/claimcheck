"""GOAL: Expose expenses over REST for the table, the summary and the manual form.

CONTRACT
  The /expenses rows in the "ClaimCheck - Spec Sheet" note, section 7.

CONSTRAINTS
  - Handlers are thin: validate, delegate to the repository, shape the response.
  - Status codes carry meaning (created, no content, not found, validation error). No errors smuggled inside 200s.
  - Every route declares its response shape, so /docs is accurate.

DONE WHEN
  - Every row of the API table works from /docs, including the failure cases.
  - test_expenses_api.py passes.

LOOK UP
  - FastAPI APIRouter
  - HTTPException
  - response_model / status_code
"""
