<!--
backend/data/policy.md

PURPOSE
  The source document for RAG. `app/rag/ingest.py` splits it on "## " headings: each section
  becomes one row in `policy_chunks` (section title + content + embedding).

GUIDANCE
  - Keep one rule-topic per "## " section, so retrieved chunks are self-contained and citable.
  - This is FICTIONAL sample data. Edit freely, then re-run the ingest endpoint.
  - Content below is copied from the spec sheet.
-->

# Expense Policy (Sample)

## Meals
Team meals are reimbursable up to ₹800 per person when at least one client or 3+ teammates attend. Solo meals are reimbursable only during travel.

## Travel
Economy flights and AC 3-tier train are reimbursable. Cabs are reimbursable for airport and station transfers and after 9 PM.

## Lodging
Hotels up to ₹5,000 per night in metro cities and ₹3,500 elsewhere.

## Software & Subscriptions
Requires manager pre-approval. Personal streaming services are never reimbursable.

## Office Supplies
Up to ₹2,000 per month without approval.

## Submission
Expenses must be submitted within 30 days with a receipt. Amounts over ₹5,000 need a manager's sign-off.
