/**
 * src/main.tsx
 *
 * PURPOSE
 *   Bootstraps React: finds #root in index.html and renders <App /> inside <React.StrictMode>.
 *
 * SHOULD CONTAIN
 *   - The createRoot(...).render(...) call, and the global stylesheet import (App.css).
 *
 * NOTE: StrictMode double-invokes effects in development. If your stream starts twice, that's why.
 *   Handle it with an AbortController cleanup in the effect rather than removing StrictMode.
 */
