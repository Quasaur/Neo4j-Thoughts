---
type: THOUGHT
name: "thought.IRREDUCIBLE COMPLEXITY"
alias: "Thought: Irreducible Complexity"
parent: "topic.CREATION"
en_content: "It's going to take more than a judge's ruling to disprove the TRUTH of Irreducible Complexity."
tags: ["creation", "complexity", "design", "truth", "science"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.IRREDUCIBLE COMPLEXITY",
    alias: "Thought: Irreducible Complexity",
    parent: "topic.CREATION",
    tags: ['creation', 'complexity', 'design', 'truth', 'science'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IRREDUCIBLE COMPLEXITY",
    ctype: "THOUGHT",
    en_title: "Irreducible Complexity",
    en_content: "It's going to take more than a judge's ruling to disprove the TRUTH of Irreducible Complexity.",
    es_title: "Complejidad irreductible",
    es_content: "Se necesitará más que el fallo de un juez para refutar la VERDAD de la Complejidad Irreducible.",
    fr_title: "Complexité irréductible",
    fr_content: "Il faudra plus qu’une décision d’un juge pour réfuter la VÉRITÉ de la complexité irréductible.",
    hi_title: "अघुलनशील जटिलता",
    hi_content: "इरेड्यूसबल जटिलता के सत्य को अस्वीकार करने में एक न्यायाधीश के फैसले से अधिक समय लगेगा।",
    zh_title: "不可减少的复杂性",
    zh_content: "要反驳不可简化的复杂性的真相，需要的不仅仅是法官的裁决。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.IRREDUCIBLE COMPLEXITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->IRREDUCIBLE COMPLEXITY"
RETURN t, parent;
```
