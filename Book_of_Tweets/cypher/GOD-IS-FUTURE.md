---
name: "thought.GOD IS FUTURE"
alias: "Thought: God Is Future"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- future
- god
- spirituality
- eternity
- presence
level: 2
neo4j: true
insert: true
---
# God Is Future

> [!Thought-en]
> God is your Future.

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Jun-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD IS FUTURE",
    alias: "Thought: God Is Future",
    parent: "topic.SPIRITUALITY",
    tags: ['future', 'god', 'spirituality', 'eternity', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD IS FUTURE",
    en_title: "God Is Future",
    en_content: "God is your Future.",
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
WHERE t.name = "thought.GOD IS FUTURE" AND c.name = "content.GOD IS FUTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD IS FUTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.GOD IS FUTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >GOD IS FUTURE" }]->(child);
```