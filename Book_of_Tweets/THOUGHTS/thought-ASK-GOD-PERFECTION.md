---
type: THOUGHT
name: "thought.ASK GOD PERFECTION"
alias: "Thought: Ask God Perfection"
parent: "topic.THE GODHEAD"
en_content: "Perfection isn't that difficult...ask God!"
tags: ["perfection", "god", "holiness", "divinity", "relationship"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Sep-2012)
CREATE (t:THOUGHT {    name: "thought.ASK GOD PERFECTION",
    alias: "Thought: Ask God Perfection",
    parent: "topic.THE GODHEAD",
    tags: ['perfection', 'god', 'holiness', 'divinity', 'relationship'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.ASK GOD PERFECTION",
    ctype: "THOUGHT",
    en_title: "Ask God Perfection",
    en_content: "Perfection isn't that difficult...ask God!",
    es_title: "Pregúntale a Dios sobre la Perfección",
    es_content: "La perfección no es tan difícil... ¡pregúntale a Dios!",
    fr_title: "Demandez à Dieu la Perfection",
    fr_content: "La perfection n'est pas si difficile... demandez à Dieu !",
    hi_title: "परमेश्वर से पूर्णता पूछें",
    hi_content: "पूर्णता इतनी कठिन नहीं है... परमेश्वर से पूछें!",
    zh_title: "Wèn shén wánměi",
    zh_content: "Wánměi bìng bù nàme kùnnán... wèn wèn shén ba!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ASK GOD PERFECTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->ASK GOD PERFECTION"
RETURN t, parent;
```
