# Designer Workflow Guide

Two AI tools. Different moments. No coding required.

---

## Your workflow, before and after

```
Before                          Now
──────────────────────          ──────────────────────────────────────
NEED arrives                    NEED arrives
  → Read ticket                   → [Skill] Brief synthesis
  → Open Figma                    → Open Figma (with a clear brief)
  → Design                        → Design
  → Weekly sync                   → [Skill] Pre-sync check → fix blockers
  → Iterate                       → Weekly sync (fewer surprises)
  → Handoff                       → Screens on staging
                                  → [Agent] Full audit → report
                                  → Handoff
```

Your Figma work doesn't change. The tools add checkpoints before and after it.

---

## Quick reference

| Moment | Tool | Where to open |
|---|---|---|
| After kick-off | Design Workflow Skill | Claude chat or Cowork |
| Before weekly sync | Design Workflow Skill | Claude chat or Cowork |
| Screens on staging | UX Review Agent | Terminal |

---

## Using the Design Workflow Skill

Open Claude or Cowork. Paste your NEED in this format:

```
NEED: [what problem are we solving?]
Constraints: [anything fixed — regulatory, technical, time]
Research findings: [what you know — note high / medium / low confidence]
Known gaps: [what you don't know yet]
```

If a field is empty, write `none`. You'll get back a design brief with the right components, risks, and open questions — ready to open Figma from.

**Before your sync**, come back to the same chat and paste:

```
Brief: [the brief from before, or describe the goal in one sentence]
Screens: [list each screen — components used, key interactions]
Decisions made: [any deliberate exceptions or trade-offs]
```

You'll get blockers (fix before showing), things to flag in the room, and what looks correct.

→ [Full reference for the skill](tools/design-workflow-skill.md)

---

## Using the UX Review Agent

The agent runs in Terminal. New to Terminal? [What is Terminal?](concepts.md)

**First time only — download the toolkit:**
```bash
git clone https://github.com/ds-danielela/ux-ai-toolkit.git ~/Documents/ux-ai-toolkit
```

**Every time — run a review:**

1. Take a screenshot of the staging screen and drop it into:
   `~/Documents/ux-ai-toolkit/agents/ux-review/inbox/`

2. Open Terminal and run:
```bash
cd ~/Documents/ux-ai-toolkit/agents/ux-review
claude
```

3. Tell the agent:
```
There's a new screen in inbox/. Run a ux-review.
```

4. Find your report in `outputs/` — a `.md` file with every issue, grouped by severity. Takes 1–3 minutes.

5. Press `Ctrl + C` to close when done.

→ [Full reference for the agent](tools/ux-review-agent.md)

---

## Keeping up to date

When the toolkit is updated, run this once in Terminal:
```bash
cd ~/Documents/ux-ai-toolkit
git pull
```

[What is git pull?](concepts.md)

---

## Common questions

**Do I need to know how to code?**
No. Every command you need is written out in this guide.

**Can I review a staging URL instead of a screenshot?**
Yes — tell the agent the URL directly:
```
Review the screen at staging.ourapp.com/screen-name
```

**What if I disagree with a finding?**
Findings are a starting point, not a verdict. Use the "Decisions made" field to document deliberate trade-offs.

**Is anything sent to a server or stored?**
No. Everything runs locally on your laptop.

**Something is broken.**
Screenshot the error and send it to your team lead.
