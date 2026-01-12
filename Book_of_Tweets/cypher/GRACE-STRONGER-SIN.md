---
name: "thought.GRACE STRONGER SIN"
alias: "Thought: Grace Stronger Sin"
type: THOUGHT
en_content: "Grace is stronger than sin, else no one could be saved. Ephesians 2:8, 9"
parent: "topic.GRACE"
tags:
- grace
- sin
- salvation
- power
- hope
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.GRACE STRONGER SIN",
    alias: "Thought: Grace Stronger Sin",
    parent: "topic.GRACE",
    tags: ['grace', 'sin', 'salvation', 'power', 'hope'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRACE STRONGER SIN",
    en_title: "Grace Stronger Sin",
    en_content: "Grace is stronger than sin, else no one could be saved. Ephesians 2:8, 9",
    es_title: "La Gracia es Más Fuerte que el Pecado",
    es_content: "La gracia es más fuerte que el pecado, de lo contrario nadie podría ser salvado. Efesios 2:8, 9",
    fr_title: "La Grâce Plus Forte que le Péché",
    fr_content: "La grâce est plus forte que le péché, sinon personne ne pourrait être sauvé. Éphésiens 2:8, 9",
    hi_title: "अनुग्रह पाप से अधिक शक्तिशाली है",
    hi_content: "अनुग्रह पाप से अधिक शक्तिशाली है, अन्यथा कोई भी उद्धार नहीं पा सकता। इफिसियों 2:8, 9",
    zh_title: "En Dian Sheng Guo Zui E",
    zh_content: "En dian sheng guo zui e, fou ze mei you ren neng de jiu. Yi fu suo shu 2:8, 9"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GRACE STRONGER SIN" AND c.name = "content.GRACE STRONGER SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GRACE STRONGER SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.GRACE STRONGER SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >GRACE STRONGER SIN" }]->(child);
```
