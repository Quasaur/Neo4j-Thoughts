---
type: THOUGHT
name: "thought.POWER OF WEAKNESS"
alias: "Thought: Power Of Weakness"
parent: "topic.WISDOM"
en_content: "True Strength understands the Power of Weakness."
tags: ["strength", "weakness", "power", "wisdom", "character"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Mar-2012a)
CREATE (t:THOUGHT {    name: "thought.POWER OF WEAKNESS",
    alias: "Thought: Power Of Weakness",
    parent: "topic.WISDOM",
    tags: ['strength', 'weakness', 'power', 'wisdom', 'character'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.POWER OF WEAKNESS",
    ctype: "THOUGHT",
    en_title: "Power Of Weakness",
    en_content: "True Strength understands the Power of Weakness.",
    es_title: "El Poder de la Debilidad",
    es_content: "La Verdadera Fortaleza entiende el Poder de la Debilidad.",
    fr_title: "La Puissance de la Faiblesse",
    fr_content: "La Vraie Force comprend la Puissance de la Faiblesse.",
    hi_title: "दुर्बलता की शक्ति",
    hi_content: "सच्ची शक्ति दुर्बलता की शक्ति को समझती है।",
    zh_title: "Ruòruò zhī Lì",
    zh_content: "Zhēn zhèng de Lìliàng míngbái Ruòruò zhī Lì."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.POWER OF WEAKNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->POWER OF WEAKNESS"
RETURN t, parent;
```
