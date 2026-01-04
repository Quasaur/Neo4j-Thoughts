---
name: "thought.LOOKING LIKE JESUS"
alias: "Thought: Looking Like Jesus"
type: THOUGHT
en_content: "Jesus is what you look like to God!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- identity
- god
- appearance
- divinity
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jul-2012a)
CREATE (t:THOUGHT {
    name: "thought.LOOKING LIKE JESUS",
    alias: "Thought: Looking Like Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'identity', 'god', 'appearance', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.LOOKING LIKE JESUS",
    en_title: "Looking Like Jesus",
    en_content: "Jesus is what you look like to God!",
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
WHERE t.name = "thought.LOOKING LIKE JESUS" AND c.name = "content.LOOKING LIKE JESUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOOKING LIKE JESUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.LOOKING LIKE JESUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >LOOKING LIKE JESUS" }]->(child);
```
