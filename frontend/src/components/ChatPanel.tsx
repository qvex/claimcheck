/**
 * src/components/ChatPanel.tsx
 *
 * PURPOSE
 *   The left column: the conversation with the agent.
 *
 * PROPS: threadId, onExpenseSaved
 *
 * SHOULD CONTAIN
 *   - Calls useChatStream(...) and renders <MessageList /> and, ONLY when status === "awaiting_confirm",
 *     <ConfirmCard />.
 *   - A controlled text input + Send button. Submit on Enter; disable while streaming or awaiting confirmation.
 *   - Error display with a "try again" affordance.
 *   - Auto-scroll to the newest message (a ref + an effect).
 *
 * CONCEPTS PRACTICED: composition, controlled inputs, conditional rendering, refs.
 */
