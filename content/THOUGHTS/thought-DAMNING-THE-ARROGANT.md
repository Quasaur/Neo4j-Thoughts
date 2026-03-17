---
type: THOUGHT
name: "thought.DAMNING THE ARROGANT"
alias: "Thought: Damning The Arrogant"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "How does God damn a sinner? By letting them prosper in their arrogance."
tags: ["judgment", "arrogance", "prosperity", "sovereignty", "god"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DAMNING THE ARROGANT",
    alias: "Thought: Damning The Arrogant",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['judgment', 'arrogance', 'prosperity', 'sovereignty', 'god'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DAMNING THE ARROGANT",
    ctype: "THOUGHT",
    en_title: "Damning The Arrogant",
    en_content: "How does God damn a sinner? By letting them prosper in their arrogance.",
    es_title: "Condenando al Arrogante",
    es_content: "¿Cómo condena Dios a un pecador? Dejándolos prosperar en su arrogancia.",
    fr_title: "Condamner l'Arrogant",
    fr_content: "Comment Dieu damne-t-Il un pécheur ? En le laissant prospérer dans son arrogance.",
    hi_title: "अहंकारी को दंडित करना",
    hi_content: "परमेश्वर एक पापी को कैसे दंडित करता है? उन्हें उनकी अहंकार में समृद्ध होने देता है।",
    zh_title: "Zhìzuì Jiāo'ào Zhě",
    zh_content: "Shàngdì zěnme zhìzuì yīgè zuìrén? Ràng tāmen zài tāmen de jiāo'ào zhōng fánróng."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DAMNING THE ARROGANT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->DAMNING THE ARROGANT"
RETURN t, parent;
```
