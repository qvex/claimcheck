/**
 * src/api.ts
 *
 * GOAL: The only place that makes (non-streaming) HTTP calls. Components ask for data. They never call fetch.
 *
 * CONSTRAINTS
 *   - The backend base URL is defined once.
 *   - Non-2xx responses become errors that carry a useful message (status + the server's detail).
 *   - Every function is typed with the shapes from types.ts.
 *   - The chat stream doesn't belong here (it's stateful; see the hook).
 *
 * DONE WHEN
 *   - Every component that needs data imports from here, and grep finds no fetch() in components/.
 */
