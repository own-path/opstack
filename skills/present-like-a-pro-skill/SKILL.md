---
name: present-like-a-pro-skill
description: "Creates high-impact presentation decks using the Present Like a Pro Figma resource for warm red and cream palettes, dramatic typography, angled compositions, slide systems, and narrative pacing. Use when the user mentions Present Like a Pro, pitch decks, presentation design, slide storytelling, keynote visuals, or asks to create or improve presentation frames in .fig format."
compatibility: "Works in Claude.ai, Claude Code, and API environments that can inspect images or import Figma .fig files."
metadata:
  author: "Kole Jain"
  version: "1.0.0"
  category: "ui-design"
  source-file: "Present like a pro.fig"
---

# Present Like a Pro

## Purpose

Use this skill to create, implement, or critique high-impact presentation decks with warm red and cream palettes, dramatic typography, angled compositions, and coherent narrative pacing. Ground decisions in the bundled Kole Jain reference, but adapt content, brand, and interaction details to the user's actual product.

## Bundled assets

- `assets/Present like a pro.fig` — original editable Figma resource
- `assets/thumbnail.png` — quick visual overview

Inspect the thumbnail first, then import or inspect the `.fig` file when detailed values, states, or layouts matter. If the environment cannot open the `.fig` file, state that limitation and use only visible evidence from the thumbnail. Never invent exact tokens or hidden states.

## Use cases

1. Design a cohesive pitch or keynote deck from a written outline.
2. Turn dense slides into a paced visual narrative.
3. Create a reusable slide system with strong opening, evidence, and closing moments.

## Workflow

### 1. Define the outcome

Identify the product, audience, target surface, primary task, required states, and implementation format. If the brief leaves the subject open, propose a concrete subject and single page or screen job before designing.

### 2. Study the reference

Inspect the bundled assets for layout hierarchy, type roles, spacing rhythm, color roles, components, content density, responsive behavior, and interaction states. Separate reusable principles from resource-specific copy and imagery.

### 3. Extract the design grammar

- Treat each slide as one beat with one claim, not a page of documentation.
- Use warm cream, red, and dark accents with high-contrast display typography.
- Employ angle, crop, and scale to create energy while maintaining a stable grid.
- Alternate dense evidence slides with simple emphatic moments to control pacing.
- Keep recurring labels, numbers, and page furniture consistent across the deck.

### 4. Plan before building

Produce a compact plan containing:

- A 4–6 color role system with named hex values
- Display, body, and utility typography roles
- Layout rules and a small ASCII wireframe when structure is not obvious
- The reusable components and states required
- One subject-specific signature element
- Responsive, keyboard, focus, contrast, and reduced-motion behavior

If exact values cannot be verified from the source, label proposed values as adaptations.

### 5. Create or revise

Use real, domain-specific content. Build the information architecture first, then components, visual styling, and motion. Preserve semantic HTML and native interaction behavior in code. When modifying an existing design, keep what already works and explain material departures from the reference.

### 6. Critique and refine

Compare the result with the brief and reference. Remove generic patterns that are unrelated to the subject. Verify at least one wide and one narrow layout. When visual tooling is available, inspect a rendered screenshot and revise visible issues before finalizing.

## Quality gates

- [ ] Every slide communicates its point in a few seconds.
- [ ] The deck has a clear beginning, escalation, proof, and conclusion.
- [ ] Text remains legible when projected and exported.
- [ ] The result has one clear visual thesis tied to the product and audience.
- [ ] Real content, empty, loading, error, and overflow states are handled where relevant.
- [ ] Contrast, keyboard focus, touch targets, and reduced motion are addressed.
- [ ] No decorative element competes with the primary task.

## Examples

**Example 1**

User says: “Turn this 12-point outline into a bold presentation deck.”

Apply the workflow, cite the relevant reference grammar, create or revise the requested artifact, then run every quality gate.
**Example 2**

User says: “Redesign my pitch deck with stronger pacing and fewer words per slide.”

Apply the workflow, cite the relevant reference grammar, create or revise the requested artifact, then run every quality gate.

## Troubleshooting

### The `.fig` file cannot be opened

Use `assets/thumbnail.png` for visible composition cues. Ask for exported frames only when hidden details would materially change the result. Do not claim to have inspected inaccessible layers.

### Fonts or images are unavailable

Choose replacements that preserve the same role, contrast, and visual weight. Record substitutions instead of silently treating them as exact matches.

### The output feels generic

Return to the product's subject, audience, and single job. Keep the relevant reference grammar, replace default copy and imagery, and strengthen one justified signature element.

### The brief conflicts with the reference

The user's explicit requirements win. Preserve only the reference principles that support the requested outcome.
