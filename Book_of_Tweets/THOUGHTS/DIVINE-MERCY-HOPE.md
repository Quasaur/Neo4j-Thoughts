---
name: "thought.DIVINE MERCY HOPE"
alias: "Thought: Divine Mercy Hope"
type: THOUGHT
en_content: "Apart from Divine Mercy there is no hope for the human race."
parent: "topic.GRACE"
tags:
- mercy
- hope
- grace
- humanity
- salvation
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Dec-2010)
CREATE (t:THOUGHT {
    name: "thought.DIVINE MERCY HOPE",
    alias: "Thought: Divine Mercy Hope",
    parent: "topic.GRACE",
    tags: ['mercy', 'hope', 'grace', 'humanity', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DIVINE MERCY HOPE",
    en_title: "Divine Mercy Hope",
    en_content: "Apart from Divine Mercy there is no hope for the human race.",
    es_title: "Esperanza de la Misericordia Divina",
    es_content: "Sin la Misericordia Divina no hay esperanza para la raza humana.",
    fr_title: "Espoir de la Miséricorde Divine",
    fr_content: "Sans la Miséricorde Divine, il n'y a pas d'espoir pour la race humaine.",
    hi_title: "दिव्य कृपा की आशा",
    hi_content: "दिव्य कृपा के बिना मानव जाति के लिए कोई आशा नहीं है।",
    zh_title: "Shén Cí Xīwàng",
    zh_content: "Chúle Shén de cíbēi zhīwài, rénlèi méiyǒu xīwàng."
});

MATCH (t:THOUGHT {name: "thought.DIVINE MERCY HOPE"})
MATCH (c:CONTENT {name: "content.DIVINE MERCY HOPE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DIVINE MERCY HOPE" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.DIVINE MERCY HOPE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE->DIVINE MERCY HOPE" }]->(child);
```
