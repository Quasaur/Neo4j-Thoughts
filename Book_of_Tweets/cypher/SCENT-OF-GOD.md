---
name: "thought.SCENT OF GOD"
alias: "Thought: Scent Of God"
type: THOUGHT
en_content: "It is Prayer, and Prayer alone, that places the Scent of God on us."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- spirituality
- presence
- scent
- character
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.SCENT OF GOD",
    alias: "Thought: Scent Of God",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'spirituality', 'presence', 'scent', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SCENT OF GOD",
    en_title: "Scent Of God",
    en_content: "It is Prayer, and Prayer alone, that places the Scent of God on us.",
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
WHERE t.name = "thought.SCENT OF GOD" AND c.name = "content.SCENT OF GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SCENT OF GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SCENT OF GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >SCENT OF GOD" }]->(child);
```
