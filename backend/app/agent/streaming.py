"""Translates LangGraph's streaming output into the app's 5 SSE event types.

This is the boundary layer: the frontend never sees LangGraph's internal format.

SHOULD CONTAIN
- An async generator `stream_events(graph, graph_input, config)` that consumes the graph's async stream
  (stream modes "messages" for tokens and "updates" for node results) and yields SSE-formatted strings:
    event: token      data: {"text": ...}           <- only LLM tokens from the "agent" node (filter on node metadata)
    event: tool       data: {"name": ..., "args": ...}  <- when the agent decides to call a tool
    event: interrupt  data: {"expense": {...}}       <- when an update contains the interrupt payload
    event: done       data: {}
    event: error      data: {"message": ...}
- A tiny helper that formats one SSE frame: "event: <type>", newline, "data: <json>", blank line.
- try/except around the whole stream: on failure emit `error`, and always end with `done` or `error`.

AVOID
- Sending raw LangGraph objects to the client.
- JSON-encoding Decimal/date without a proper encoder.

CONCEPTS PRACTICED: async generators, SSE protocol, stream modes, interrupt detection.
"""
