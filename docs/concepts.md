# Key concepts

Things that come up in this toolkit. Plain language only.

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

---

**Context**
Everything Claude reads before it responds to you. In this toolkit, context loads in a fixed order: the project file (CLAUDE.md) first, then memory from past sessions, then your prompt. The more precise those first two are, the less you need to explain each time. If Claude gives a generic answer, it usually means the context is thin — add more to CLAUDE.md or memory.

---

**Memory**
Notes Claude keeps between sessions. Unlike a normal chat that forgets everything when you close it, memory persists. It stores decisions you've made, preferences, and open threads. You can ask Claude to update its memory at any time. If it starts acting on something outdated, tell it to forget — it will update the record.

---

**Plan mode**
A way to ask Claude to think before it acts. Instead of starting work immediately, Claude lays out its approach first — what it will do, in what order, and what assumptions it's making. You review the plan, correct anything wrong, then give it the go-ahead. Useful for any task with more than two steps. Saves time compared to fixing wrong work after the fact.

---

**MCP (Model Context Protocol)**
A way to connect Claude directly to external tools — like Figma — so it can read your actual screens instead of relying on a description. With a Figma MCP connected, Claude can inspect your layers, check component names, and catch spec mismatches directly. Without it, it works from screenshots or what you describe. Layer names in Figma must match the design system exactly for the connection to work reliably.
