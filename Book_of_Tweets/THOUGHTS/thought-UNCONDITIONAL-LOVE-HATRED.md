---
type: THOUGHT
name: "thought.UNCONDITIONAL LOVE HATRED"
alias: "Thought: Unconditional Love Hatred"
parent: "topic.THE GODHEAD"
en_content: "God's Love is unconditional...as is His Hatred of evil."
tags: ["love", "hatred", "evil", "character", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Oct-2011)
CREATE (t:THOUGHT {    name: "thought.UNCONDITIONAL LOVE HATRED",
    alias: "Thought: Unconditional Love Hatred",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'hatred', 'evil', 'character', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL LOVE HATRED",
    ctype: "THOUGHT",
    en_title: "Unconditional Love Hatred",
    en_content: "God's Love is unconditional...as is His Hatred of evil.",
    es_title: "Amor Incondicional Odio",
    es_content: "El Amor de Dios es incondicional...así como Su Odio al mal.",
    fr_title: "Amour Inconditionnel Haine",
    fr_content: "L'Amour de Dieu est inconditionnel...tout comme Sa Haine du mal.",
    hi_title: "बिना शर्त प्रेम घृणा",
    hi_content: "परमेश्वर का प्रेम बिना शर्त है...जैसे कि बुराई के लिए उनकी घृणा है।",
    zh_title: "Wu Tiao Jian De Ai Hen",
    zh_content: "Shang Di de ai shi wu tiao jian de...zheng ru Ta dui e de hen yi yang."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNCONDITIONAL LOVE HATRED"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->UNCONDITIONAL LOVE HATRED"
RETURN t, parent;
```
