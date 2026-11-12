"""The agent's state schema: what flows between graph nodes and is saved by the checkpointer.

SHOULD CONTAIN
- `AgentState`: a TypedDict with one key, `messages`, annotated with LangGraph's `add_messages` reducer.

CONCEPT TO UNDERSTAND (write a one-line comment explaining it in your own words)
- A *reducer* decides how a node's returned update merges into existing state. `add_messages` appends new
  messages, and replaces a message that has the same id. confirm_node relies on that when the user edits
  an expense.
- LangGraph has a built-in `MessagesState` that does the same thing. Define your own once to learn how it works.

AVOID: putting things in state that can be derived (e.g. the pending expense already lives in the tool call).
"""
