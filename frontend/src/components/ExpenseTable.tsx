/**
 * src/components/ExpenseTable.tsx
 *
 * GOAL: Show saved expenses and let the user delete them.
 *
 * CONSTRAINTS
 *   - Loading, error and empty states each look intentional.
 *   - Refreshes when told to by the parent.
 *   - A slow, outdated response can never overwrite a newer one.
 *   - Money is formatted for India (₹, Indian digit grouping).
 *
 * DONE WHEN
 *   - Adding or deleting from anywhere is reflected here, and killing the backend shows a clear error with a retry.
 *
 * LOOK UP
 *   - React: fetching data in effects and avoiding race conditions
 *   - Intl.NumberFormat
 */
