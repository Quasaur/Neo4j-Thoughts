---
name: "thought.EYES OF CHRIST"
alias: "Thought: Eyes Of Christ"
type: THOUGHT
en_content: "From the smallest subatomic particle to the deepest intent of the human heart, the Eyes of Christ miss nothing."
parent: "topic.THE GODHEAD"
tags:
- omniscience
- christ
- science
- heart
- divinity
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.EYES OF CHRIST",
    alias: "Thought: Eyes Of Christ",
    parent: "topic.THE GODHEAD",
    tags: ['omniscience', 'christ', 'science', 'heart', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.EYES OF CHRIST",
    en_title: "Eyes Of Christ",
    en_content: "From the smallest subatomic particle to the deepest intent of the human heart, the Eyes of Christ miss nothing.",
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
WHERE t.name = "thought.EYES OF CHRIST" AND c.name = "content.EYES OF CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EYES OF CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.EYES OF CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >EYES OF CHRIST" }]->(child);
```
