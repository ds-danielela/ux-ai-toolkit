# Getting Started

How to set up the toolkit on your machine. Takes about 10 minutes.

---

## For designers

You need two things: Claude Code (to run the agent) and a copy of this repo.

### 1. Install Claude Code

Open Terminal (`Cmd + Space`, type "Terminal", press Enter) and run:

```bash
npm install -g @anthropic/claude-code
```

If you see a "command not found: npm" error, you need to install Node.js first.
Download it from [nodejs.org](https://nodejs.org) — click the LTS version and follow the installer.

### 2. Clone the repo

```bash
git clone https://github.com/ds-danielela/ux-ai-toolkit.git ~/Documents/ux-ai-toolkit
```

This downloads everything to your Documents folder. You only do this once.

### 3. Install the skill in Cowork

Open Cowork or Claude chat. The Design Workflow Skill activates automatically when you describe a NEED or ask for a DS review — nothing to install.

### 4. Run your first review

```bash
cd ~/Documents/ux-ai-toolkit/agents/ux-review
claude
```

Drop a screenshot in the `inbox/` folder, then tell the agent:

```
There's a new screen in inbox/. Run a ux-review.
```

That's it. Reports appear in `outputs/`.

---

## Keeping the toolkit up to date

When the knowledge base or tools are updated, pull the latest version:

```bash
cd ~/Documents/ux-ai-toolkit
git pull
```

Run this once a week or whenever your team lead announces an update.

---

## For team leads

### Adding or updating design system knowledge

All shared knowledge lives in `shared/design-system/`. To update it:

1. Create a branch: `git checkout -b update/[what-youre-changing]`
2. Edit the relevant file
3. Open a pull request on GitHub
4. The team lead reviews and merges
5. Everyone pulls the update with `git pull`

### Adding a new agent

1. Create `agents/your-agent-name/` at the repo root
2. Add a `CLAUDE.md` and `agent-config/` folder inside it
3. Reference `../../shared/` for design system knowledge
4. Add its `inbox/`, `outputs/`, `archive/` to `.gitignore`
5. Update this docs site with a new page under `docs/tools/`

### Adding a new skill

1. Create `skills/your-skill-name/SKILL.md`
2. Follow the format of the existing skill
3. Update `docs/_sidebar.md` to add it to the navigation

---

## Troubleshooting

**"command not found: claude"**
Claude Code isn't installed. Run `npm install -g @anthropic/claude-code` again.

**"Permission denied" error**
You may need to prefix with `sudo`: `sudo npm install -g @anthropic/claude-code`

**The agent doesn't find my screenshot**
Make sure the file is in `agents/ux-review/inbox/` — not a subfolder inside it.

**Something else is broken**
Take a screenshot of the error and send it to your team lead.
