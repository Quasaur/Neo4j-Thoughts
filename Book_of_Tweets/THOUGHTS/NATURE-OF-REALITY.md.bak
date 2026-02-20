---
name: "thought.NATURE OF REALITY"
alias: "Thought: Nature Of Reality"
type: THOUGHT
en_content: "Reality: perhaps matter is only real to other matter...?"
parent: "topic.PHILOSOPHY"
tags:
- reality
- matter
- philosophy
- ontology
- perception
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2010b)
CREATE (t:THOUGHT {
    name: "thought.NATURE OF REALITY",
    alias: "Thought: Nature Of Reality",
    parent: "topic.PHILOSOPHY",
    tags: ['reality', 'matter', 'philosophy', 'ontology', 'perception'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NATURE OF REALITY",
    en_title: "Nature Of Reality",
    en_content: "Reality: perhaps matter is only real to other matter...?",
    es_title: "Naturaleza de la realidad",
    es_content: "Realidad: ¿quizás la materia sólo es real para otra materia...?",
    fr_title: "Nature de la réalité",
    fr_content: "Réalité : peut-être que la matière n'est réelle que pour une autre matière... ?",
    hi_title: "वास्तविकता की प्रकृति",
    hi_content: "वास्तविकता: शायद पदार्थ केवल दूसरे पदार्थ के लिए ही वास्तविक है...?",
    zh_title: "现实的本质",
    zh_content: "现实：也许物质只对其他物质才是真实的……？"
});

MATCH (t:THOUGHT {name: "thought.NATURE OF REALITY"})
MATCH (c:CONTENT {name: "content.NATURE OF REALITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NATURE OF REALITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.NATURE OF REALITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY->NATURE OF REALITY" }]->(child);
```
