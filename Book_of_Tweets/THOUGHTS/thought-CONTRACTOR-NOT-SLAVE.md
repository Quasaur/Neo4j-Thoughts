---
type: THOUGHT
name: "thought.CONTRACTOR NOT SLAVE"
alias: "Thought: Contractor Not Slave"
parent: "topic.MORALITY"
en_content: "A contractor is NOT a slave."
tags: ["work", "freedom", "slave", "morality", "society"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2012)
CREATE (t:THOUGHT {    name: "thought.CONTRACTOR NOT SLAVE",
    alias: "Thought: Contractor Not Slave",
    parent: "topic.MORALITY",
    tags: ['work', 'freedom', 'slave', 'morality', 'society'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CONTRACTOR NOT SLAVE",
    ctype: "THOUGHT",
    en_title: "Contractor Not Slave",
    en_content: "A contractor is NOT a slave.",
    es_title: "Contratista No Esclavo",
    es_content: "Un contratista NO es un esclavo.",
    fr_title: "Entrepreneur Pas Esclave",
    fr_content: "Un entrepreneur n'est PAS un esclave.",
    hi_title: "ठेकेदार गुलाम नहीं",
    hi_content: "एक ठेकेदार गुलाम नहीं है।",
    zh_title: "Chéng Bāo Shāng Bù Shì Núlì",
    zh_content: "Chéng bāo shāng bù shì núlì."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CONTRACTOR NOT SLAVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->CONTRACTOR NOT SLAVE"
RETURN t, parent;
```
