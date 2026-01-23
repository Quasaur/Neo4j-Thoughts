---
name: "thought.PRAYER MY SHELTER"
alias: "Thought: Prayer My Shelter"
type: THOUGHT
en_content: "Prayer is my shelter...my fortress...my stress-free zone...my dessert."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- shelter
- fortress
- stress
- spirituality
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013d)
CREATE (t:THOUGHT {
    name: "thought.PRAYER MY SHELTER",
    alias: "Thought: Prayer My Shelter",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'shelter', 'fortress', 'stress', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER MY SHELTER",
    en_title: "Prayer My Shelter",
    en_content: "Prayer is my shelter...my fortress...my stress-free zone...my dessert.",
    es_title: "La Oración: Mi Refugio",
    es_content: "La oración es mi refugio... mi fortaleza... mi zona libre de estrés... mi postre.",
    fr_title: "La Prière : Mon Abri",
    fr_content: "La prière est mon abri... ma forteresse... ma zone sans stress... mon dessert.",
    hi_title: "प्रार्थना मेरी शरण",
    hi_content: "प्रार्थना मेरी शरण है... मेरा किला... मेरा तनाव-मुक्त क्षेत्र... मेरी मिठाई।",
    zh_title: "Qí dǎo shì wǒ de bì hù suǒ 祈祷是我的庇护所",
    zh_content: "Qí dǎo shì wǒ de bì hù suǒ... wǒ de bǎolěi... wǒ de wú yālì qū... wǒ de tiándiǎn. 祈祷是我的庇护所...我的堡垒...我的无压力区...我的甜点。"
});

MATCH (t:THOUGHT {name: "thought.PRAYER MY SHELTER"})
MATCH (c:CONTENT {name: "content.PRAYER MY SHELTER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER MY SHELTER" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.PRAYER MY SHELTER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER MY SHELTER" }]->(child);
```
