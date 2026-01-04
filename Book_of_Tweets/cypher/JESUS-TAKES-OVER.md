---
name: "thought.JESUS TAKES OVER"
alias: "Thought: Jesus Takes Over"
type: THOUGHT
en_content: "\"I come: not to take sides, but to take over.\" - Jesus Christ"
parent: "topic.THE GODHEAD"
tags:
- jesus
- power
- sovereignty
- kingdom
- takeover
level: 1
neo4j: true
insert: true
---
# Jesus Takes Over

> [!Thought-en]
> "I come: not to take sides, but to take over." - Jesus Christ

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.JESUS TAKES OVER",
    alias: "Thought: Jesus Takes Over",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'power', 'sovereignty', 'kingdom', 'takeover'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.JESUS TAKES OVER",
    en_title: "Jesus Takes Over",
    en_content: "\"I come: not to take sides, but to take over.\" - Jesus Christ",
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
WHERE t.name = "thought.JESUS TAKES OVER" AND c.name = "content.JESUS TAKES OVER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.JESUS TAKES OVER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.JESUS TAKES OVER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >JESUS TAKES OVER" }]->(child);
```