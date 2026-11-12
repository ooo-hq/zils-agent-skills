# Zils agent skills

Lets a coding agent train a custom [Zils](https://zils.ai) decision model on your data and call it. A decision model answers one repeated question about an input: yes or no, one of a list, or a score.

This repository holds a plugin for Claude Code and Cursor. It adds:

- **The Zils MCP server** (`npx -y @zils/cli mcp`): tools to find decision calls in your code, measure Zils on them, prepare training data, submit and follow a training run, and call the model.
- **`zils-fit` skill:** finds where a decision model fits in a repository and measures it against what you use now.
- **`zils-train` skill:** trains a model on your labeled data, with a cost limit you approve.

## Install

**Claude Code**

```sh
claude plugin marketplace add ooo-hq/zils-agent-skills
claude plugin install zils@zils
```

**Cursor:** add this repository as a plugin, or copy `mcp.json` into `.cursor/mcp.json`.

**Skills only, for any agent that reads skills** (Codex, Gemini CLI, opencode, Pi and others):

```sh
npx skills add ooo-hq/zils-agent-skills
```

This installs the two skills without the MCP server. Add the server too where the agent supports MCP.

**Any other agent:** add the MCP server by itself.

```sh
claude mcp add zils -- npx -y @zils/cli mcp      # Claude Code
codex mcp add zils -- npx -y @zils/cli mcp       # Codex
```

Other hosts: run `npx` with the arguments `-y @zils/cli mcp` over stdio.

## Use

Ask your agent:

> See where Zils fits in this repo.

> Train a Zils model on tickets.csv to pick the team for each ticket.

## Requirements and sign-in

Node.js 20 or later and Python 3.11 or later.

The agent runs `zils login` and you finish sign-in in your browser. No key goes in this plugin's files, in a tool argument, or in a command.

## What this plugin runs and where your data goes

- **What it runs.** The plugin starts one local program: `npx -y @zils/cli@0.4.21 mcp`. That downloads the `@zils/cli` package, pinned to that exact version, from the npm registry. On first start the package installs the Zils Python client and its dependencies from PyPI into a private cache. It does not change your system Python.
- **What stays on your machine.** Scanning your code for decision calls and preparing training files happen locally.
- **What is sent to Zils.** When you sign in, call a model, measure Zils on your examples, or submit a training run, the inputs, answers and training files involved are sent to the Zils service at `training.zils.ai`. Every training submission carries a cost limit you approve.
- **Nowhere else.** The MCP server and the skills send your data to no other service.

How Zils handles the data it receives: [zils.ai/privacy](https://zils.ai/privacy). Terms: [zils.ai/terms](https://zils.ai/terms). Help: [docs.zils.ai](https://docs.zils.ai) or [zils.ai/contact](https://zils.ai/contact).

## License

MIT. The Zils logo is a trademark of Zils; see [zils-brand](https://github.com/ooo-hq/zils-brand).
