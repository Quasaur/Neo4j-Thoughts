---
name: "thought.PREEMINENCE OF GOODNESS"
alias: "Thought: Preeminence Of Goodness"
type: THOUGHT
en_content: "That which comes first has the preeminence; righteousness came before sin and goodness came before evil."
parent: "topic.THE GODHEAD"
tags:
- goodness
- righteousness
- eternity
- character
- preeminence
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.PREEMINENCE OF GOODNESS",
    alias: "Thought: Preeminence Of Goodness",
    parent: "topic.THE GODHEAD",
    tags: ['goodness', 'righteousness', 'eternity', 'character', 'preeminence'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.PREEMINENCE OF GOODNESS",
    en_title: "Preeminence Of Goodness",
    en_content: "That which comes first has the preeminence; righteousness came before sin and goodness came before evil.",
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
WHERE t.name = "thought.PREEMINENCE OF GOODNESS" AND c.name = "content.PREEMINENCE OF GOODNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PREEMINENCE OF GOODNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.PREEMINENCE OF GOODNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >PREEMINENCE OF GOODNESS" }]->(child);
```
