---
name: "thought.WRATH OF GOD"
alias: "Thought: Wrath Of God"
type: THOUGHT
en_content: "The worst thing Earth must face is not Antichrist, but The Wrath of God."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- wrath
- god
- judgment
- earth
- sovereignty
level: 5
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.WRATH OF GOD",
    alias: "Thought: Wrath Of God",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['wrath', 'god', 'judgment', 'earth', 'sovereignty'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.WRATH OF GOD",
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

MATCH (t:THOUGHT {name: "thought.WRATH OF GOD"})
MATCH (c:CONTENT {name: "content.WRATH OF GOD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.WRATH OF GOD" }]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.WRATH OF GOD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY->WRATH OF GOD" }]->(child);
```
