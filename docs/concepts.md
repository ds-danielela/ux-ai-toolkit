# Key concepts

Five things that come up in this toolkit. Plain language only.

---

**Terminal**
A text-based way to control your Mac. Instead of clicking icons, you type short commands. Think of it as a direct line to your computer — faster for specific tasks, but unfamiliar if you've never seen it. You only need three commands to use this toolkit, and they're always written out for you.

---

**Node.js**
A tool that lets your Mac run certain programs. You install it once, it runs quietly in the background, and you never open or configure it. It's a prerequisite, not a tool you use directly.

---

**git / git pull**
Git tracks changes to files over time — like version history, but for the entire project. `git pull` means "give me the latest version of everything." Same idea as syncing a shared folder. You run it when your team lead tells you the toolkit has been updated.

---

**Skill vs agent**
Two different ways AI works in this toolkit.

A **skill** runs inside Claude chat. You describe your problem, it responds. Like texting a colleague.

An **agent** runs on your laptop. You give it a folder and a task, it works through everything autonomously, and files a report when it's done. Like sending a brief to a contractor.

---

**Design tokens**
Named values for colours, spacing, and typography shared across the product. Instead of specifying `#0F62FE` directly, a designer uses `color.interactive.primary`. If the brand colour ever changes, it updates everywhere at once — nothing breaks. When the agent flags a "token violation," it means a raw value was used instead of the named token.
