---
type: THOUGHT
name: "thought.GOD NOT DEADBEAT"
alias: "Thought: God Not Deadbeat"
parent: "topic.THE GODHEAD"
en_content: "God is not a deadbeat... He takes care of His own."
tags: ["provision", "care", "god", "character", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Jun-2013)
CREATE (t:THOUGHT {    name: "thought.GOD NOT DEADBEAT",
    alias: "Thought: God Not Deadbeat",
    parent: "topic.THE GODHEAD",
    tags: ['provision', 'care', 'god', 'character', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD NOT DEADBEAT",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD NOT DEADBEAT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD NOT DEADBEAT"
RETURN t, parent;
```
