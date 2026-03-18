---
type: THOUGHT
name: "thought.PRAYER NOT JOB"
alias: "Thought: Prayer Not Job"
parent: "topic.SPIRITUALITY"
en_content: "Prayer was never meant to be a job."
tags: ["prayer", "work", "spirituality", "connection", "attitude"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013a)
CREATE (t:THOUGHT {    name: "thought.PRAYER NOT JOB",
    alias: "Thought: Prayer Not Job",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'work', 'spirituality', 'connection', 'attitude'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.PRAYER NOT JOB",
    ctype: "THOUGHT",
    en_title: "Prayer Not Job",
    en_content: "Prayer was never meant to be a job.",
    es_title: "La Oración No Es Trabajo",
    es_content: "La oración nunca fue pensada para ser un trabajo.",
    fr_title: "La Prière N'est Pas un Travail",
    fr_content: "La prière n'a jamais été conçue pour être un travail.",
    hi_title: "प्रार्थना कोई काम नहीं",
    hi_content: "प्रार्थना कभी भी एक काम बनने के लिए नहीं थी।",
    zh_title: "Qí dǎo Bú Shì Gōng Zuò",
    zh_content: "Qí dǎo cóng lái dōu bú shì wèi le chéng wéi yī fèn gōng zuò."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRAYER NOT JOB"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->PRAYER NOT JOB"
RETURN t, parent;
```
