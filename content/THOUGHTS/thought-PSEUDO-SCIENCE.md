---
type: THOUGHT
name: "thought.PSEUDO SCIENCE"
alias: "Thought: Pseudo-science"
parent: "topic.COSMOLOGY"
en_content: "There is no science without God."
tags: ["science", "divinity", "pseudoscience", "truth", "deity"]
ptopic: "[[topic-COSMOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PSEUDO SCIENCE",
    alias: "Thought: Pseudo-science",
    parent: "topic.COSMOLOGY",
    tags: ["science", "divinity", "pseudoscience", "truth", "deity"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PSEUDO SCIENCE",
    ctype: "THOUGHT",
    en_title: "Pseudo-science",
    en_content: "There is no science without God.",
    es_title: "PSEUDO-CIENCIA",
    es_content: "No hay ciencia sin Dios.",
    fr_title: "PSEUDO-SCIENCE",
    fr_content: "Il n'y a pas de science sans Dieu.",
    hi_title: "छद्म विज्ञान",
    hi_content: "ईश्वर के बिना कोई विज्ञान नहीं है।",
    zh_title: "wěi kē xué",
    zh_content: "méi yǒu shàng dì jiù méi yǒu kē xué 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PSEUDO SCIENCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.COSMOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.COSMOLOGY->PSEUDO SCIENCE"
RETURN t, parent;
```
