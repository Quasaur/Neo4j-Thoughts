---
name: "thought.FIRST LOVE WAITING"
alias: "Thought: First Love Waiting"
type: THOUGHT
en_content: "Prayer is where my First Love is always waiting for me!"
parent: "topic.SPIRITUALITY"
tags:
- prayer
- love
- waiting
- spirituality
- relationship
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013h)
CREATE (t:THOUGHT {
    name: "thought.FIRST LOVE WAITING",
    alias: "Thought: First Love Waiting",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'love', 'waiting', 'spirituality', 'relationship'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FIRST LOVE WAITING",
    en_title: "First Love Waiting",
    en_content: "Prayer is where my First Love is always waiting for me!",
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
WHERE t.name = "thought.FIRST LOVE WAITING" AND c.name = "content.FIRST LOVE WAITING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FIRST LOVE WAITING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.FIRST LOVE WAITING"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >FIRST LOVE WAITING" }]->(child);
```
