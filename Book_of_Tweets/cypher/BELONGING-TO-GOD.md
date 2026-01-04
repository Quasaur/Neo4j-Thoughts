---
name: "thought.BELONGING TO GOD"
alias: "Thought: Belonging To God"
type: THOUGHT
parent: "topic.HUMANITY"
tags:
- belonging
- identity
- choice
- life
- god
level: 3
neo4j: true
insert: true
---
# Belonging To God

> [!Thought-en]
> If we don't belong to God, we belong to ourselves...and shall perish in ourselves because we choose not to live in God.

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-May-2011)
CREATE (t:THOUGHT {
    name: "thought.BELONGING TO GOD",
    alias: "Thought: Belonging To God",
    parent: "topic.HUMANITY",
    tags: ['belonging', 'identity', 'choice', 'life', 'god'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BELONGING TO GOD",
    en_title: "Belonging To God",
    en_content: "If we don't belong to God, we belong to ourselves...and shall perish in ourselves because we choose not to live in God.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BELONGING TO GOD" AND c.name = "content.BELONGING TO GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BELONGING TO GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.BELONGING TO GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >BELONGING TO GOD" }]->(child);
```