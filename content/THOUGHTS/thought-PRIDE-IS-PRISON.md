---
type: THOUGHT
name: "thought.PRIDE IS PRISON"
alias: "Thought: Pride Is Prison"
parent: "topic.EVIL"
en_content: "Pride is a prison, and Unconditional Love the only Liberator."
tags: ["pride", "love", "freedom", "attitude", "liberation"]
ptopic: "[[topic-EVIL]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PRIDE IS PRISON",
    alias: "Thought: Pride Is Prison",
    parent: "topic.EVIL",
    tags: ['pride', 'love', 'freedom', 'attitude', 'liberation'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PRIDE IS PRISON",
    ctype: "THOUGHT",
    en_title: "Pride Is Prison",
    en_content: "Pride is a prison, and Unconditional Love the only Liberator.",
    es_title: "El Orgullo Es Prisión",
    es_content: "El orgullo es una prisión, y el Amor Incondicional el único Libertador.",
    fr_title: "L'Orgueil Est Prison",
    fr_content: "L'orgueil est une prison, et l'Amour Inconditionnel le seul Libérateur.",
    hi_title: "अहंकार कारागार है",
    hi_content: "अहंकार एक कारागार है, और निःशर्त प्रेम ही एकमात्र मुक्तिदाता है।",
    zh_title: "Jiāo'ào Shì Jiānyù",
    zh_content: "Jiāo'ào shì yīzuò jiānyù, ér Wútiáojiàn de Ài shì wéiyī de Jiětuō zhě."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRIDE IS PRISON"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->PRIDE IS PRISON"
RETURN t, parent;
```
