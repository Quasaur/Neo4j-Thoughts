---
type: THOUGHT
name: "thought.DIVINE MERCY HOPE"
alias: "Thought: Divine Mercy Hope"
parent: "topic.MERCY"
en_content: "Apart from Divine Mercy there is no hope for the human race."
tags: ["mercy", "hope", "grace", "humanity", "salvation"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DIVINE MERCY HOPE",
    alias: "Thought: Divine Mercy Hope",
    parent: "topic.MERCY",
    tags: ['mercy', 'hope', 'grace', 'humanity', 'salvation'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.DIVINE MERCY HOPE",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DIVINE MERCY HOPE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->DIVINE MERCY HOPE"
RETURN t, parent;
```
