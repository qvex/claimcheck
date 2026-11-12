/**
 * src/components/AddExpenseForm.tsx
 *
 * PURPOSE
 *   The manual, non-agent way to add an expense (and practice for plain React forms).
 *
 * PROPS: onSaved() (the parent bumps refreshKey)
 *
 * SHOULD CONTAIN
 *   - Controlled inputs: amount, category (a select from the Category union), description, date (defaults to today).
 *   - Client-side validation that mirrors the backend rules, with inline error messages.
 *   - On submit: api.createExpense(...), a disabled button while saving, server-error display,
 *     and resetting the form on success.
 *
 * NOTE: the backend validates again. Client validation is for UX, server validation is for correctness.
 */
