---
type: THOUGHT
name: "thought.UNSUSTAINABLE WORLD SYSTEM"
alias: "Thought: Unsustainable World System"
parent: "topic.HUMANITY"
en_content: "I believe the Hebrew Scriptures...this world system is unsustainable."
tags: ["humanity", "world", "society", "bible", "truth"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Feb-2012a)
CREATE (t:THOUGHT {    name: "thought.UNSUSTAINABLE WORLD SYSTEM",
    alias: "Thought: Unsustainable World System",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'world', 'society', 'bible', 'truth'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.UNSUSTAINABLE WORLD SYSTEM",
    ctype: "THOUGHT",
    en_title: "Unsustainable World System",
    en_content: "I believe the Hebrew Scriptures...this world system is unsustainable.",
    es_title: "Sistema Mundial Insostenible",
    es_content: "Creo que las Escrituras Hebreas...este sistema mundial es insostenible.",
    fr_title: "Système Mondial Non Viable",
    fr_content: "Je crois que les Écritures Hébraïques...ce système mondial n'est pas viable.",
    hi_title: "अस्थिर विश्व व्यवस्था",
    hi_content: "मैं मानता हूँ कि हिब्रू धर्मग्रंथ...यह विश्व व्यवस्था अस्थिर है।",
    zh_title: "Bu Ke Chi Xu De Shi Jie Xi Tong",
    zh_content: "Wo Xiang Xin Xi Bo Lai Sheng Jing...Zhe Ge Shi Jie Xi Tong Shi Bu Ke Chi Xu De."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNSUSTAINABLE WORLD SYSTEM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->UNSUSTAINABLE WORLD SYSTEM"
RETURN t, parent;
```
