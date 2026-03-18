---
type: THOUGHT
name: "thought.INTELLIGENT DESIGN"
alias: "Thought: Intelligent Design"
parent: "topic.CREATION"
en_content: "INTELLIGENT DESIGN!"
tags: ["creation", "design", "intelligence", "truth", "science"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.INTELLIGENT DESIGN",
    alias: "Thought: Intelligent Design",
    parent: "topic.CREATION",
    tags: ['creation', 'design', 'intelligence', 'truth', 'science'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INTELLIGENT DESIGN",
    ctype: "THOUGHT",
    en_title: "Intelligent Design",
    en_content: "INTELLIGENT DESIGN!",
    es_title: "Diseño Inteligente",
    es_content: "¡DISEÑO INTELIGENTE!",
    fr_title: "Conception Intelligente",
    fr_content: "CONCEPTION INTELLIGENTE !",
    hi_title: "बुद्धिमान डिज़ाइन",
    hi_content: "बुद्धिमान डिज़ाइन!",
    zh_title: "Zhìhuì shèjì 智慧设计",
    zh_content: "Zhìnéng shèjì! 智能设计！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INTELLIGENT DESIGN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->INTELLIGENT DESIGN"
RETURN t, parent;
```
