#!/usr/bin/env python3
"""Add 'verified: false' as the last YAML frontmatter property to all markdown files in content/."""

import os
import re

CONTENT_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts/content"

def add_verified_to_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match YAML frontmatter: starts and ends with ---
    # The frontmatter must begin at the very start of the file
    pattern = re.compile(r'^(---\n)(.*?)(^---)', re.DOTALL | re.MULTILINE)
    match = pattern.match(content)

    if not match:
        print(f"  SKIP (no frontmatter): {filepath}")
        return False

    open_delim = match.group(1)
    yaml_body = match.group(2)
    close_delim = match.group(3)
    rest = content[match.end():]

    # Already has verified? Skip.
    if re.search(r'^verified:', yaml_body, re.MULTILINE):
        print(f"  SKIP (already has verified): {filepath}")
        return False

    # Ensure yaml_body ends with a newline before appending
    if not yaml_body.endswith("\n"):
        yaml_body += "\n"

    new_frontmatter = open_delim + yaml_body + "verified: false\n" + close_delim
    new_content = new_frontmatter + rest

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    updated = 0
    skipped = 0

    for root, dirs, files in os.walk(CONTENT_DIR):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                result = add_verified_to_file(filepath)
                if result:
                    updated += 1
                else:
                    skipped += 1

    print(f"\nDone. Updated: {updated} | Skipped: {skipped}")


if __name__ == "__main__":
    main()
