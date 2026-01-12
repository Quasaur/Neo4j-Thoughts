---
name: "thought.REVELATION ISRAELI CHURCH"
alias: "Thought: Revelation Israeli Church"
type: THOUGHT
en_content: "Revelation is not about the gentile church as much as the Israeli church. In this context, everything starts to make sense."
parent: "topic.RELIGION"
tags:
- revelation
- israel
- church
- bible
- history
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jun-2013)
CREATE (t:THOUGHT {
    name: "thought.REVELATION ISRAELI CHURCH",
    alias: "Thought: Revelation Israeli Church",
    parent: "topic.RELIGION",
    tags: ['revelation', 'israel', 'church', 'bible', 'history'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.REVELATION ISRAELI CHURCH",
    en_title: "Revelation Israeli Church",
    en_content: "Revelation is not about the gentile church as much as the Israeli church. In this context, everything starts to make sense.",
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
WHERE t.name = "thought.REVELATION ISRAELI CHURCH" AND c.name = "content.REVELATION ISRAELI CHURCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REVELATION ISRAELI CHURCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.REVELATION ISRAELI CHURCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >REVELATION ISRAELI CHURCH" }]->(child);
```
