---
type: THOUGHT
name: "thought.NOTHING WRONG GOD"
alias: "Thought: Nothing Wrong God"
parent: "topic.THE GODHEAD"
en_content: "There is nothing wrong with God."
tags: ["character", "perfection", "god", "divinity", "truth"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Feb-2013)
CREATE (t:THOUGHT {    name: "thought.NOTHING WRONG GOD",
    alias: "Thought: Nothing Wrong God",
    parent: "topic.THE GODHEAD",
    tags: ['character', 'perfection', 'god', 'divinity', 'truth'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.NOTHING WRONG GOD",
    ctype: "THOUGHT",
    en_title: "Nothing Wrong God",
    en_content: "There is nothing wrong with God.",
    es_title: "Nada Malo en Dios",
    es_content: "No hay nada malo en Dios.",
    fr_title: "Rien de Mal en Dieu",
    fr_content: "Il n'y a rien de mal en Dieu.",
    hi_title: "परमेश्वर में कोई दोष नहीं",
    hi_content: "परमेश्वर में कोई दोष नहीं है।",
    zh_title: "Shén méiyǒu cuòwù",
    zh_content: "Shén méiyǒu rènhé cuòwù."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NOTHING WRONG GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->NOTHING WRONG GOD"
RETURN t, parent;
```
