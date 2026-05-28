# Designer Workflow Guide

A plain-language guide to the new AI-assisted design workflow.
No coding knowledge required.

---

## What's new and why it matters

You now have two AI tools available at different moments in your design process. They don't replace Figma, Jira, or your weekly syncs — they sit alongside them and do the repetitive checking work so you don't have to.

**The core idea is simple:** before you open Figma, an AI helps you structure your thinking. Before you show your work, an AI checks it against the design system. You spend your time on actual design decisions, not on hunting for the right token or double-checking component rules.

---

## Your workflow, before and after

### Before
```
NEED arrives
    → Read the ticket
    → Open Figma
    → Design
    → Weekly sync
    → Iterate
    → Handoff
```

### Now
```
NEED arrives
    → [AI] Synthesise inputs → get a brief
    → Open Figma with a clear brief
    → Design
    → [AI] Check screens before sync → fix blockers
    → Weekly sync (with fewer surprises)
    → Screens on staging
    → [AI] Full audit → structured report
    → Handoff
```

The Figma part doesn't change. What changes is what happens before and after it.

---

## The two tools

### Tool 1 — Design Workflow Assistant (chat)

**What it is:** a skill inside Claude that you talk to like a colleague.

**What it does:**
- Turns your NEED inputs (ticket, research notes, constraints) into a structured design brief
- Checks your screens against the design system before a sync or formal review
- Flags only the things that would block you — nothing else

**Where you open it:** Claude chat or Cowork — the same place you already use Claude.

**When to use it:**
- Right after a kick-off, before you open Figma
- The day before a weekly sync, to catch blockers early

**What you need to know:** nothing new. If you can type in Claude, you can use this.

---

### Tool 2 — UX Review Agent (terminal)

**What it is:** an AI that runs on your laptop and reviews staging screens autonomously.

**What it does:**
- Takes a screenshot or a staging URL
- Checks it against every design system rule
- Writes a structured report (a readable summary and a machine-readable file)
- Grades every issue by severity: Critical, Major, Minor, Suggestion

**Where you open it:** Terminal — the black window on your Mac. (More on this below.)

**When to use it:**
- When screens are live on staging and you want a thorough, documented audit
- When you need a report to share with the team or reference in a handoff

**What you need to know:** how to open Terminal and run one command. That's it. Step-by-step below.

---

## Using Tool 1 — Design Workflow Assistant

### Step 1: Open Claude or Cowork

Open Claude in your browser or the Cowork desktop app. The Design Workflow Assistant skill activates automatically when you describe what you're working on.

### Step 2: Paste your NEED in this format

Copy this, fill it in, and send it:

```
NEED: [one paragraph — what problem are we solving?]
Constraints: [list anything fixed — regulatory, technical, time]
Research findings: [list what you know, note if high / medium / low confidence]
Known gaps: [list what you don't know yet]
```

If a field is empty, just write "none". The assistant will tell you if it needs anything else.

**Example:**
```
NEED: Patients need to confirm their appointment details before a consultation.
      Currently they call reception. We want a self-service screen.

Constraints:
- Must work on tablet (iPad)
- Cannot collect new data — read-only confirmation only
- Needs to match the existing check-in flow

Research findings:
- 68% of missed appointments happen because patients forgot the time (high confidence)
- Patients over 60 struggle with small touch targets (medium confidence)

Known gaps:
- Don't know if patients have the app installed before arriving
```

### Step 3: Read the brief

The assistant produces a design brief with:
- What you're solving (plain language)
- What you know and don't know
- Which design system components to use
- High-priority risks
- Open questions to resolve before you start

Use the brief as your starting point in Figma. If something is unclear, ask the assistant to expand on it.

### Step 4: Before your sync, paste your screens

When your designs are ready for review, come back to the same chat and paste this:

```
Brief: [paste the brief you got in step 3, or describe the goal]
Screens: [list each screen — what's on it, which components you used]
Decisions made: [any times you deliberately broke a rule or made a trade-off]
```

**Example:**
```
Brief: Self-service appointment confirmation screen for tablet.

Screens:
- Confirmation screen: Page header, patient name, appointment time and location,
  primary button "Confirm", secondary button "I need to change this"
- Success state: Toast notification, return to home button

Decisions made:
- Used a Banner instead of Toast for the success state because the action
  is high-stakes and I wanted it to be more prominent
```

The assistant will flag only blockers (things to fix before showing your work) and things worth raising in the room. If there are no blockers, it will say so explicitly.

---

## Using Tool 2 — UX Review Agent

This tool runs in Terminal. If you've never used Terminal before, follow these steps exactly. You only need to do the setup once.

### First-time setup

**Step 1: Check that Claude Code is installed**

Open Terminal. You can find it by pressing `Cmd + Space` and typing "Terminal".

Type this and press Enter:
```
claude --version
```

If you see a version number, you're ready. If you see an error, ask your team lead to help install Claude Code.

**Step 2: Clone the toolkit (one time only)**

In Terminal, type this and press Enter:
```
git clone https://github.com/ds-danielela/ux-ai-toolkit.git ~/Documents/ux-ai-toolkit
```

This downloads the toolkit to your Documents folder. You only do this once.

---

### Running a review

**Step 1: Take a screenshot of the staging screen**

Take a screenshot of the screen you want to review (or have the staging URL ready). Save it somewhere easy to find — your Desktop is fine.

**Step 2: Open Terminal and go to the agent folder**

Type this and press Enter:
```
cd ~/Documents/ux-ai-toolkit/agents/ux-review
```

Think of this as opening the right drawer in a filing cabinet.

**Step 3: Drop your screenshot into the inbox**

Open Finder. In the menu bar, click Go → Go to Folder and type:
```
~/Documents/ux-ai-toolkit/agents/ux-review/inbox
```

Drag your screenshot into this folder.

**Step 4: Start the agent**

Back in Terminal, type this and press Enter:
```
claude
```

A chat interface opens. Tell it what you want:
```
There's a new screen in inbox/. Run a ux-review.
```

The agent reads the screen, loads the design system rules, and starts the review. This takes 1–3 minutes depending on the screen.

**Step 5: Read the report**

When it's done, open Finder and go to:
```
~/Documents/ux-ai-toolkit/agents/ux-review/outputs
```

You'll find two files with today's date and the screen name:
- `.md` file — human-readable summary, grouped by severity
- `.json` file — structured data (useful if you want to share findings in a tool)

Open the `.md` file. It lists every issue found, where it is, which rule it breaks, and how to fix it.

**Step 6: Close the agent**

When you're done, press `Ctrl + C` in Terminal to close the agent.

---

## Keeping the toolkit up to date

When your team adds new knowledge (personas, flows, updated design system rules), you need to pull the latest version. In Terminal:

```
cd ~/Documents/ux-ai-toolkit
git pull
```

That's the only maintenance you need to do. One command, whenever you want the latest.

---

## Common questions

**Do I need to know how to code?**
No. The only Terminal commands you need are in this guide. Copy and paste them exactly.

**What if I get an error in Terminal?**
Take a screenshot and send it to your team lead. Don't try to debug it yourself.

**Can I review a staging URL instead of a screenshot?**
Yes. Skip the screenshot step and tell the agent the URL instead:
```
Review the screen at staging.ourapp.com/appointments/confirm
```

**What if the agent flags something I disagree with?**
Findings are a starting point, not a verdict. If you made a deliberate trade-off, note it in your sync. The "Decisions made" field in the skill review is the right place to document exceptions.

**What if a component isn't in the design system yet?**
The agent will flag it as a missing component and suggest the closest existing option. Bring it to DS governance — the agent's job is to surface these gaps, not to decide them.

**How is this different from asking Claude a question normally?**
Normal Claude chat gives you general knowledge. These tools have your actual design system loaded — they know your specific components, your exact tokens, and your rules. The answers are grounded in your product, not generic best practices.

**Do my screenshots or staging URLs get stored anywhere?**
No. Everything runs locally on your laptop. Screenshots go into your local `inbox/` folder, reports go into your local `outputs/` folder. Nothing is sent to a shared server.

---

## Quick reference

| Moment | Tool | How to open |
|---|---|---|
| After kick-off — need a brief | Design Workflow Assistant | Claude chat or Cowork |
| Before weekly sync — check for blockers | Design Workflow Assistant | Claude chat or Cowork |
| Screens on staging — full audit | UX Review Agent | Terminal → `cd agents/ux-review` → `claude` |

---

## Getting help

Something broken or unclear? Reach out to your team lead before trying to fix it yourself. The toolkit is designed to be easy to use, but it's new — your feedback helps make it better for everyone.

---

*Last updated: 2026-05-28*
