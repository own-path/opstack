---
name: opstack-ui-review
description: "Build or review UI using real content and interaction evidence: responsive layout, accessible controls, loading/error states, mobile behavior, and purposeful motion."
---

# Check the interface people use

Start from the user's task, existing design system, and the actual target screens. Prefer an existing component over inventing another primitive. Use semantic controls with accessible names, keyboard operation, visible focus, and appropriate focus restoration. Inspect hierarchy, spacing, type, contrast, content density, and error recovery against the project's established visual language.

Exercise empty, loading, error, success, disabled, and long-content states where relevant. Check narrow screens, zoom, overflow, slow network responses, and repeated actions. For mobile inspect safe areas, touch targets, keyboard behavior, and scroll interactions. Use real or representative awkward data rather than only ideal samples.

Motion should explain a transition or provide feedback. Prefer compositor-friendly properties, interruptible interactions, and reduced-motion support. Do not animate high-frequency functional data or add decorative delays to routine actions.

If Daryl's installed UI skills are available, load only the relevant one: emil-design-eng, break-ui, mobile-native, gestures, review-animations, or animation-performance. This checklist is self-contained when those optional skills are absent. Use available browser/native tools to observe the changed behavior and screenshots when visual comparisons matter. If visual inspection is unavailable, state the limit instead of claiming visual verification. For a review-only request, return findings without edits.
