---
type: THOUGHT
name: "thought.NATURE OF REALITY"
alias: "Thought: Nature Of Reality"
parent: "topic.PHILOSOPHY"
en_content: "Reality: perhaps matter is only real to other matter...?"
tags: ["reality", "matter", "philosophy", "ontology", "perception"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2010b)
CREATE (t:THOUGHT {    name: "thought.NATURE OF REALITY",
    alias: "Thought: Nature Of Reality",
    parent: "topic.PHILOSOPHY",
    tags: ['reality', 'matter', 'philosophy', 'ontology', 'perception'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.NATURE OF REALITY",
    ctype: "THOUGHT",
    en_title: "Nature Of Reality",
    en_content: "Reality: perhaps matter is only real to other matter...?",
    es_title: "Naturaleza de la realidad",
    es_content: "Realidad: ¿quizás la materia sólo es real para otra materia...?",
    fr_title: "Nature de la réalité",
    fr_content: "Réalité : peut-être que la matière n'est réelle que pour une autre matière... ?",
    hi_title: "वास्तविकता की प्रकृति",
    hi_content: "वास्तविकता: शायद पदार्थ केवल दूसरे पदार्थ के लिए ही वास्तविक है...?",
    zh_title: "xiàn shí de běn zhì",
    zh_content: "xiàn shí ： yě xǔ wù zhì zhǐ duì qí tā wù zhì cái shì zhēn shí de ……？"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NATURE OF REALITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->NATURE OF REALITY"
RETURN t, parent;
```
