"""Repository tests. The money math must be exactly right.

SHOULD COVER
- summarize() totals by category over a date range, including boundaries (the first and last day of the month).
- Decimal precision: e.g. 0.10 + 0.20 sums to exactly 0.30.
- An empty range returns zero totals (not an error).
- group_by="day" returns one row per day that has spending.
"""
