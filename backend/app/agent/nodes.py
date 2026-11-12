"""Graph nodes and routing functions.

SHOULD CONTAIN
- `agent_node(state)`
    Prepends the system message, calls the chat model with TOOLS bound, and returns {"messages": [response]}.
- `confirm_node(state)`  <- the human-in-the-loop step
    Finds the `add_expense` tool call in the last AI message, then calls `interrupt({...expense args...})`.
    That pauses the graph, saves state and surfaces the payload to the client. When the user resumes:
      approve -> return nothing (go on to tools, which executes the insert)
      edit    -> return an updated AI message (SAME message id, edited tool-call args), so the reducer replaces it
      reject  -> return a ToolMessage for that tool call saying "user rejected", then route back to agent_node
- `tools_node`: LangGraph's prebuilt ToolNode(TOOLS) is fine here.
- `route_after_agent(state)` -> "confirm" if there's an add_expense call, "tools" for other tool calls,
  END if there are no tool calls.
- `route_after_confirm(state)` -> "tools" (approved/edited) or "agent" (rejected).

CONCEPT TO UNDERSTAND
- On resume, LangGraph RE-RUNS the interrupted node from the top. Any code before `interrupt()` must be
  side-effect free.

AVOID: inserting into the DB inside confirm_node. Only the tool writes.
"""
