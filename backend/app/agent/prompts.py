"""System prompt for the expense agent.

SHOULD CONTAIN
- `SYSTEM_PROMPT`: a template with a `{today}` placeholder (the LLM needs it to resolve "yesterday").
- Rules the prompt must state clearly:
    1. New spending -> always call `add_expense` (the app will ask the user to confirm).
    2. Never invent or guess amounts or dates. If one is missing, ask a clarifying question instead.
    3. Spending questions -> call `query_expenses`. Never do arithmetic from memory.
    4. Policy questions -> call `search_policy` and cite the section name in the answer.
    5. Currency defaults to INR. Keep answers short.
- A function like `build_system_message(today: date)` that fills the template.

AVOID
- Hardcoding the date.
- Huge prompts. Tool docstrings also reach the LLM, so don't repeat them here.
"""
