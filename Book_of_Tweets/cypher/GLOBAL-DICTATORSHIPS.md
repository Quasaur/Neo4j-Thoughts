---
name: "thought.GLOBAL DICTATORSHIPS"
alias: "Thought: Global Dictatorships"
type: THOUGHT
en_content: "2 billion of the 7 billion people on this planet live under dictatorships."
parent: "topic.MORALITY"
tags:
- dictatorship
- society
- justice
- politics
- humanity
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Dec-2011a)
CREATE (t:THOUGHT {
    name: "thought.GLOBAL DICTATORSHIPS",
    alias: "Thought: Global Dictatorships",
    parent: "topic.MORALITY",
    tags: ['dictatorship', 'society', 'justice', 'politics', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GLOBAL DICTATORSHIPS",
    en_title: "Global Dictatorships",
    en_content: "2 billion of the 7 billion people on this planet live under dictatorships.",
    es_title: "Dictaduras Globales",
    es_content: "2 mil millones de los 7 mil millones de personas en este planeta viven bajo dictaduras.",
    fr_title: "Dictatures Mondiales",
    fr_content: "2 milliards des 7 milliards de personnes sur cette planète vivent sous des dictatures.",
    hi_title: "वैश्विक तानाशाही",
    hi_content: "इस ग्रह पर 7 अरब लोगों में से 2 अरब लोग तानाशाही के तहत रहते हैं।",
    zh_title: "Quanqiu Ducai Zhengzhi",
    zh_content: "Zai zhe ge xingqiu shang qi shi yi ren zhong you er shi yi ren shenghuo zai ducai zhengquan xia."
});

MATCH (t:THOUGHT {name: "thought.GLOBAL DICTATORSHIPS"})
MATCH (c:CONTENT {name: "content.GLOBAL DICTATORSHIPS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GLOBAL DICTATORSHIPS" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.GLOBAL DICTATORSHIPS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >GLOBAL DICTATORSHIPS" }]->(child);
```
