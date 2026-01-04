---
name: "thought.ALL OF GOD JESUS"
alias: "Thought: All Of God Jesus"
type: THOUGHT
en_content: "Jesus Christ is the only Man Who could fit ALL OF GOD in Himself, because HE IS GOD!"
parent: topic.THE GOSPEL
tags:
  - jesus
  - christ
  - fullness
  - divinity
  - god
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Oct-2013a)
CREATE (t:THOUGHT {
    name: "thought.ALL OF GOD JESUS",
    alias: "Thought: All Of God Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'christ', 'fullness', 'divinity', 'god'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ALL OF GOD JESUS",
    en_title: "All Of God Jesus",
    en_content: "Jesus Christ is the only Man Who could fit ALL OF GOD in Himself, because HE IS GOD!",
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
WHERE t.name = "thought.ALL OF GOD JESUS" AND c.name = "content.ALL OF GOD JESUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALL OF GOD JESUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ALL OF GOD JESUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >ALL OF GOD JESUS" }]->(child);
```
