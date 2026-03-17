---
type: THOUGHT
name: "thought.LIVING RELATIONSHIPS"
alias: "Thought: Living Relationship"
parent: "topic.PSYCHOLOGY"
en_content: "Life is all about relationships."
tags: ["live", "relationships", "people", "jesus_christ", "god"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LIVING RELATIONSHIPS",
    alias: "Thought: Living Relationship",
    parent: "topic.PSYCHOLOGY",
    tags: ["live", "relationships", "people", "jesus_christ", "god"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LIVING RELATIONSHIPS",
    ctype: "THOUGHT",
    en_title: "Living Relationship",
    en_content: "Life is all about relationships.",
    es_title: "RELACIÓN DE VIDA",
    es_content: "La vida se trata de relaciones.",
    fr_title: "RELATION VIVANTE",
    fr_content: "La vie est une question de relations.",
    hi_title: "जीवित संबंध",
    hi_content: "जीवन रिश्तों के बारे में है।",
    zh_title: "shēng huó guān xì",
    zh_content: "shēng huó jiù shì guān xì 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIVING RELATIONSHIPS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->LIVING RELATIONSHIPS"
RETURN t, parent;
```
