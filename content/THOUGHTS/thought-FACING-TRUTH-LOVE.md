---
type: THOUGHT
name: "thought.FACING TRUTH LOVE"
alias: "Thought: Facing Truth Love"
parent: "topic.LOVE"
en_content: "It's God's Love for us that enables us to face the truth about ourselves."
tags: ["love", "truth", "grace", "self_examination", "transformation"]
ptopic: "[[topic-LOVE]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FACING TRUTH LOVE",
    alias: "Thought: Facing Truth Love",
    parent: "topic.LOVE",
    tags: ['love', 'truth', 'grace', 'self_examination', 'transformation'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FACING TRUTH LOVE",
    ctype: "THOUGHT",
    en_title: "Facing Truth Love",
    en_content: "It's God's Love for us that enables us to face the truth about ourselves.",
    es_title: "Amor que Enfrenta la Verdad",
    es_content: "Es el Amor de Dios por nosotros lo que nos permite enfrentar la verdad sobre nosotros mismos.",
    fr_title: "L'Amour qui Affronte la Vérité",
    fr_content: "C'est l'Amour de Dieu pour nous qui nous permet de faire face à la vérité sur nous-mêmes.",
    hi_title: "सत्य का सामना करने वाला प्रेम",
    hi_content: "यह परमेश्वर का हमारे लिए प्रेम है जो हमें अपने बारे में सत्य का सामना करने में सक्षम बनाता है।",
    zh_title: "Mian Dui Zhen Li De Ai",
    zh_content: "Zheng Shi Shang Di Dui Wo Men De Ai Shi Wo Men Neng Gou Mian Dui Guan Yu Zi Ji De Zhen Li."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FACING TRUTH LOVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->FACING TRUTH LOVE"
RETURN t, parent;
```
