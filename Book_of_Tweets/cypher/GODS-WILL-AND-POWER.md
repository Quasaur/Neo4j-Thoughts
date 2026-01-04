---
name: "thought.GODS WILL AND POWER"
alias: "Thought: Gods Will And Power"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- will
- desire
- power
- god
level: 1
neo4j: true
insert: true
---
# Gods Will And Power

> [!Thought-en]
> God has His Own Will and Desire and more than enough Power to execute Them.

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2014)
CREATE (t:THOUGHT {
    name: "thought.GODS WILL AND POWER",
    alias: "Thought: Gods Will And Power",
    parent: "topic.THE GODHEAD",
    tags: ['will', 'desire', 'power', 'god'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS WILL AND POWER",
    en_title: "Gods Will And Power",
    en_content: "God has His Own Will and Desire and more than enough Power to execute Them.",
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
WHERE t.name = "thought.GODS WILL AND POWER" AND c.name = "content.GODS WILL AND POWER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS WILL AND POWER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS WILL AND POWER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS WILL AND POWER" }]->(child);
```