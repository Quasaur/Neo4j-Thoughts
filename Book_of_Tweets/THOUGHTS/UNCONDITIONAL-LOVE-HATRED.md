---
name: "thought.UNCONDITIONAL LOVE HATRED"
alias: "Thought: Unconditional Love Hatred"
type: THOUGHT
en_content: "God's Love is unconditional...as is His Hatred of evil."
parent: "topic.THE GODHEAD"
tags:
- love
- hatred
- evil
- character
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.UNCONDITIONAL LOVE HATRED",
    alias: "Thought: Unconditional Love Hatred",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'hatred', 'evil', 'character', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL LOVE HATRED",
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

MATCH (t:THOUGHT {name: "thought.UNCONDITIONAL LOVE HATRED"})
MATCH (c:CONTENT {name: "content.UNCONDITIONAL LOVE HATRED"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNCONDITIONAL LOVE HATRED" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.UNCONDITIONAL LOVE HATRED"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->UNCONDITIONAL LOVE HATRED" }]->(child);
```
