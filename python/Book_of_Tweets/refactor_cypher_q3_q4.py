#!/usr/bin/env python3
"""
Refactor Q3+Q4 Cypher queries in Book_of_Tweets/THOUGHTS markdown files.

Converts the old MATCH/MATCH/MERGE format to the new ON CREATE SET format
used in content/THOUGHTS (as applied in the 2026-03-16 and 2026-03-18 operations):

OLD Q3+Q4:
    MATCH (t:THOUGHT {name: "thought.XXXXX"})
    MATCH (c:CONTENT {name: "content.XXXXX"})
    MERGE (t)-[:HAS_CONTENT { "name": "edge.XXXXX" }]->(c);

    MATCH (parent:TOPIC {name: "topic.YYYYY"})
    MATCH (child:THOUGHT {name: "thought.XXXXX"})
    MERGE (parent)-[:HAS_THOUGHT { "name": "YYYYY->XXXXX" }]->(child);

NEW Q3+Q4:
    MERGE (t)-[r:HAS_CONTENT]->(c)
    ON CREATE SET r.name = "t.edge.XXXXX"
    // 3. Pass 't' forward, find the Parent Topic, and link them
    WITH t
    MATCH (parent:TOPIC {name: "topic.YYYYY"})
    MERGE (parent)-[r2:HAS_THOUGHT]->(t)
    ON CREATE SET r2.name = "t.edge.YYYYY->XXXXX"
    RETURN t, parent;

Also corrects:
- r.name prefix: "edge." -> "t.edge."
- r2.name prefix: must be "t.edge." (not missing or bare)
- r2.name hyphens: "DIVINE-SOVEREIGNTY" -> "DIVINE SOVEREIGNTY"
"""

import os
import re

THOUGHTS_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts/Book_of_Tweets/THOUGHTS"


def get_frontmatter_value(fm_block, key):
    """Extract a value from YAML frontmatter, stripping quotes."""
    m = re.search(rf'^{key}:\s*"([^"]+)"', fm_block, re.MULTILINE)
    if not m:
        m = re.search(rf"^{key}:\s*'([^']+)'", fm_block, re.MULTILINE)
    if not m:
        m = re.search(rf'^{key}:\s*(.+)', fm_block, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return None


def build_new_q3_q4(thought_part, parent_part):
    """Build the new Q3+Q4 block."""
    return (
        f'MERGE (t)-[r:HAS_CONTENT]->(c)\n'
        f'ON CREATE SET r.name = "t.edge.{thought_part}"\n'
        f'// 3. Pass \'t\' forward, find the Parent Topic, and link them\n'
        f'WITH t\n'
        f'MATCH (parent:TOPIC {{name: "topic.{parent_part}"}})\n'
        f'MERGE (parent)-[r2:HAS_THOUGHT]->(t)\n'
        f'ON CREATE SET r2.name = "t.edge.{parent_part}->{thought_part}"\n'
        f'RETURN t, parent;'
    )


def refactor_file(fpath):
    """Refactor Q3+Q4 in a single file. Returns (changed, description)."""
    text = open(fpath).read()

    # Get frontmatter
    fm_m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not fm_m:
        return False, "no frontmatter"
    fm = fm_m.group(1)

    # Get thought name and parent from frontmatter (source of truth)
    thought_name = get_frontmatter_value(fm, 'name')   # e.g. "thought.ACCOUNTABILITY"
    parent_name  = get_frontmatter_value(fm, 'parent') # e.g. "topic.MORALITY"
    if not thought_name or not parent_name:
        return False, "missing name or parent in frontmatter"
    if not thought_name.startswith('thought.'):
        return False, f"unexpected name format: {thought_name}"
    if not parent_name.startswith('topic.'):
        return False, f"unexpected parent format: {parent_name}"

    thought_part = thought_name[len('thought.'):].upper()
    # Normalize hyphens to spaces in parent part
    parent_part  = parent_name[len('topic.'):].upper().replace('-', ' ')

    # Extract cypher block
    cypher_m = re.search(r'(```[Cc]ypher\s*)(.*?)(```)', text, re.DOTALL)
    if not cypher_m:
        return False, "no cypher block"
    block = cypher_m.group(2)

    # Detect format: if already using ON CREATE SET, skip
    if 'ON CREATE SET' in block:
        # Already converted — but still check r2.name correctness
        expected_r2 = f't.edge.{parent_part}->{thought_part}'
        r2_m = re.search(r'ON CREATE SET r2\.name\s*=\s*"([^"]*)"', block)
        if r2_m and r2_m.group(1) != expected_r2:
            new_block = block.replace(
                f'ON CREATE SET r2.name = "{r2_m.group(1)}"',
                f'ON CREATE SET r2.name = "{expected_r2}"'
            )
            new_text = text[:cypher_m.start(2)] + new_block + text[cypher_m.end(2):]
            open(fpath, 'w').write(new_text)
            return True, f"r2.name corrected: {r2_m.group(1)!r} → {expected_r2!r}"
        return False, "already in new format"

    # Build new Q3+Q4 block
    new_q3_q4 = build_new_q3_q4(thought_part, parent_part)

    # Pattern: match the old Q3+Q4 block
    # Q3: MATCH (t:...) \n MATCH (c:...) \n MERGE ...->(c); with optional blank line before Q4
    # Q4: MATCH (parent:...) \n MATCH (child:...) \n MERGE ...;
    old_q3_q4_pattern = re.compile(
        r'MATCH\s*\(t:THOUGHT\s*\{[^}]+\}\)\s*\n'
        r'MATCH\s*\(c:CONTENT\s*\{[^}]+\}\)\s*\n'
        r'MERGE\s*\(t\)-\[:HAS_CONTENT[^\]]*\]->\(c\);?\s*\n'
        r'(?:\s*\n)?'
        r'MATCH\s*\(parent:TOPIC\s*\{[^}]+\}\)\s*\n'
        r'MATCH\s*\(child:THOUGHT\s*\{[^}]+\}\)\s*\n'
        r'MERGE\s*\(parent\)-\[:HAS_THOUGHT[^\]]*\]->\(child\);?',
        re.DOTALL
    )

    m = old_q3_q4_pattern.search(block)
    if not m:
        return False, "old Q3+Q4 pattern not matched"

    new_block = block[:m.start()] + new_q3_q4 + block[m.end():]
    new_text = text[:cypher_m.start(2)] + new_block + text[cypher_m.end(2):]
    open(fpath, 'w').write(new_text)
    return True, f"converted → t.edge.{parent_part}->{thought_part}"


def main():
    files = sorted(
        f for f in os.listdir(THOUGHTS_DIR)
        if f.endswith('.md') and os.path.isfile(os.path.join(THOUGHTS_DIR, f))
    )

    converted = []
    r2_only = []
    skipped = []
    already_done = []

    for fname in files:
        fpath = os.path.join(THOUGHTS_DIR, fname)
        changed, desc = refactor_file(fpath)
        if changed:
            if 'r2.name corrected' in desc:
                r2_only.append((fname, desc))
            else:
                converted.append((fname, desc))
        elif 'already in new format' in desc:
            already_done.append(fname)
        else:
            skipped.append((fname, desc))

    print(f"Files checked:       {len(files)}")
    print(f"Converted Q3+Q4:     {len(converted)}")
    print(f"r2.name only fixed:  {len(r2_only)}")
    print(f"Already new format:  {len(already_done)}")
    print(f"Skipped:             {len(skipped)}")

    if skipped:
        print("\n=== SKIPPED ===")
        for fname, reason in skipped:
            print(f"  {fname}: {reason}")

    if r2_only:
        print("\n=== r2.name CORRECTIONS ===")
        for fname, desc in r2_only:
            print(f"  {fname}: {desc}")


if __name__ == '__main__':
    main()
