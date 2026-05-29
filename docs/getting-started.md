# Getting Started

Two tools, two different setups. Start with whichever one you need first.

---

## Tool 1 — Design Workflow Skill

**No setup needed.** The skill runs inside Claude chat or Cowork.

Open Claude (or Cowork) and describe what you're working on. The skill activates automatically when you mention a NEED, a design brief, or a screen review. Nothing to install.

→ [Learn how to use it](tools/design-workflow-skill.md)

---

## Tool 2 — UX Review Agent

The agent runs on your laptop and needs a one-time setup. It takes about 10 minutes. You don't need to know how to code.

### What you need before you start

- A Mac
- An Anthropic account with Claude access
- About 10 minutes

---

### Step 1 — Install Node.js

Node.js is a behind-the-scenes tool that lets your computer run the agent. You install it once and never think about it again.

Download it from [nodejs.org](https://nodejs.org), click the **LTS** version, and follow the installer.

---

### Step 2 — Install Claude Code

Claude Code connects the agent to Claude's AI. Open Terminal (`Cmd + Space`, type "Terminal", press Enter) and paste:

```bash
npm install -g @anthropic/claude-code
```

Press Enter and wait. A lot of text will scroll by — that's normal. When it's done, check it worked:

```bash
claude --version
```

If you see a version number, you're set. If you see an error, try: `sudo npm install -g @anthropic/claude-code`

---

### Step 3 — Download the toolkit

This puts a copy of the toolkit on your computer. You only do this once.

```bash
git clone https://github.com/ds-danielela/ux-ai-toolkit.git ~/Documents/ux-ai-toolkit
```

This creates an `ux-ai-toolkit` folder in your Documents. Everything lives there.

---

### Step 4 — Run your first review

```bash
cd ~/Documents/ux-ai-toolkit/agents/ux-review
claude
```

The agent will start up. Drop a screenshot of any screen into the `ux-ai-toolkit/agents/ux-review/inbox/` folder, then tell the agent:

```
There's a new screen in inbox/. Run a ux-review.
```

Your report will appear in the `outputs/` folder inside the same directory.

→ [Full guide to using the agent](tools/ux-review-agent.md)

---

## Keeping your toolkit up to date

When the design system or tools are updated, your team lead will let you know. To update your copy, open Terminal and run:

```bash
cd ~/Documents/ux-ai-toolkit
git pull
```

That's it.

---

## Something not working?

**"command not found: npm"** — Node.js isn't installed yet. Go back to Step 1.

**"command not found: claude"** — Claude Code didn't install. Repeat Step 2.

**"Permission denied"** — Add `sudo` before the command that failed.

**The agent can't find your screenshot** — Make sure the file is directly inside `inbox/`, not in a subfolder.

**Anything else** — Screenshot the error and send it to your team lead.
