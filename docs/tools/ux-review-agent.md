# UX Review Agent

Full audit of staging screens against the design system. Writes a structured report with every issue graded by severity.

---

## When to use it

- Screens are live on staging and you want a thorough, documented audit
- You need a report to share with the team or reference in a handoff
- You want to check multiple screens systematically

> **Not sure which tool to use?** If the screen isn't on staging yet, use the [Design Workflow Skill](tools/design-workflow-skill.md) instead.

---

## How to run a review

### Step 1 — Start the agent

```bash
cd ~/Documents/ux-ai-toolkit/agents/ux-review
claude
```

### Step 2 — Give it something to review

Drop a screenshot in `agents/ux-review/inbox/`, then:

```
There's a new screen in inbox/. Run a ux-review.
```

Or point it at a staging URL:

```
Review the screen at staging.ourapp.com/appointments/confirm
```

### Step 3 — Read the report

Reports appear in `agents/ux-review/outputs/` as two files:

- `YYYY-MM-DD-[screen-name].md` — human-readable summary
- `YYYY-MM-DD-[screen-name].json` — structured data for downstream use

---

## What it checks

| Area | What the agent looks for |
|---|---|
| Component usage | Is the right component used for this context? |
| Token compliance | Are spacing, color, and typography values on-scale? |
| Do/don't rules | Does anything violate a named rule from the design system? |
| Labels and copy | Outcome-describing labels? Sentence case? |
| Missing states | Error, loading, and empty states accounted for? |
| Heuristics | Nielsen's 10 usability principles as a secondary lens |

---

## Severity levels

| Level | Meaning |
|---|---|
| **Critical** | Blocks task completion — must fix before shipping |
| **Major** | Design system violation creating inconsistency |
| **Minor** | Works, but a better option exists |
| **Suggestion** | Polish or copy improvement — no rule violated |

---

## Report format

```markdown
# UX Review — [Screen Name]
Date: 2026-05-28 | Screen: inbox/checkout-step2.png

## Critical (1)
- **Payment CTA**: ButtonPrimary used for a destructive action.
  Replace with the destructive variant.

## Major (1)
- **Postcode field**: No inline error on invalid format.
  Add ErrorText below the field.

## Minor (1)
- **Section header**: Font size 13px off the type scale.
  Use LabelSmall token.

## Suggestions (1)
- **Continue button**: Label "Next" doesn't describe the outcome.
  Consider "Continue to payment".

---
Total: 1 Critical, 1 Major, 1 Minor, 1 Suggestion
```

---

## Knowledge the agent uses

The agent loads knowledge from `shared/design-system/` at the start of every review.

| File | What it contains |
|---|---|
| `components/*.json` | Component rules, variants, props, states |
| `docs/components/*.md` | Narrative component guidance |
| `foundations/` | Color tokens, spacing, typography, border, radius |
| `guidelines/do-dont-rules.json` | 50+ named rules with severity levels |
| `guidelines/token-usage-rules.json` | Token constraints |
| `docs/patterns/` | Forms, navigation, loading, notifications |

---

## Component coverage

Not all components have the same level of structured knowledge. See the [Component Coverage](design-system/component-status.md) page for the full map.

| Coverage | Components | What it means |
|---|---|---|
| ✅ Full | 23 | KB JSON + ZH docs — precise, rule-referenced findings |
| 📄 Docs only | 34 | ZH docs only — narrative findings, less precise |
| ❌ None | 2 | Heuristic findings only, clearly labelled |
