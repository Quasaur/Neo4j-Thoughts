---
type: THOUGHT
name: "thought.SPECIFIED COMPLEXITY"
alias: "Thought: Specified Complexity"
parent: "topic.CREATION"
en_content: "Evolution can't explain Specified Complexity."
tags: ["creation", "complexity", "design", "evolution", "intelligence"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SPECIFIED COMPLEXITY",
    alias: "Thought: Specified Complexity",
    parent: "topic.CREATION",
    tags: ['creation', 'complexity', 'design', 'evolution', 'intelligence'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPECIFIED COMPLEXITY",
    ctype: "THOUGHT",
    en_title: "Specified Complexity",
    en_content: "Evolution can't explain Specified Complexity.",
    es_title: "Complejidad especificada",
    es_content: "La evolución no puede explicar la Complejidad Especificada.",
    fr_title: "Complexité spécifiée",
    fr_content: "L'évolution ne peut pas expliquer la complexité spécifiée.",
    hi_title: "निर्दिष्ट जटिलता",
    hi_content: "विकास निर्दिष्ट जटिलता की व्याख्या नहीं कर सकता।",
    zh_title: "指定复杂度",
    zh_content: "进化论无法解释特定的复杂性。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SPECIFIED COMPLEXITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->SPECIFIED COMPLEXITY"
RETURN t, parent;
```
