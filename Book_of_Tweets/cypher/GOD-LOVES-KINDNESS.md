---
name: "thought.GOD LOVES KINDNESS"
alias: "Thought: God Loves Kindness"
type: THOUGHT
en_content: "God loves Kindness!"
parent: "topic.THE GODHEAD"
tags:
- kindness
- character
- god
- love
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Jun-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD LOVES KINDNESS",
    alias: "Thought: God Loves Kindness",
    parent: "topic.THE GODHEAD",
    tags: ['kindness', 'character', 'god', 'love', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD LOVES KINDNESS",
    en_title: "God Loves Kindness",
    en_content: "God loves Kindness!",
    es_title: "Dios Ama la Bondad",
    es_content: "¡Dios ama la Bondad!",
    fr_title: "Dieu Aime la Bonté",
    fr_content: "Dieu aime la Bonté !",
    hi_title: "परमेश्वर दया से प्रेम करते हैं",
    hi_content: "परमेश्वर दया से प्रेम करते हैं!",
    zh_title: "Shàngdì ài shànláng 上帝爱善良",
    zh_content: "Shàngdì rè'ai shànláng! 上帝热爱善良！"
});

MATCH (t:THOUGHT {name: "thought.GOD LOVES KINDNESS"})
MATCH (c:CONTENT {name: "content.GOD LOVES KINDNESS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD LOVES KINDNESS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD LOVES KINDNESS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD LOVES KINDNESS" }]->(child);
```
