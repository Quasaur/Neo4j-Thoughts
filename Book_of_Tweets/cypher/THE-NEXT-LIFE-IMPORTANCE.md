---
name: "thought.THE NEXT LIFE IMPORTANCE"
alias: "Thought: The Next Life Importance"
type: THOUGHT
en_content: "There's NOTHING in this life that's more important than The Next Life!"
parent: "topic.SPIRITUALITY"
tags:
- life
- eternity
- importance
- spirituality
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-May-2014)
CREATE (t:THOUGHT {
    name: "thought.THE NEXT LIFE IMPORTANCE",
    alias: "Thought: The Next Life Importance",
    parent: "topic.SPIRITUALITY",
    tags: ['life', 'eternity', 'importance', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE NEXT LIFE IMPORTANCE",
    en_title: "The Next Life Importance",
    en_content: "There's NOTHING in this life that's more important than The Next Life!",
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
WHERE t.name = "thought.THE NEXT LIFE IMPORTANCE" AND c.name = "content.THE NEXT LIFE IMPORTANCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE NEXT LIFE IMPORTANCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.THE NEXT LIFE IMPORTANCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >THE NEXT LIFE IMPORTANCE" }]->(child);
```
