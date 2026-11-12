/**
 * src/App.tsx
 *
 * PURPOSE
 *   Top-level layout and the owner of the state shared by both sides of the page.
 *
 * SHOULD CONTAIN
 *   - Two-column layout: <ChatPanel /> on the left; <SummaryBar />, <AddExpenseForm /> and <ExpenseTable /> on the right.
 *   - `threadId` state: read from localStorage on first load (create a new id with crypto.randomUUID()
 *     if missing). It's passed to ChatPanel, so a refresh continues the same conversation.
 *   - `refreshKey` state (a number): incremented when the agent saves an expense or the manual form submits.
 *     Passed to ExpenseTable and SummaryBar so they refetch. This is "lifting state up".
 *   - (Optional) a "New conversation" button that resets threadId.
 *
 * AVOID: fetching data here. Children own their own data loading.
 */
