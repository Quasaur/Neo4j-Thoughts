---
name: "thought.CONGRESS NOT OURS"
alias: "Thought: Congress Not Ours"
type: THOUGHT
en_content: "The United States Congress no longer belongs to the American People."
parent: "topic.MORALITY"
tags:
- congress
- america
- people
- morality
- ownership
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.CONGRESS NOT OURS",
    alias: "Thought: Congress Not Ours",
    parent: "topic.MORALITY",
    tags: ['congress', 'america', 'people', 'morality', 'ownership'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONGRESS NOT OURS",
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

MATCH (t:THOUGHT {name: "thought.CONGRESS NOT OURS"})
MATCH (c:CONTENT {name: "content.CONGRESS NOT OURS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CONGRESS NOT OURS" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.CONGRESS NOT OURS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->CONGRESS NOT OURS" }]->(child);
```
