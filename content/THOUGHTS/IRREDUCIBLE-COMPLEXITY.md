---
name: "thought.IRREDUCIBLE COMPLEXITY"
alias: "Thought: Irreducible Complexity"
type: THOUGHT
en_content: "It's going to take more than a judge's ruling to disprove the TRUTH of Irreducible Complexity."
parent: "topic.CREATION"
tags:
- creation
- complexity
- design
- truth
- science
level: 2
neo4j: true
ptopic: "[[topic-CREATION]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Nov-2010b)
CREATE (t:THOUGHT {
    name: "thought.IRREDUCIBLE COMPLEXITY",
    alias: "Thought: Irreducible Complexity",
    parent: "topic.CREATION",
    tags: ['creation', 'complexity', 'design', 'truth', 'science'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IRREDUCIBLE COMPLEXITY",
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

MATCH (t:THOUGHT {name: "thought.IRREDUCIBLE COMPLEXITY"})
MATCH (c:CONTENT {name: "content.IRREDUCIBLE COMPLEXITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.IRREDUCIBLE COMPLEXITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.CREATION"})
MATCH (child:THOUGHT {name: "thought.IRREDUCIBLE COMPLEXITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION->IRREDUCIBLE COMPLEXITY" }]->(child);
```
