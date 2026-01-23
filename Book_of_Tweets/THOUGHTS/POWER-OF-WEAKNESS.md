---
name: "thought.POWER OF WEAKNESS"
alias: "Thought: Power Of Weakness"
type: THOUGHT
en_content: "True Strength understands the Power of Weakness."
parent: "topic.WISDOM"
tags:
- strength
- weakness
- power
- wisdom
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Mar-2012a)
CREATE (t:THOUGHT {
    name: "thought.POWER OF WEAKNESS",
    alias: "Thought: Power Of Weakness",
    parent: "topic.WISDOM",
    tags: ['strength', 'weakness', 'power', 'wisdom', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.POWER OF WEAKNESS",
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

MATCH (t:THOUGHT {name: "thought.POWER OF WEAKNESS"})
MATCH (c:CONTENT {name: "content.POWER OF WEAKNESS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.POWER OF WEAKNESS" }]->(c);

MATCH (parent:TOPIC {name: "topic.WISDOM"})
MATCH (child:THOUGHT {name: "thought.POWER OF WEAKNESS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >POWER OF WEAKNESS" }]->(child);
```
