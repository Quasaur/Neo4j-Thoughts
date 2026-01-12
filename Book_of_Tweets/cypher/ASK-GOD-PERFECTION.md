---
name: "thought.ASK GOD PERFECTION"
alias: "Thought: Ask God Perfection"
type: THOUGHT
en_content: "Perfection isn't that difficult...ask God!"
parent: "topic.THE GODHEAD"
tags:
- perfection
- god
- holiness
- divinity
- relationship
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.ASK GOD PERFECTION",
    alias: "Thought: Ask God Perfection",
    parent: "topic.THE GODHEAD",
    tags: ['perfection', 'god', 'holiness', 'divinity', 'relationship'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ASK GOD PERFECTION",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ASK GOD PERFECTION" AND c.name = "content.ASK GOD PERFECTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ASK GOD PERFECTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ASK GOD PERFECTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >ASK GOD PERFECTION" }]->(child);
```
