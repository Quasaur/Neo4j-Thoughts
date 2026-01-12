---
name: "thought.SIN TASTES GOOD"
alias: "Thought: Sin Tastes Good"
type: THOUGHT
en_content: "Sin is killing us; but at least it tastes good!"
parent: "topic.MORALITY"
tags:
- sin
- taste
- irony
- morality
- character
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Nov-2013b)
CREATE (t:THOUGHT {
    name: "thought.SIN TASTES GOOD",
    alias: "Thought: Sin Tastes Good",
    parent: "topic.MORALITY",
    tags: ['sin', 'taste', 'irony', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIN TASTES GOOD",
    en_title: "Sin Tastes Good",
    en_content: "Sin is killing us; but at least it tastes good!",
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
WHERE t.name = "thought.SIN TASTES GOOD" AND c.name = "content.SIN TASTES GOOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIN TASTES GOOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SIN TASTES GOOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SIN TASTES GOOD" }]->(child);
```
