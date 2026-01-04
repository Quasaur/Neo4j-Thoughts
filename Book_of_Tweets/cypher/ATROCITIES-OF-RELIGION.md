---
name: "thought.ATROCITIES OF RELIGION"
alias: "Thought: Atrocities Of Religion"
type: THOUGHT
en_content: "It's amazing what atrocities religion will allow."
parent: "topic.RELIGION"
tags:
- religion
- atrocity
- character
- failure
- judgment
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Mar-2012b)
CREATE (t:THOUGHT {
    name: "thought.ATROCITIES OF RELIGION",
    alias: "Thought: Atrocities Of Religion",
    parent: "topic.RELIGION",
    tags: ['religion', 'atrocity', 'character', 'failure', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ATROCITIES OF RELIGION",
    en_title: "Atrocities Of Religion",
    en_content: "It's amazing what atrocities religion will allow.",
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
WHERE t.name = "thought.ATROCITIES OF RELIGION" AND c.name = "content.ATROCITIES OF RELIGION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ATROCITIES OF RELIGION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.ATROCITIES OF RELIGION"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >ATROCITIES OF RELIGION" }]->(child);
```
