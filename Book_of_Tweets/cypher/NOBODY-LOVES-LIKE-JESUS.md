---
name: "thought.NOBODY LOVES LIKE JESUS"
alias: "Thought: Nobody Loves Like Jesus"
type: THOUGHT
en_content: "My mother loved me VERY MUCH; but on her finest day she could not take away my sins...nobody loves me like Jesus!"
parent: "topic.THE GODHEAD"
tags:
- love
- jesus
- salvation
- sin
- mother
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Jul-2011)
CREATE (t:THOUGHT {
    name: "thought.NOBODY LOVES LIKE JESUS",
    alias: "Thought: Nobody Loves Like Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'jesus', 'salvation', 'sin', 'mother'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NOBODY LOVES LIKE JESUS",
    en_title: "Nobody Loves Like Jesus",
    en_content: "My mother loved me VERY MUCH; but on her finest day she could not take away my sins...nobody loves me like Jesus!",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOBODY LOVES LIKE JESUS" AND c.name = "content.NOBODY LOVES LIKE JESUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOBODY LOVES LIKE JESUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NOBODY LOVES LIKE JESUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NOBODY LOVES LIKE JESUS" }]->(child);
```
