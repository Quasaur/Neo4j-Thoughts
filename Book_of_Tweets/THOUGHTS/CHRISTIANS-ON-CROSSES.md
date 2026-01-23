---
name: "thought.CHRISTIANS ON CROSSES"
alias: "Thought: Christians On Crosses"
type: THOUGHT
en_content: "True Christians are easy to identify: they're the ones hanging on crosses."
parent: "topic.RELIGION"
tags:
- christians
- cross
- identity
- religion
- sacrifice
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.CHRISTIANS ON CROSSES",
    alias: "Thought: Christians On Crosses",
    parent: "topic.RELIGION",
    tags: ['christians', 'cross', 'identity', 'religion', 'sacrifice'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHRISTIANS ON CROSSES",
    en_title: "Christians On Crosses",
    en_content: "True Christians are easy to identify: they're the ones hanging on crosses.",
    es_title: "Cristianos en Cruces",
    es_content: "Los verdaderos cristianos son fáciles de identificar: son los que están colgados en cruces.",
    fr_title: "Chrétiens sur des Croix",
    fr_content: "Les vrais chrétiens sont faciles à identifier : ce sont ceux qui sont suspendus à des croix.",
    hi_title: "क्रूस पर ईसाई",
    hi_content: "सच्चे ईसाई पहचानने में आसान हैं: वे वे हैं जो क्रूस पर लटके हुए हैं।",
    zh_title: "Guà Zài Shízi Jià Shàng de Jīdūtú",
    zh_content: "Zhēnzhèng de Jīdūtú hěn róngyì shi bié: Tāmen shì guà zài shízi jià shàng de rén."
});

MATCH (t:THOUGHT {name: "thought.CHRISTIANS ON CROSSES"})
MATCH (c:CONTENT {name: "content.CHRISTIANS ON CROSSES"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRISTIANS ON CROSSES" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.CHRISTIANS ON CROSSES"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHRISTIANS ON CROSSES" }]->(child);
```
