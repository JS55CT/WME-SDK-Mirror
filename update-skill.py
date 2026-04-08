"""
update-skill.py
===============
Pulls the latest WME SDK skill from the Claude Code skills directory.

This script copies the SKILL.md file from ~/.claude/skills/wme-sdk into the
local skills/ folder, keeping it in sync with the main SDK documentation updates.

Path Substitution:
  Automatically converts hardcoded absolute paths to relative paths so that
  the skill works for anyone who clones or forks the repository.
  - Original: c:/Users/Jstrand/OneDrive - FactSet/Personal/waze stuff/WAZE SDK Mirror/WME SDK/web-assets.waze.com/wme_sdk_docs/production/latest/NotebookLM/
  - Replaced: ../NotebookLM/

Usage:
  py update-skill.py
  py update-skill.py --skill-path /custom/path/to/skill

Output:
  - skills/SKILL.md -- Copy of the WME SDK skill with paths adjusted for repo
  - Prints status (updated, already current, or error)
"""

import os
import re
import argparse
from pathlib import Path

DEFAULT_SKILL_SOURCE = os.path.expanduser("~/.claude/skills/wme-sdk/SKILL.md")

# Hardcoded path to replace with relative path
HARDCODED_PATH = "c:/Users/Jstrand/OneDrive - FactSet/Personal/waze stuff/WAZE SDK Mirror/WME SDK/web-assets.waze.com/wme_sdk_docs/production/latest/NotebookLM/"
RELATIVE_PATH = "../NotebookLM/"


def get_skill_path(custom_path=None):
    """Resolve the skill source path."""
    if custom_path:
        return custom_path
    return DEFAULT_SKILL_SOURCE


def main():
    parser = argparse.ArgumentParser(
        description="Pull latest WME SDK skill from Claude Code skills directory"
    )
    parser.add_argument(
        "--skill-path",
        default=None,
        help=f"Custom path to the skill file (default: {DEFAULT_SKILL_SOURCE})"
    )
    args = parser.parse_args()

    skill_source = get_skill_path(args.skill_path)
    skill_dest = os.path.join(os.getcwd(), "skills", "SKILL.md")

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(skill_dest), exist_ok=True)

    # Check if source exists
    if not os.path.isfile(skill_source):
        print(f"[ERROR] Skill source not found: {skill_source}")
        print(f"        Is the wme-sdk skill installed in ~/.claude/skills/?")
        return 1

    # Copy the skill
    try:
        # Read source to check if update is needed
        with open(skill_source, 'r', encoding='utf-8') as f:
            source_content = f.read()

        # Replace hardcoded path with relative path for repo portability
        # Handle both forward slashes (from file) and backslashes (Windows paths)
        modified_content = source_content.replace(
            HARDCODED_PATH.replace('/', '\\'),
            RELATIVE_PATH
        )
        modified_content = modified_content.replace(
            HARDCODED_PATH,
            RELATIVE_PATH
        )

        # Check if destination exists and has same content
        if os.path.isfile(skill_dest):
            with open(skill_dest, 'r', encoding='utf-8') as f:
                dest_content = f.read()
            if modified_content == dest_content:
                print("[OK] Skill is current: skills/SKILL.md")
                return 0

        # Write updated skill with path substitution
        with open(skill_dest, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        print("[UPDATED] Skill copied and paths adjusted for repo portability")
        print(f"          Destination: skills/SKILL.md")
        print(f"          Path change: hardcoded -> ../NotebookLM/")
        return 0

    except Exception as e:
        print(f"[ERROR] Failed to update skill: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
