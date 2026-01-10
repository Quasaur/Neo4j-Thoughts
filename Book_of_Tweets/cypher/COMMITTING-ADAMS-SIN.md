---
name: "thought.COMMITTING ADAMS SIN"
alias: "Thought: Committing Adams Sin"
type: THOUGHT
en_content: "We continue to commit Adam's sin, and then wonder why we suffer."
parent: "topic.HUMANITY"
tags:
- sin
- adam
- suffering
- humanity
- character
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.COMMITTING ADAMS SIN",
    alias: "Thought: Committing Adams Sin",
    parent: "topic.HUMANITY",
    tags: ['sin', 'adam', 'suffering', 'humanity', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.COMMITTING ADAMS SIN",
    en_title: "Committing Adams Sin",
    en_content: "We continue to commit Adam's sin, and then wonder why we suffer.",
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
WHERE t.name = "thought.COMMITTING ADAMS SIN" AND c.name = "content.COMMITTING ADAMS SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.COMMITTING ADAMS SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.COMMITTING ADAMS SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >COMMITTING ADAMS SIN" }]->(child);
```
