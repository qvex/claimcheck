/**
 * src/components/ConfirmCard.tsx
 *
 * GOAL: The human-in-the-loop moment. The user sees exactly what will be saved, and decides.
 *
 * CONTRACT
 *   Supports the three decisions the backend accepts: approve, edit, reject.
 *
 * CONSTRAINTS
 *   - Nothing is saved without an explicit user action.
 *   - Edited values are validated before they're sent.
 *   - A decision can't be submitted twice.
 *
 * DONE WHEN
 *   - Approve saves one row, reject saves none, edit saves the edited values.
 */
