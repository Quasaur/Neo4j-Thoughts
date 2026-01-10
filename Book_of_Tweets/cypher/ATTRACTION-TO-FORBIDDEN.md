---
name: "thought.ATTRACTION TO FORBIDDEN"
alias: "Thought: Attraction To Forbidden"
type: THOUGHT
en_content: "What attracts us to the forbidden? Sin."
parent: "topic.MORALITY"
tags:
- sin
- attraction
- forbidden
- morality
- temptation
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011d)
CREATE (t:THOUGHT {
    name: "thought.ATTRACTION TO FORBIDDEN",
    alias: "Thought: Attraction To Forbidden",
    parent: "topic.MORALITY",
    tags: ['sin', 'attraction', 'forbidden', 'morality', 'temptation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ATTRACTION TO FORBIDDEN",
    en_title: "Attraction To Forbidden",
    en_content: "What attracts us to the forbidden? Sin.",
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
WHERE t.name = "thought.ATTRACTION TO FORBIDDEN" AND c.name = "content.ATTRACTION TO FORBIDDEN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ATTRACTION TO FORBIDDEN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.ATTRACTION TO FORBIDDEN"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >ATTRACTION TO FORBIDDEN" }]->(child);
```
