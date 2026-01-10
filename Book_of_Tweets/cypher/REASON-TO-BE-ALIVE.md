---
name: "thought.REASON TO BE ALIVE"
alias: "Thought: Reason To Be Alive"
type: THOUGHT
en_content: "The only reason we are alive is to find Jesus that He may take away our sin."
parent: "topic.SPIRITUALITY"
tags:
- jesus
- life
- purpose
- sin
- spirituality
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013c)
CREATE (t:THOUGHT {
    name: "thought.REASON TO BE ALIVE",
    alias: "Thought: Reason To Be Alive",
    parent: "topic.SPIRITUALITY",
    tags: ['jesus', 'life', 'purpose', 'sin', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.REASON TO BE ALIVE",
    en_title: "Reason To Be Alive",
    en_content: "The only reason we are alive is to find Jesus that He may take away our sin.",
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
WHERE t.name = "thought.REASON TO BE ALIVE" AND c.name = "content.REASON TO BE ALIVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REASON TO BE ALIVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.REASON TO BE ALIVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >REASON TO BE ALIVE" }]->(child);
```
