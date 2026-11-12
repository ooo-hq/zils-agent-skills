---
name: zils-train
description: Train a custom Zils decision model on the user's own labeled data and call it. Use when the user wants a model that answers one repeated question (yes/no, one of a list, or a score) from their data, or asks to train, fine-tune or replace an LLM classifier with Zils.
---

# Train a Zils decision model

A Zils model answers one repeated question about an input: yes or no, one of
a list, or a score. Training needs rows where the input and the right answer
are both known.

1. Read the training guide and follow it step by step. It is the current
   walkthrough: signing in, preparing the file, checking it, the cost limit,
   submitting, and calling the finished model.
   - If the `zils` MCP server is connected, call its `train_guide` tool.
   - If it is not, run `npx -y @zils/cli@0.4.21 train guide` in a shell. It
     prints the same guide and says which `zils` command stands in for each
     tool. It needs no login and sends nothing.
2. Ask the user before anything that spends money or sends their data. Every
   submission takes a cost limit; state it to the user first.
3. Never put a key in a tool argument or a command. Sign-in is `zils login`,
   which the user completes in their browser.
4. When the run finishes, show the user its test result and the code that
   calls the model.

If the user has no labeled data yet, or wants to know where a decision model
would fit in their code, use the `zils-fit` skill first.
