---
name: "thought.HUMILITY IN PRAYER"
alias: "Thought: Humility In Prayer"
type: THOUGHT
en_content: "Prayer needs no Humility to be spoken, but no prayer is heard without it."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- humility
- spirituality
- connection
- truth
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-May-2012)
CREATE (t:THOUGHT {
    name: "thought.HUMILITY IN PRAYER",
    alias: "Thought: Humility In Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'humility', 'spirituality', 'connection', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HUMILITY IN PRAYER",
    en_title: "Humility In Prayer",
    en_content: "Prayer needs no Humility to be spoken, but no prayer is heard without it.",
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
WHERE t.name = "thought.HUMILITY IN PRAYER" AND c.name = "content.HUMILITY IN PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HUMILITY IN PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HUMILITY IN PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HUMILITY IN PRAYER" }]->(child);
```
