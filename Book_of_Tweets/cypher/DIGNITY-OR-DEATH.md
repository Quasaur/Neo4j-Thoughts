---
name: "thought.DIGNITY OR DEATH"
alias: "Thought: Dignity Or Death"
type: THOUGHT
en_content: "Give me DIGNITY or give me death!"
parent: "topic.HUMANITY"
tags:
- dignity
- freedom
- humanity
- character
- sacrifice
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.DIGNITY OR DEATH",
    alias: "Thought: Dignity Or Death",
    parent: "topic.HUMANITY",
    tags: ['dignity', 'freedom', 'humanity', 'character', 'sacrifice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DIGNITY OR DEATH",
    en_title: "Dignity Or Death",
    en_content: "Give me DIGNITY or give me death!",
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
WHERE t.name = "thought.DIGNITY OR DEATH" AND c.name = "content.DIGNITY OR DEATH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DIGNITY OR DEATH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.DIGNITY OR DEATH"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >DIGNITY OR DEATH" }]->(child);
```
