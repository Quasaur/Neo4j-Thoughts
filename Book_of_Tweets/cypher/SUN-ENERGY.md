---
name: "thought.SUN ENERGY"
alias: "Thought: Sun Energy"
type: THOUGHT
en_content: "The Sun releases 5 million tons of matter per second...God is Great!"
parent: "topic.CREATION"
tags:
- creation
- sun
- power
- matter
- majesty
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2011c)
CREATE (t:THOUGHT {
    name: "thought.SUN ENERGY",
    alias: "Thought: Sun Energy",
    parent: "topic.CREATION",
    tags: ['creation', 'sun', 'power', 'matter', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SUN ENERGY",
    en_title: "Sun Energy",
    en_content: "The Sun releases 5 million tons of matter per second...God is Great!",
    es_title: "Energía Solar",
    es_content: "El Sol libera 5 millones de toneladas de materia por segundo...¡Dios es Grande!",
    fr_title: "Énergie Solaire",
    fr_content: "Le Soleil libère 5 millions de tonnes de matière par seconde...Dieu est Grand !",
    hi_title: "सूर्य ऊर्जा",
    hi_content: "सूर्य प्रति सेकंड 5 मिलियन टन पदार्थ छोड़ता है...भगवान महान है!",
    zh_title: "Tàiyáng Néngliàng",
    zh_content: "Tàiyáng měi miǎo shìfàng wǔbǎi wàn dūn wùzhì...Shàngdì shì wěidà de!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SUN ENERGY" AND c.name = "content.SUN ENERGY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SUN ENERGY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.SUN ENERGY"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >SUN ENERGY" }]->(child);
```
