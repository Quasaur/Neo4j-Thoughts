---
name: "thought.PRAYER NOT JOB"
alias: "Thought: Prayer Not Job"
type: THOUGHT
en_content: "Prayer was never meant to be a job."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- work
- spirituality
- connection
- attitude
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.PRAYER NOT JOB",
    alias: "Thought: Prayer Not Job",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'work', 'spirituality', 'connection', 'attitude'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER NOT JOB",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRAYER NOT JOB" AND c.name = "content.PRAYER NOT JOB"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER NOT JOB" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER NOT JOB"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER NOT JOB" }]->(child);
```
