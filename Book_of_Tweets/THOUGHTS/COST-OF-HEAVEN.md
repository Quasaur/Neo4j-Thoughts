---
name: "thought.COST OF HEAVEN"
alias: "Thought: Cost Of Heaven"
type: THOUGHT
en_content: "Heaven is free--but it ain't cheap!"
parent: "topic.GRACE"
tags:
- heaven
- grace
- sacrifice
- cost
- salvation
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.COST OF HEAVEN",
    alias: "Thought: Cost Of Heaven",
    parent: "topic.GRACE",
    tags: ['heaven', 'grace', 'sacrifice', 'cost', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.COST OF HEAVEN",
    en_title: "Cost Of Heaven",
    en_content: "Heaven is free--but it ain't cheap!",
    es_title: "Costo del Cielo",
    es_content: "¡El cielo es gratis--pero no es barato!",
    fr_title: "Coût du Paradis",
    fr_content: "Le paradis est gratuit--mais ce n'est pas bon marché !",
    hi_title: "स्वर्ग की कीमत",
    hi_content: "स्वर्ग मुफ्त है--लेकिन यह सस्ता नहीं है!",
    zh_title: "Tiān Táng de Dàijià",
    zh_content: "Tiān táng shì miǎnfèi de--dàn tā bù piányi!"
});

MATCH (t:THOUGHT {name: "thought.COST OF HEAVEN"})
MATCH (c:CONTENT {name: "content.COST OF HEAVEN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.COST OF HEAVEN" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.COST OF HEAVEN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE->COST OF HEAVEN" }]->(child);
```
