# Workspace Rules and Directives

## Neo4j-Thoughts & wisdom-book Workspaces

This document contains critical rules and conventions that must be followed at all times when working in these workspaces.

---

## AI Assistant Tools

### Git Operations
- **USE**: VSCode native Source Control & GitLens extension
- **METHOD**: Run git commands via `run_in_terminal` tool
- **DO NOT USE**: GitKraken MCP tools

---

## Neo4j Hierarchy & Level Rules

### Level Assignment
- **Subtopics**: parent level + 1
- **Children (THOUGHT, QUOTE, PASSAGE)**: same level as parent topic

**Example:**
- topic.PSYCHOLOGY is level 4
- Its subtopics would be level 5
- Its THOUGHT/QUOTE/PASSAGE children are level 4

### Node Types
- `TOPIC`: Organizational categories
- `THOUGHT`: Individual thoughts
- `QUOTE`: Quotations
- `PASSAGE`: Biblical or other passages
- `DESCRIPTION`: Description node containing multilingual text for TOPIC nodes.
- `CONTENT`: Content node containing multilingual text for THOUGHT, QUOTE & PASSAGE nodes.

### Relationships
- `HAS_THOUGHT`: TOPIC → THOUGHT
- `HAS_QUOTE`: TOPIC → QUOTE
- `HAS_PASSAGE`: TOPIC → PASSAGE
- `HAS_DESCRIPTION`: TOPIC → DESCRIPTION
- `HAS_CONTENT`: THOUGHT/QUOTE/PASSAGE → CONTENT
- `HAS_TOPIC`: TOPIC → TOPIC (parent to subtopic)

**NEVER use:**
- `FITS_WITHIN`
- `TAGGED_WITH`
- Any other relationship types not listed above

---

## Obsidian-Cypher Format

### Required YAML Frontmatter Properties
```yaml
name: "thought.NAME WITH SPACES"
alias: "<NODE>: Display Name"
type: THOUGHT|QUOTE|PASSAGE|TOPIC
parent: "topic.PARENT NAME" o topic.PARENTNAME [has a single-word parent]
tags:
  - tag1
  - tag2
  - tag3
  - tag4
  - tag5
neo4j: true
ptopic: "[[topic-PARENT NAME]]"
level: N
inserted: true
```

**IMPORTANT**: All YAML `name` & `alias` values will be encased in quotes ("").

### Properties to EXCLUDE
- `draft` - Delete this
- `mling` - Delete this
- `aliases` - Use `alias` (singular) instead
- `title` - Use `alias` instead

### Cypher Block Structure

All Obsidian-Cypher files must have an embedded Cypher block with:

1. **CREATE TOPIC/THOUGHT/QUOTE/PASSAGE node**
2. **CREATE DESCRIPTION node for TOPIC | CONTENT node for THOUGHT/QUOTE/PASSAGE nodes**
3. **MERGE HAS_DESCRIPTION relationship for TOPIC | HAS_CONTENT relationship for THOUGHT/QUOTE/PASSAGE**
4. **MERGE HAS_THOUGHT/QUOTE/PASSAGE relationship** (parent TOPIC→ child)

**Example:**
```cypher
CREATE (t:THOUGHT {
    name: "thought.EXAMPLE",
    alias: "Thought: EXAMPLE",
    parent: "topic.PARENT",
    tags: ["tag1", "tag2"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EXAMPLE",
    en_title: "EXAMPLE",
    en_content: "English content...",
    es_title: "EJEMPLO",
    es_content: "Contenido en español...",
    fr_title: "EXEMPLE",
    fr_content: "Contenu en français...",
    hi_title: "उदाहरण",
    hi_content: "हिंदी सामग्री...",
    zh_title: "例子",
    zh_content: "中文内容..."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EXAMPLE" AND c.name = "content.EXAMPLE"
MERGE (t)-[:HAS_CONTENT {name: "edge.EXAMPLE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PARENT" AND child.name = "thought.EXAMPLE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PARENT->EXAMPLE"}]->(child);
```

### Naming Conventions
- Node names use underscores: `thought.692_189`
- File names use hyphens: `692-189.md`
- Content titles vary (check existing database for consistency)

### Multilingual Content Rules
- **zh_title**: Must use Chinese Pinyin (NOT Chinese Simplified characters), maximum 4 words
- **zh_content**: Must use Chinese Pinyin (NOT Chinese Simplified characters)
- All other language fields follow standard conventions for their respective languages

---

## Git Workflow

### Use Terminal Commands ONLY
```bash
git status
git add -A
git commit -m "message"
git push
```

### DO NOT Use
- GitKraken MCP tools
- Any GUI git commands

---

## File Organization

### Directory Structure
```
content/
  THOUGHTS/         # Inserted thoughts (with embedded Cypher)
  THOUGHTS/UnInserted/  # Not yet inserted (may have embedded Cypher)
  TOPICS/           # All in Obsidian-Cypher format
  QUOTES/
  PASSAGES/
  BIBLE/
```

### Insertion Status
- **Inserted**: File has embedded Cypher block AND `inserted: true` in frontmatter
- **Not Inserted**: File may have embedded Cypher but not yet run against database
- Files in `UnInserted/` should NOT be moved to main folder until actually inserted into Neo4j AuraDB

---

## Neo4j AuraDB Connection

```python
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")
```

### Before Creating Cypher Blocks
1. Query the actual database to get existing node structure
2. Match naming conventions exactly (underscores vs hyphens)
3. Verify level against parent topic
4. Check content format in existing nodes

---

## Critical Reminders

1. **Always check existing Obsidian-Cypher files** for format reference before creating new ones
2. **Query Neo4j database** to verify existing node structure before modifications
3. **Level inheritance**: Children inherit parent's level, subtopics are parent + 1
4. **Use terminal git commands**, never GitKraken tools
5. **Don't move files to main THOUGHTS folder** until they're actually inserted into Neo4j

---

## Document Version
Last Updated: January 10, 2026
