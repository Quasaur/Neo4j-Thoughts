---
name: "thought.FALSE RELIGION TWIN"
alias: "Thought: False Religion Twin"
type: THOUGHT
en_content: "The Twin of Wickedness is False Religion."
parent: "topic.RELIGION"
tags:
- religion
- wickedness
- evil
- truth
- character
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.FALSE RELIGION TWIN",
    alias: "Thought: False Religion Twin",
    parent: "topic.RELIGION",
    tags: ['religion', 'wickedness', 'evil', 'truth', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FALSE RELIGION TWIN",
    en_title: "False Religion Twin",
    en_content: "The Twin of Wickedness is False Religion.",
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
WHERE t.name = "thought.FALSE RELIGION TWIN" AND c.name = "content.FALSE RELIGION TWIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FALSE RELIGION TWIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.FALSE RELIGION TWIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >FALSE RELIGION TWIN" }]->(child);
```
