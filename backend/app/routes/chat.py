"""Chat endpoints that run the LangGraph agent and stream results as Server-Sent Events.

SHOULD CONTAIN
- POST /chat           body ChatRequest
    Builds the run config with `configurable.thread_id` (this is what makes memory work), sends the user
    message into the compiled graph (from app.state), and returns a StreamingResponse with media type
    "text/event-stream" that wraps `agent.streaming.stream_events(...)`.
- POST /chat/resume    body ResumeRequest
    Resumes a paused (interrupted) run for the same thread_id by passing a LangGraph
    `Command(resume=...)` that carries the decision (+ edited expense), and streams the rest the same way.
- (Optional) GET /chat/{thread_id}/history that reads the checkpointed messages, so the UI can restore a
  conversation after a refresh.
- Response headers that disable caching/buffering for SSE (e.g. Cache-Control: no-cache).

AVOID
- Letting an exception escape mid-stream (the browser just sees a broken stream).
  streaming.py should emit an `error` event instead.
- Building a new graph per request.

CONCEPTS PRACTICED: streaming HTTP responses, thread-scoped agent memory, resuming interrupted graphs.
"""
