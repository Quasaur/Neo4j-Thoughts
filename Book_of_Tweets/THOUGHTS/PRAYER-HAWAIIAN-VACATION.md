---
name: "thought.PRAYER HAWAIIAN VACATION"
alias: "Thought: Prayer Hawaiian Vacation"
type: THOUGHT
en_content: "Prayer is my Hawaiian vacation."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- rest
- vacation
- spirituality
- joy
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013b)
CREATE (t:THOUGHT {
    name: "thought.PRAYER HAWAIIAN VACATION",
    alias: "Thought: Prayer Hawaiian Vacation",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'rest', 'vacation', 'spirituality', 'joy'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER HAWAIIAN VACATION",
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

MATCH (t:THOUGHT {name: "thought.PRAYER HAWAIIAN VACATION"})
MATCH (c:CONTENT {name: "content.PRAYER HAWAIIAN VACATION"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER HAWAIIAN VACATION" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.PRAYER HAWAIIAN VACATION"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->PRAYER HAWAIIAN VACATION" }]->(child);
```
