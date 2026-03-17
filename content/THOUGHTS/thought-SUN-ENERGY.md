---
type: THOUGHT
name: "thought.SUN ENERGY"
alias: "Thought: Sun Energy"
parent: "topic.ASTROPHYSICS"
en_content: "The Sun releases 5 million tons of matter per second...God is Great!"
tags: ["creation", "sun", "power", "matter", "majesty"]
ptopic: "[[topic-ASTROPHYSICS]]"
level: 5
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SUN ENERGY",
    alias: "Thought: Sun Energy",
    parent: "topic.ASTROPHYSICS",
    tags: ['creation', 'sun', 'power', 'matter', 'majesty'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.SUN ENERGY",
    ctype: "THOUGHT",
    en_title: "Thought: Sun Energy",
    en_content: "The Sun releases 5 million tons of matter per second...God is Great!",
    es_title: "Pensamiento: Energía solar",
    es_content: "El Sol libera 5 millones de toneladas de materia por segundo...¡Dios es Grande!",
    fr_title: "Pensée : Énergie solaire",
    fr_content: "Le Soleil libère 5 millions de tonnes de matière par seconde...Dieu est Grand !",
    hi_title: "विचार: सूर्य ऊर्जाा",
    hi_content: "सूर्य प्रति सेकंड 5 मिलियन टन पदार्थ छोड़ता है...भगवान महान है!",
    zh_title: "sī xiǎng : tài yáng néng",
    zh_content: "Tàiyáng měi miǎo shìfàng wǔbǎi wàn dūn wùzhì...Shàngdì shì wěidà de!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SUN ENERGY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "tooic.ASTROPHYSICS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ASTROPHYSICS->SUN ENERGY"
RETURN t, parent;
```
