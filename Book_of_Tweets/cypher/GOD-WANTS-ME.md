---
name: "thought.GOD WANTS ME"
alias: "Thought: God Wants Me"
type: THOUGHT
en_content: "Everybody demands something from me, but only God wants me."
parent: "topic.THE GODHEAD"
tags:
- love
- desire
- god
- relationship
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2012c)
CREATE (t:THOUGHT {
    name: "thought.GOD WANTS ME",
    alias: "Thought: God Wants Me",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'desire', 'god', 'relationship', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD WANTS ME",
    en_title: "God Wants Me",
    en_content: "Everybody demands something from me, but only God wants me.",
    es_title: "Dios Me Quiere",
    es_content: "Todos me exigen algo, pero solo Dios me quiere.",
    fr_title: "Dieu Me Veut",
    fr_content: "Tout le monde exige quelque chose de moi, mais seul Dieu me veut.",
    hi_title: "परमेश्वर मुझे चाहता है",
    hi_content: "हर कोई मुझसे कुछ न कुछ मांगता है, लेकिन केवल परमेश्वर मुझे चाहता है।",
    zh_title: "Shàngdì Xiǎng Yào Wǒ",
    zh_content: "Měi gè rén dōu xiàng wǒ suǒqǔ shénme, dàn zhǐyǒu Shàngdì xiǎng yào wǒ."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD WANTS ME" AND c.name = "content.GOD WANTS ME"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD WANTS ME" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD WANTS ME"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD WANTS ME" }]->(child);
```
