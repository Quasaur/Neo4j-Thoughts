#!/usr/bin/env python3
"""Sync selected THOUGHT markdown files from AuraDB back into local content files.

This script:
- scans `content/THOUGHTS` for files whose YAML `parent` matches a target topic
- queries AuraDB for the THOUGHT node and its HAS_CONTENT child CONTENT node
- only updates files whose AuraDB CONTENT `en_title` begins with "Thought:"
- sets local YAML `verified: true`
- updates YAML frontmatter values from the AuraDB THOUGHT and CONTENT nodes
- rewrites the THOUGHT and CONTENT CREATE blocks in the local Cypher block
"""

from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from pathlib import Path

import yaml
from neo4j import GraphDatabase


URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

REPO_ROOT = Path(__file__).resolve().parents[2]
THOUGHTS_DIR = REPO_ROOT / "content" / "THOUGHTS"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
THOUGHT_CREATE_RE = re.compile(r"CREATE\s*\(t:THOUGHT\s*\{.*?\}\);", re.DOTALL)
CONTENT_CREATE_RE = re.compile(r"CREATE\s*\(c:CONTENT\s*\{.*?\}\);", re.DOTALL)

CONTENT_FIELDS = [
    "en_title",
    "en_content",
    "es_title",
    "es_content",
    "fr_title",
    "fr_content",
    "hi_title",
    "hi_content",
    "zh_title",
    "zh_content",
]


def yaml_literal(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    return json.dumps(str(value), ensure_ascii=False)


def cypher_literal(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        rendered = ", ".join(cypher_literal(item) for item in value)
        return f"[{rendered}]"
    return json.dumps(str(value), ensure_ascii=False)


def load_frontmatter(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    if not match:
        raise ValueError(f"No YAML frontmatter found in {file_path}")
    data = yaml.safe_load(match.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Frontmatter is not a mapping in {file_path}")
    return content, data


def derive_ptopic(parent_name: str) -> str:
    return f"[[topic-{parent_name.removeprefix('topic.')}]]"


def build_frontmatter(local_yaml, thought_props, content_props):
    frontmatter = OrderedDict()
    frontmatter["type"] = local_yaml.get("type", "THOUGHT")
    frontmatter["name"] = thought_props["name"]
    frontmatter["alias"] = thought_props["alias"]
    frontmatter["parent"] = thought_props["parent"]

    for field in CONTENT_FIELDS:
        db_value = content_props.get(field, "")
        if db_value != "" or field in local_yaml:
            frontmatter[field] = db_value

    frontmatter["tags"] = thought_props.get("tags", [])
    frontmatter["ptopic"] = derive_ptopic(thought_props["parent"])
    frontmatter["level"] = thought_props["level"]
    frontmatter["neo4j"] = local_yaml.get("neo4j", True)
    frontmatter["verified"] = True

    reserved = set(frontmatter.keys())
    for key, value in local_yaml.items():
        if key not in reserved:
            frontmatter[key] = value

    lines = ["---"]
    for key, value in frontmatter.items():
        lines.append(f"{key}: {yaml_literal(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def render_thought_create(thought_props):
    lines = [
        "CREATE (t:THOUGHT {",
        f"    name: {cypher_literal(thought_props['name'])},",
        f"    alias: {cypher_literal(thought_props['alias'])},",
        f"    parent: {cypher_literal(thought_props['parent'])},",
        f"    tags: {cypher_literal(thought_props.get('tags', []))},",
        f"    level: {cypher_literal(thought_props['level'])}",
        "});",
    ]
    return "\n".join(lines)


def render_content_create(content_props):
    ordered_fields = ["name", "ctype", *CONTENT_FIELDS]
    lines = ["CREATE (c:CONTENT {"]
    for index, key in enumerate(ordered_fields):
        suffix = "," if index < len(ordered_fields) - 1 else ""
        lines.append(f"    {key}: {cypher_literal(content_props.get(key, ''))}{suffix}")
    lines.append("});")
    return "\n".join(lines)


def rewrite_body(body, thought_props, content_props):
    thought_name_suffix = thought_props["name"].removeprefix("thought.")
    parent_suffix = thought_props["parent"].removeprefix("topic.")

    new_body = THOUGHT_CREATE_RE.sub(render_thought_create(thought_props), body, count=1)
    new_body = CONTENT_CREATE_RE.sub(render_content_create(content_props), new_body, count=1)
    new_body = re.sub(
        r'ON CREATE SET r\.name = ".*?"',
        f'ON CREATE SET r.name = "t.edge.{thought_name_suffix}"',
        new_body,
        count=1,
    )
    new_body = re.sub(
        r'MATCH \(parent:TOPIC \{name: ".*?"\}\)',
        f'MATCH (parent:TOPIC {{name: "{thought_props["parent"]}"}})',
        new_body,
        count=1,
    )
    new_body = re.sub(
        r'ON CREATE SET r2\.name = ".*?"',
        f'ON CREATE SET r2.name = "t.edge.{parent_suffix}->{thought_name_suffix}"',
        new_body,
        count=1,
    )
    return new_body


def fetch_auradb_record(session, thought_name):
    record = session.run(
        """
        MATCH (t:THOUGHT {name: $thought_name})-[:HAS_CONTENT]->(c:CONTENT)
        RETURN properties(t) AS thought, properties(c) AS content
        """,
        thought_name=thought_name,
    ).single()
    if not record:
        return None
    return record["thought"], record["content"]


def update_file(file_path: Path, thought_props, content_props, apply_changes: bool):
    original_content, local_yaml = load_frontmatter(file_path)
    frontmatter_match = FRONTMATTER_RE.match(original_content)
    assert frontmatter_match is not None
    body = original_content[frontmatter_match.end() :]

    new_frontmatter = build_frontmatter(local_yaml, thought_props, content_props)
    new_body = rewrite_body(body, thought_props, content_props)
    new_content = new_frontmatter + new_body.lstrip("\n")

    changed = new_content != original_content
    if changed and apply_changes:
        file_path.write_text(new_content, encoding="utf-8")
    return changed


def main():
    parser = argparse.ArgumentParser(
        description="Sync qualifying THOUGHT markdown files from AuraDB into local files."
    )
    parser.add_argument("--parent", default="topic.ATTITUDE", help="YAML parent filter")
    parser.add_argument("--apply", action="store_true", help="Write changes to disk")
    args = parser.parse_args()

    matched_files = []
    updated_files = []
    skipped_files = []

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            for file_path in sorted(THOUGHTS_DIR.glob("thought-*.md")):
                try:
                    _, local_yaml = load_frontmatter(file_path)
                except ValueError as exc:
                    skipped_files.append(f"{file_path.name}: {exc}")
                    continue

                if local_yaml.get("parent") != args.parent:
                    continue

                thought_name = local_yaml.get("name")
                if not thought_name:
                    skipped_files.append(f"{file_path.name}: missing YAML name")
                    continue

                record = fetch_auradb_record(session, thought_name)
                if not record:
                    skipped_files.append(f"{file_path.name}: AuraDB THOUGHT/CONTENT not found")
                    continue

                thought_props, content_props = record
                en_title = content_props.get("en_title", "")
                if not isinstance(en_title, str) or not en_title.startswith("Thought:"):
                    skipped_files.append(f"{file_path.name}: AuraDB en_title did not start with 'Thought:'")
                    continue

                matched_files.append(file_path.name)
                changed = update_file(file_path, thought_props, content_props, args.apply)
                if changed:
                    updated_files.append(file_path.name)

    mode_label = "APPLY" if args.apply else "DRY RUN"
    print(f"[{mode_label}] Qualified files: {len(matched_files)}")
    for name in matched_files:
        marker = "updated" if name in updated_files else "no-op"
        print(f"  - {name} ({marker})")

    print(f"\n[{mode_label}] Skipped: {len(skipped_files)}")
    for item in skipped_files:
        print(f"  - {item}")

    print(f"\n[{mode_label}] Files changed: {len(updated_files)}")


if __name__ == "__main__":
    main()
