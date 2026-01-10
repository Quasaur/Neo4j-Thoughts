---
name: "thought.MEN SHAVING CHILDREN"
alias: "Thought: Men Shaving Children"
type: THOUGHT
en_content: "It may be that women like us men to shave that they may treat us like children."
parent: "topic.HUMANITY"
tags:
- men
- women
- shaving
- children
- humor
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Sep-2013)
CREATE (t:THOUGHT {
    name: "thought.MEN SHAVING CHILDREN",
    alias: "Thought: Men Shaving Children",
    parent: "topic.HUMANITY",
    tags: ['men', 'women', 'shaving', 'children', 'humor'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MEN SHAVING CHILDREN",
    en_title: "Men Shaving Children",
    en_content: "It may be that women like us men to shave that they may treat us like children.",
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
WHERE t.name = "thought.MEN SHAVING CHILDREN" AND c.name = "content.MEN SHAVING CHILDREN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MEN SHAVING CHILDREN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.MEN SHAVING CHILDREN"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >MEN SHAVING CHILDREN" }]->(child);
```
