---
name: "thought.UNSUSTAINABLE WORLD SYSTEM"
alias: "Thought: Unsustainable World System"
type: THOUGHT
en_content: "I believe the Hebrew Scriptures...this world system is unsustainable."
parent: "topic.HUMANITY"
tags:
- humanity
- world
- society
- bible
- truth
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.UNSUSTAINABLE WORLD SYSTEM",
    alias: "Thought: Unsustainable World System",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'world', 'society', 'bible', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNSUSTAINABLE WORLD SYSTEM",
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

MATCH (t:THOUGHT {name: "thought.UNSUSTAINABLE WORLD SYSTEM"})
MATCH (c:CONTENT {name: "content.UNSUSTAINABLE WORLD SYSTEM"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNSUSTAINABLE WORLD SYSTEM" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.UNSUSTAINABLE WORLD SYSTEM"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->UNSUSTAINABLE WORLD SYSTEM" }]->(child);
```
