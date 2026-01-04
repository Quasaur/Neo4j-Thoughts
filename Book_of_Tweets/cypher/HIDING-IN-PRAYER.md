---
name: "thought.HIDING IN PRAYER"
alias: "Thought: Hiding In Prayer"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- prayer
- world
- hiding
- spirituality
- presence
level: 2
neo4j: true
insert: true
---
# Hiding In Prayer

> [!Thought-en]
> Prayer is where I hide from the world.

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013e)
CREATE (t:THOUGHT {
    name: "thought.HIDING IN PRAYER",
    alias: "Thought: Hiding In Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'world', 'hiding', 'spirituality', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HIDING IN PRAYER",
    en_title: "Hiding In Prayer",
    en_content: "Prayer is where I hide from the world.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HIDING IN PRAYER" AND c.name = "content.HIDING IN PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HIDING IN PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HIDING IN PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HIDING IN PRAYER" }]->(child);
```