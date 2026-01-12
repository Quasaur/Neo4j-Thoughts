---
name: "thought.LIFE IN PRAYER"
alias: "Thought: Life In Prayer"
type: THOUGHT
en_content: "There is no life outside of Prayer."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- life
- spirituality
- essence
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Feb-2014)
CREATE (t:THOUGHT {
    name: "thought.LIFE IN PRAYER",
    alias: "Thought: Life In Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'life', 'spirituality', 'essence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIFE IN PRAYER",
    en_title: "Life In Prayer",
    en_content: "There is no life outside of Prayer.",
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
WHERE t.name = "thought.LIFE IN PRAYER" AND c.name = "content.LIFE IN PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIFE IN PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.LIFE IN PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >LIFE IN PRAYER" }]->(child);
```
