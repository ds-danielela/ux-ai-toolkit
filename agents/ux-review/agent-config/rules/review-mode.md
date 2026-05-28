# Review Mode

The agent operates in one mode for now: **Free Mode**.

---

## Free Mode

**Triggered when:** no persona is specified in the request.

**What the agent does:**
1. Loads `../shared/design-system/components.md`
2. Loads `../shared/design-system/tokens.md`
3. Loads `../shared/design-system/anti-patterns.md`
4. Loads `../shared/research/patterns.md` for behavioral context
5. Applies Nielsen's 10 usability heuristics as a secondary lens
6. Flags issues using the severity framework

**Example triggers:**
```
"Review the settings page for UX issues"
"Run a ux-review on inbox/checkout.png"
```

---

## Persona Mode (not yet active)

> Reserved for when persona files are added to `../shared/research/personas/`.
> When a persona is named in the request, the agent will load that persona's
> file and review through their behavioral lens.
>
> To activate: add a persona `.md` file to `../shared/research/personas/`
> and update this file to describe the trigger logic.
