---
name: "thought.ALONZO CHURCH FAITH"
alias: "Thought: Alonzo Church Faith"
type: THOUGHT
en_content: "Alonzo Church Ph.D, Inventor of the lambda calculus, was a devout Christian...who says science and faith don't mix?"
parent: "topic.RELIGION"
tags:
- science
- faith
- alonzo_church
- logic
- religion
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Oct-2013b)
CREATE (t:THOUGHT {
    name: "thought.ALONZO CHURCH FAITH",
    alias: "Thought: Alonzo Church Faith",
    parent: "topic.RELIGION",
    tags: ['science', 'faith', 'alonzo_church', 'logic', 'religion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ALONZO CHURCH FAITH",
    en_title: "Alonzo Church Faith",
    en_content: "Alonzo Church Ph.D, Inventor of the lambda calculus, was a devout Christian...who says science and faith don't mix?",
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
WHERE t.name = "thought.ALONZO CHURCH FAITH" AND c.name = "content.ALONZO CHURCH FAITH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALONZO CHURCH FAITH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.ALONZO CHURCH FAITH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >ALONZO CHURCH FAITH" }]->(child);
```
