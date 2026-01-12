---
name: "thought.PRIEST OF CHRIST"
alias: "Thought: Priest Of Christ"
type: THOUGHT
en_content: "As a priest of Christ, it's my job to speak God's Word (The Holy Bible) into the planetary atmosphere."
parent: "topic.SPIRITUALITY"
tags:
- priest
- christ
- atmosphere
- bible
- assignment
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Apr-2012b)
CREATE (t:THOUGHT {
    name: "thought.PRIEST OF CHRIST",
    alias: "Thought: Priest Of Christ",
    parent: "topic.SPIRITUALITY",
    tags: ['priest', 'christ', 'atmosphere', 'bible', 'assignment'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRIEST OF CHRIST",
    en_title: "Priest Of Christ",
    en_content: "As a priest of Christ, it's my job to speak God's Word (The Holy Bible) into the planetary atmosphere.",
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
WHERE t.name = "thought.PRIEST OF CHRIST" AND c.name = "content.PRIEST OF CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRIEST OF CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRIEST OF CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRIEST OF CHRIST" }]->(child);
```
