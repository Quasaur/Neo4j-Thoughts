---
name: "thought.LOVE SEVERING SIN"
alias: "Thought: Love Severing Sin"
type: THOUGHT
en_content: "Only Love can separate sinners from their sins."
parent: "topic.GRACE"
tags:
- love
- sin
- separation
- grace
- transformation
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Jan-2012b)
CREATE (t:THOUGHT {
    name: "thought.LOVE SEVERING SIN",
    alias: "Thought: Love Severing Sin",
    parent: "topic.GRACE",
    tags: ['love', 'sin', 'separation', 'grace', 'transformation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LOVE SEVERING SIN",
    en_title: "Love Severing Sin",
    en_content: "Only Love can separate sinners from their sins.",
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
WHERE t.name = "thought.LOVE SEVERING SIN" AND c.name = "content.LOVE SEVERING SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVE SEVERING SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.LOVE SEVERING SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LOVE SEVERING SIN" }]->(child);
```
