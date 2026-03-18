---
type: THOUGHT
name: "thought.INCORRUPTIBLE GOODNESS"
alias: "Thought: Incorruptible Goodness"
parent: "topic.THE GODHEAD"
en_content: "Good is greater than evil; for the Fountain of All Good (God) has never been nor can ever be corrupted by evil."
tags: ["goodness", "god", "corruption", "divinity", "character"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012c)
CREATE (t:THOUGHT {    name: "thought.INCORRUPTIBLE GOODNESS",
    alias: "Thought: Incorruptible Goodness",
    parent: "topic.THE GODHEAD",
    tags: ['goodness', 'god', 'corruption', 'divinity', 'character'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.INCORRUPTIBLE GOODNESS",
    ctype: "THOUGHT",
    en_title: "Incorruptible Goodness",
    en_content: "Good is greater than evil; for the Fountain of All Good (God) has never been nor can ever be corrupted by evil.",
    es_title: "Bondad Incorruptible",
    es_content: "El bien es mayor que el mal; pues la Fuente de Todo Bien (Dios) nunca ha sido ni puede jamás ser corrompida por el mal.",
    fr_title: "Bonté Incorruptible",
    fr_content: "Le bien est plus grand que le mal ; car la Source de Tout Bien (Dieu) n'a jamais été et ne peut jamais être corrompue par le mal.",
    hi_title: "अविनाशी भलाई",
    hi_content: "भलाई बुराई से बड़ी है; क्योंकि समस्त भलाई का स्रोत (परमेश्वर) न कभी भ्रष्ट हुआ है और न कभी बुराई से भ्रष्ट हो सकता है।",
    zh_title: "Bu Xiu De Shan Liang",
    zh_content: "Shan da yu e; yin wei yi qie shan de quan yuan (Shen) cong wei ye bu neng bei e suo fu bai."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INCORRUPTIBLE GOODNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->INCORRUPTIBLE GOODNESS"
RETURN t, parent;
```
