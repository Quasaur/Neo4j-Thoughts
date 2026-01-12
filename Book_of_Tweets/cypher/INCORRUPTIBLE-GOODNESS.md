---
name: "thought.INCORRUPTIBLE GOODNESS"
alias: "Thought: Incorruptible Goodness"
type: THOUGHT
en_content: "Good is greater than evil; for the Fountain of All Good (God) has never been nor can ever be corrupted by evil."
parent: "topic.THE GODHEAD"
tags:
- goodness
- god
- corruption
- divinity
- character
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012c)
CREATE (t:THOUGHT {
    name: "thought.INCORRUPTIBLE GOODNESS",
    alias: "Thought: Incorruptible Goodness",
    parent: "topic.THE GODHEAD",
    tags: ['goodness', 'god', 'corruption', 'divinity', 'character'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.INCORRUPTIBLE GOODNESS",
    en_title: "Incorruptible Goodness",
    en_content: "Good is greater than evil; for the Fountain of All Good (God) has never been nor can ever be corrupted by evil.",
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
WHERE t.name = "thought.INCORRUPTIBLE GOODNESS" AND c.name = "content.INCORRUPTIBLE GOODNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INCORRUPTIBLE GOODNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.INCORRUPTIBLE GOODNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >INCORRUPTIBLE GOODNESS" }]->(child);
```
