---
name: "thought.MERCY OF JESUS"
alias: "Thought: Mercy Of Jesus"
type: THOUGHT
en_content: "Jesus is FAR MORE merciful and compassionate than you are!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- mercy
- compassion
- divinity
- love
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.MERCY OF JESUS",
    alias: "Thought: Mercy Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'mercy', 'compassion', 'divinity', 'love'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MERCY OF JESUS",
    en_title: "Mercy Of Jesus",
    en_content: "Jesus is FAR MORE merciful and compassionate than you are!",
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
WHERE t.name = "thought.MERCY OF JESUS" AND c.name = "content.MERCY OF JESUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MERCY OF JESUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MERCY OF JESUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >MERCY OF JESUS" }]->(child);
```
