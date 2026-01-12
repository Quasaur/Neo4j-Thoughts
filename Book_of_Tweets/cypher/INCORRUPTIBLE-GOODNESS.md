---
name: "thought.INCORRUPTIBLE GOODNESS"
alias: "Thought: Incorruptible Goodness"
type: THOUGHT
en_content: "Good is greater than evil; for the Fountain of All Good (God) has never been nor can ever be corrupted by evil."
parent: "topic.THE GODHEAD"
tags:
- goodness
- god
- corruption
- divinity
- character
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012c)
CREATE (t:THOUGHT {
    name: "thought.INCORRUPTIBLE GOODNESS",
    alias: "Thought: Incorruptible Goodness",
    parent: "topic.THE GODHEAD",
    tags: ['goodness', 'god', 'corruption', 'divinity', 'character'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.INCORRUPTIBLE GOODNESS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INCORRUPTIBLE GOODNESS" AND c.name = "content.INCORRUPTIBLE GOODNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INCORRUPTIBLE GOODNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.INCORRUPTIBLE GOODNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >INCORRUPTIBLE GOODNESS" }]->(child);
```
