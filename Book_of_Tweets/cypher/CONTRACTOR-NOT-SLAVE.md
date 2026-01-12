---
name: "thought.CONTRACTOR NOT SLAVE"
alias: "Thought: Contractor Not Slave"
type: THOUGHT
en_content: "A contractor is NOT a slave."
parent: "topic.MORALITY"
tags:
- work
- freedom
- slave
- morality
- society
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.CONTRACTOR NOT SLAVE",
    alias: "Thought: Contractor Not Slave",
    parent: "topic.MORALITY",
    tags: ['work', 'freedom', 'slave', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONTRACTOR NOT SLAVE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CONTRACTOR NOT SLAVE" AND c.name = "content.CONTRACTOR NOT SLAVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CONTRACTOR NOT SLAVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CONTRACTOR NOT SLAVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CONTRACTOR NOT SLAVE" }]->(child);
```
