"""Tools the LLM can call. Each one is typed, small and backed by repository.py or rag/search.py.

SHOULD CONTAIN (use LangChain's @tool decorator or StructuredTool, with Pydantic args schemas)
- `add_expense(amount, currency, category, description, spent_on)`
    Inserts via repository.add_expense(source="agent"). By the time this runs, confirm_node has already
    obtained human approval. Returns a short confirmation string including the new id.
- `query_expenses(category=None, start_date=None, end_date=None, group_by="category")`
    Calls repository.summarize and returns compact JSON or text totals.
- `search_policy(query, k=3)`
    Calls rag.search and returns the top chunks formatted as "[Section] content", so the LLM can cite them.
- `TOOLS`: the list of all three, used both for llm.bind_tools(...) and for the ToolNode.

IMPORTANT
- Tool docstrings and argument descriptions ARE the instructions the LLM sees. Write them carefully.
- Each tool opens and closes its own DB session (tools run outside a request).

AVOID
- A free-form "run_sql" tool (no text-to-SQL).
- Returning huge payloads. Keep tool outputs short to save tokens.

CONCEPTS PRACTICED: tool calling, typed tool schemas, separating LLM decisions from deterministic execution.
"""
