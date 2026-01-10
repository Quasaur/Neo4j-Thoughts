---
name: "thought.SIN MAKES IDIOTS"
alias: "Thought: Sin Makes Idiots"
type: THOUGHT
en_content: "Sin makes idiots of us all; Christ came to take away the sins of the body (disease) as well as the sins of the soul!"
parent: "topic.GRACE"
tags:
- sin
- christ
- healing
- body
- soul
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013e)
CREATE (t:THOUGHT {
    name: "thought.SIN MAKES IDIOTS",
    alias: "Thought: Sin Makes Idiots",
    parent: "topic.GRACE",
    tags: ['sin', 'christ', 'healing', 'body', 'soul'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIN MAKES IDIOTS",
    en_title: "Sin Makes Idiots",
    en_content: "Sin makes idiots of us all; Christ came to take away the sins of the body (disease) as well as the sins of the soul!",
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
WHERE t.name = "thought.SIN MAKES IDIOTS" AND c.name = "content.SIN MAKES IDIOTS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIN MAKES IDIOTS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.SIN MAKES IDIOTS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >SIN MAKES IDIOTS" }]->(child);
```
