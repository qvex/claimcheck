"""(Stretch) Agent graph routing tests, with no real LLM.

SHOULD COVER
- With a fake chat model that returns an add_expense tool call, the graph pauses at confirm (interrupt).
  Resuming with approve inserts exactly one row. Resuming with reject inserts none.
- With a fake model that returns plain text, the graph ends without calling any tool.
- Use an in-memory checkpointer here, not Postgres.
"""
