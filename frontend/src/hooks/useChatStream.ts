/**
 * src/hooks/useChatStream.ts
 *
 * PURPOSE
 *   A custom hook that owns everything about talking to the agent: sending messages, reading the SSE stream,
 *   and the human-in-the-loop pause. Components just call it and render what it returns.
 *
 * SIGNATURE (suggested)
 *   useChatStream({ threadId, onExpenseSaved }) -> { messages, status, pendingExpense, error, send, resume }
 *
 * SHOULD CONTAIN
 *   - send(text): append the user message + an empty assistant message, set status "streaming",
 *     POST /chat, then read the stream.
 *   - resume(decision, editedExpense?): POST /chat/resume and read the stream the same way.
 *   - Stream reading: response.body.getReader() + TextDecoder; keep a text buffer; split on blank lines
 *     (the SSE frame boundary); parse the "event:" and "data:" lines; switch on the event type:
 *       token     -> append text to the last assistant message
 *       tool      -> add a tool-activity message ("Searching policy...")
 *       interrupt -> set pendingExpense, status "awaiting_confirm"
 *       done      -> status "idle"; call onExpenseSaved() so the table refreshes
 *       error     -> status "error", keep the message
 *   - An AbortController, aborted on unmount, so a navigation or refresh doesn't leave a dangling stream.
 *
 * AVOID
 *   - EventSource (it only supports GET; your endpoints are POST).
 *   - Stale-closure bugs when appending tokens. Use functional state updates (setX(prev => ...)).
 *   - Assuming one network chunk == one SSE frame (frames can be split across chunks; that's why you buffer).
 */
