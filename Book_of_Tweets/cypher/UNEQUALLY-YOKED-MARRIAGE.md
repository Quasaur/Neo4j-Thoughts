---
name: "thought.UNEQUALLY YOKED MARRIAGE"
alias: "Thought: Unequally Yoked Marriage"
type: THOUGHT
en_content: "The Christian who marries a unbeliever has the Devil for a father-in-law!"
parent: "topic.MORALITY"
tags:
- marriage
- unbeliever
- devil
- morality
- family
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Jun-2012c)
CREATE (t:THOUGHT {
    name: "thought.UNEQUALLY YOKED MARRIAGE",
    alias: "Thought: Unequally Yoked Marriage",
    parent: "topic.MORALITY",
    tags: ['marriage', 'unbeliever', 'devil', 'morality', 'family'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNEQUALLY YOKED MARRIAGE",
    en_title: "Unequally Yoked Marriage",
    en_content: "The Christian who marries a unbeliever has the Devil for a father-in-law!",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNEQUALLY YOKED MARRIAGE" AND c.name = "content.UNEQUALLY YOKED MARRIAGE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNEQUALLY YOKED MARRIAGE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.UNEQUALLY YOKED MARRIAGE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >UNEQUALLY YOKED MARRIAGE" }]->(child);
```
