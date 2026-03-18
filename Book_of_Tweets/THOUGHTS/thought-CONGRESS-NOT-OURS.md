---
type: THOUGHT
name: "thought.CONGRESS NOT OURS"
alias: "Thought: Congress Not Ours"
parent: "topic.MORALITY"
en_content: "The United States Congress no longer belongs to the American People."
tags: ["congress", "america", "people", "morality", "ownership"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Sep-2013a)
CREATE (t:THOUGHT {    name: "thought.CONGRESS NOT OURS",
    alias: "Thought: Congress Not Ours",
    parent: "topic.MORALITY",
    tags: ['congress', 'america', 'people', 'morality', 'ownership'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CONGRESS NOT OURS",
    ctype: "THOUGHT",
    en_title: "Congress Not Ours",
    en_content: "The United States Congress no longer belongs to the American People.",
    es_title: "Congreso No Es Nuestro",
    es_content: "El Congreso de los Estados Unidos ya no pertenece al Pueblo Americano.",
    fr_title: "Congrès Pas Le Nôtre",
    fr_content: "Le Congrès des États-Unis n'appartient plus au peuple américain.",
    hi_title: "कांग्रेस हमारी नहीं",
    hi_content: "संयुक्त राज्य कांग्रेस अब अमेरिकी लोगों की नहीं है।",
    zh_title: "Guóhuì Bù Shǔyú Wǒmen",
    zh_content: "Měiguó Guóhuì yǐjīng bù zài shǔyú Měiguó Rénmín."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CONGRESS NOT OURS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->CONGRESS NOT OURS"
RETURN t, parent;
```
