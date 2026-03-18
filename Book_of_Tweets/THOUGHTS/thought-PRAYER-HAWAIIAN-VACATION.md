---
type: THOUGHT
name: "thought.PRAYER HAWAIIAN VACATION"
alias: "Thought: Prayer Hawaiian Vacation"
parent: "topic.SPIRITUALITY"
en_content: "Prayer is my Hawaiian vacation."
tags: ["prayer", "rest", "vacation", "spirituality", "joy"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013b)
CREATE (t:THOUGHT {    name: "thought.PRAYER HAWAIIAN VACATION",
    alias: "Thought: Prayer Hawaiian Vacation",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'rest', 'vacation', 'spirituality', 'joy'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.PRAYER HAWAIIAN VACATION",
    ctype: "THOUGHT",
    en_title: "Prayer Hawaiian Vacation",
    en_content: "Prayer is my Hawaiian vacation.",
    es_title: "Oración Vacaciones en Hawái",
    es_content: "La oración es mis vacaciones en Hawái.",
    fr_title: "Prière Vacances Hawaïennes",
    fr_content: "La prière est mes vacances hawaïennes.",
    hi_title: "प्रार्थना हवाई छुट्टी",
    hi_content: "प्रार्थना मेरी हवाई छुट्टी है।",
    zh_title: "Qídǎo Xiàwēiyí Jiàqī",
    zh_content: "Qídǎo shì wǒ de Xiàwēiyí jiàqī."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRAYER HAWAIIAN VACATION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->PRAYER HAWAIIAN VACATION"
RETURN t, parent;
```
