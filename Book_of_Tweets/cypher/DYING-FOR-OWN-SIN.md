---
name: "thought.DYING FOR OWN SIN"
alias: "Thought: Dying For Own Sin"
type: THOUGHT
en_content: "I die--not for Adam's sin but for my own; for I was in Adam when he sinned and therefore sinned with him!"
parent: "topic.HUMANITY"
tags:
- sin
- death
- responsibility
- adam
- humanity
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.DYING FOR OWN SIN",
    alias: "Thought: Dying For Own Sin",
    parent: "topic.HUMANITY",
    tags: ['sin', 'death', 'responsibility', 'adam', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DYING FOR OWN SIN",
    en_title: "Dying For Own Sin",
    en_content: "I die--not for Adam's sin but for my own; for I was in Adam when he sinned and therefore sinned with him!",
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
WHERE t.name = "thought.DYING FOR OWN SIN" AND c.name = "content.DYING FOR OWN SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DYING FOR OWN SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.DYING FOR OWN SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >DYING FOR OWN SIN" }]->(child);
```
