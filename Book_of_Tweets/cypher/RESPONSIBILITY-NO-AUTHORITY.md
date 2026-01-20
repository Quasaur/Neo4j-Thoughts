---
name: "thought.RESPONSIBILITY NO AUTHORITY"
alias: "Thought: Responsibility No Authority"
type: THOUGHT
en_content: "Responsibility without authority is like a boat without a motor."
parent: "topic.WISDOM"
tags:
- responsibility
- authority
- logic
- wisdom
- analogy
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.RESPONSIBILITY NO AUTHORITY",
    alias: "Thought: Responsibility No Authority",
    parent: "topic.WISDOM",
    tags: ['responsibility', 'authority', 'logic', 'wisdom', 'analogy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RESPONSIBILITY NO AUTHORITY",
    en_title: "Responsibility No Authority",
    en_content: "Responsibility without authority is like a boat without a motor.",
    es_title: "Responsabilidad Sin Autoridad",
    es_content: "La responsabilidad sin autoridad es como un barco sin motor.",
    fr_title: "Responsabilité Sans Autorité",
    fr_content: "La responsabilité sans autorité est comme un bateau sans moteur.",
    hi_title: "अधिकार के बिना जिम्मेदारी",
    hi_content: "अधिकार के बिना जिम्मेदारी एक मोटर के बिना नाव के समान है।",
    zh_title: "Wu Quan Wei De Ze Ren",
    zh_content: "Mei you quan wei de ze ren jiu xiang mei you fa dong ji de chuan."
});

MATCH (t:THOUGHT {name: "thought.RESPONSIBILITY NO AUTHORITY"})
MATCH (c:CONTENT {name: "content.RESPONSIBILITY NO AUTHORITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.RESPONSIBILITY NO AUTHORITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.WISDOM"})
MATCH (child:THOUGHT {name: "thought.RESPONSIBILITY NO AUTHORITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >RESPONSIBILITY NO AUTHORITY" }]->(child);
```
