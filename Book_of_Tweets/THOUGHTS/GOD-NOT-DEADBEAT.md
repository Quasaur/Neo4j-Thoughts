---
name: "thought.GOD NOT DEADBEAT"
alias: "Thought: God Not Deadbeat"
type: THOUGHT
en_content: "God is not a deadbeat... He takes care of His own."
parent: "topic.THE GODHEAD"
tags:
- provision
- care
- god
- character
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Jun-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD NOT DEADBEAT",
    alias: "Thought: God Not Deadbeat",
    parent: "topic.THE GODHEAD",
    tags: ['provision', 'care', 'god', 'character', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD NOT DEADBEAT",
    en_title: "God Not Deadbeat",
    en_content: "God is not a deadbeat... He takes care of His own.",
    es_title: "Dios No es un Irresponsable",
    es_content: "Dios no es un irresponsable... Él cuida de los Suyos.",
    fr_title: "Dieu n'est Pas un Irresponsable",
    fr_content: "Dieu n'est pas un irresponsable... Il prend soin des Siens.",
    hi_title: "परमेश्वर लापरवाह नहीं",
    hi_content: "परमेश्वर लापरवाह नहीं हैं... वे अपनों की देखभाल करते हैं।",
    zh_title: "Shàngdì bù shì làndàng  shàng dì bú shì làn dāng",
    zh_content: "Shàngdì bù shì làndàng... tā huì zhàogù zìjǐ de rén.  shàng dì bú shì làn dāng ... tā huì zhào gù zì jǐ de rén 。"
});

MATCH (t:THOUGHT {name: "thought.GOD NOT DEADBEAT"})
MATCH (c:CONTENT {name: "content.GOD NOT DEADBEAT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD NOT DEADBEAT" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD NOT DEADBEAT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GOD NOT DEADBEAT" }]->(child);
```
