---
name: "thought.SPECIFIED COMPLEXITY"
alias: "Thought: Specified Complexity"
type: THOUGHT
en_content: "Evolution can't explain Specified Complexity."
parent: "topic.CREATION"
tags:
- creation
- complexity
- design
- evolution
- intelligence
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Nov-2010a)
CREATE (t:THOUGHT {
    name: "thought.SPECIFIED COMPLEXITY",
    alias: "Thought: Specified Complexity",
    parent: "topic.CREATION",
    tags: ['creation', 'complexity', 'design', 'evolution', 'intelligence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPECIFIED COMPLEXITY",
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

MATCH (t:THOUGHT {name: "thought.SPECIFIED COMPLEXITY"})
MATCH (c:CONTENT {name: "content.SPECIFIED COMPLEXITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPECIFIED COMPLEXITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.CREATION"})
MATCH (child:THOUGHT {name: "thought.SPECIFIED COMPLEXITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >SPECIFIED COMPLEXITY" }]->(child);
```
