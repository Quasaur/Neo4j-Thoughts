---
name: "thought.BORN TWICE"
alias: "Thought: Born Twice"
type: THOUGHT
en_content: "Born once, die twice; born twice, die once--Happy Resurrection Day!"
parent: "topic.RELIGION"
tags:
- resurrection
- life
- death
- rebirth
- salvation
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.BORN TWICE",
    alias: "Thought: Born Twice",
    parent: "topic.RELIGION",
    tags: ['resurrection', 'life', 'death', 'rebirth', 'salvation'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.BORN TWICE",
    en_title: "Born Twice",
    en_content: "Born once, die twice; born twice, die once--Happy Resurrection Day!",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BORN TWICE" AND c.name = "content.BORN TWICE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BORN TWICE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.BORN TWICE"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >BORN TWICE" }]->(child);
```
