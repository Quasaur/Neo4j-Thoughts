---
name: "thought.GOD LOVES ABUSERS"
alias: "Thought: God Loves Abusers"
type: THOUGHT
en_content: "God loves abusers."
parent: "topic.THE GODHEAD"
tags:
- love
- god
- abusers
- mercy
- character
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Feb-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD LOVES ABUSERS",
    alias: "Thought: God Loves Abusers",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'god', 'abusers', 'mercy', 'character'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD LOVES ABUSERS",
    en_title: "God Loves Abusers",
    en_content: "God loves abusers.",
    es_title: "Dios Ama a los Abusadores",
    es_content: "Dios ama a los abusadores.",
    fr_title: "Dieu Aime les Abuseurs",
    fr_content: "Dieu aime les abuseurs.",
    hi_title: "ईश्वर दुर्व्यवहार करने वालों से प्रेम करता है",
    hi_content: "ईश्वर दुर्व्यवहार करने वालों से प्रेम करता है।",
    zh_title: "Shàngdì ài shīnüè zhě",
    zh_content: "Shàngdì ài shīnüè zhě."
});

MATCH (t:THOUGHT {name: "thought.GOD LOVES ABUSERS"})
MATCH (c:CONTENT {name: "content.GOD LOVES ABUSERS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD LOVES ABUSERS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD LOVES ABUSERS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GOD LOVES ABUSERS" }]->(child);
```
