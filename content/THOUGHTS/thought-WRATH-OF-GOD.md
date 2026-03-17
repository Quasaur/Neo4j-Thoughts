---
type: THOUGHT
name: "thought.WRATH OF GOD"
alias: "Thought: Wrath Of God"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "The worst thing Earth must face is not Antichrist, but The Wrath of God."
tags: ["wrath", "god", "judgment", "earth", "sovereignty"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.WRATH OF GOD",
    alias: "Thought: Wrath Of God",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['wrath', 'god', 'judgment', 'earth', 'sovereignty'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.WRATH OF GOD",
    ctype: "THOUGHT",
    en_title: "Wrath Of God",
    en_content: "The worst thing Earth must face is not Antichrist, but The Wrath of God.",
    es_title: "La Ira de Dios",
    es_content: "Lo peor que debe enfrentar la Tierra no es el Anticristo, sino La Ira de Dios.",
    fr_title: "La Colère de Dieu",
    fr_content: "La pire chose que la Terre doit affronter n'est pas l'Antéchrist, mais La Colère de Dieu.",
    hi_title: "परमेश्वर का क्रोध",
    hi_content: "पृथ्वी को जिस सबसे बुरी चीज़ का सामना करना है वह मसीह विरोधी नहीं, बल्कि परमेश्वर का क्रोध है।",
    zh_title: "Shén de Fènnù",
    zh_content: "Dìqiú bìxū miànduì de zuì zāogāo de shìqíng bùshì Dí Jīdū, ér shì Shén de Fènnù."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WRATH OF GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->WRATH OF GOD"
RETURN t, parent;
```
