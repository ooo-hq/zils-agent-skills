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

Node.js 20 or later and Python 3.11 or later. The first start installs the Zils command line tool into a private cache.

The agent runs `zils login` and you finish sign-in in your browser. No key goes in this plugin's files, in a tool argument, or in a command.

## License

MIT. The Zils logo is a trademark of Zils; see [zils-brand](https://github.com/ooo-hq/zils-brand).
