/**
 * src/components/ConfirmCard.tsx
 *
 * PURPOSE
 *   The human-in-the-loop UI. Shows the expense the agent parsed and waits for the user's decision before
 *   anything is saved.
 *
 * PROPS: expense (the interrupt payload), onDecision(decision, editedExpense?)
 *
 * SHOULD CONTAIN
 *   - A read-only summary by default: amount (formatted with currency), category, date, description.
 *   - Approve / Edit / Reject buttons.
 *   - Edit mode: a controlled mini-form pre-filled with the parsed values and basic validation
 *     (amount > 0, date present); Save sends decision "edit" with the edited values.
 *   - Buttons disabled while the resume request is in flight (prevents double submission).
 *
 * CONCEPTS PRACTICED: conditional rendering, local component state, controlled forms, preventing double submit.
 */
