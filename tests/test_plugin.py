"""Checks that every manifest in this repository describes the same plugin."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = {"command": "npx", "args": ["-y", "@zils/cli", "mcp"]}  # what `claude mcp add zils` runs


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def frontmatter(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    assert match, f"{path} has no frontmatter"
    return dict(line.split(": ", 1) for line in match.group(1).splitlines())


class ManifestTests(unittest.TestCase):
    def test_claude_and_cursor_manifests_name_the_same_plugin(self):
        claude, cursor = load(".claude-plugin/plugin.json"), load(".cursor-plugin/plugin.json")
        for field in ("name", "version", "description", "license", "homepage", "repository"):
            self.assertEqual(claude[field], cursor[field], field)
        self.assertEqual(claude["name"], "zils")
        self.assertEqual(claude["license"], "MIT")
        self.assertTrue((ROOT / "LICENSE").read_text(encoding="utf-8").startswith("MIT License"))

    def test_the_marketplace_lists_this_repository_as_the_plugin(self):
        market, plugin = load(".claude-plugin/marketplace.json"), load(".claude-plugin/plugin.json")
        (entry,) = market["plugins"]
        self.assertEqual(entry, {"name": plugin["name"], "source": "./"})

    def test_both_agents_start_the_published_mcp_server(self):
        # Claude Code reads .mcp.json, Cursor reads mcp.json.
        for path in (".mcp.json", "mcp.json"):
            self.assertEqual(load(path), {"mcpServers": {"zils": RUN}}, path)

    def test_no_file_asks_for_or_holds_a_key(self):
        # Sign-in is `zils login`; nothing here may carry or request a credential.
        for path in (".mcp.json", "mcp.json", ".claude-plugin/plugin.json", ".cursor-plugin/plugin.json"):
            text = (ROOT / path).read_text(encoding="utf-8")
            self.assertIsNone(re.search(r"env|userConfig|variables|zils_sk_|token", text), path)

    def test_the_logo_both_manifests_name_is_in_the_repository(self):
        claude, cursor = load(".claude-plugin/plugin.json"), load(".cursor-plugin/plugin.json")
        self.assertEqual(claude["icon"], "./assets/zils-icon.png")
        self.assertEqual(cursor["logo"], "assets/zils-icon.png")
        self.assertTrue((ROOT / "assets/zils-icon.png").is_file())


class SkillTests(unittest.TestCase):
    def test_each_skill_folder_matches_its_name_and_says_when_to_use_it(self):
        folders = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
        self.assertEqual(folders, ["zils-fit", "zils-train"])
        for folder in folders:
            meta = frontmatter(f"skills/{folder}/SKILL.md")
            self.assertEqual(meta["name"], folder)
            self.assertGreater(len(meta["description"]), 60, folder)

    def test_the_training_skill_sends_the_agent_to_the_servers_own_guide(self):
        # The steps live in the MCP server (train_guide), so they cannot go stale here.
        text = (ROOT / "skills/zils-train/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("train_guide", text)
        self.assertLess(len(text.splitlines()), 40)


if __name__ == "__main__":
    unittest.main()
