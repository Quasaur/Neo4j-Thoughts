---
name: "thought.QUESTIONING GODS EXISTENCE"
alias: "Thought: Questioning Gods Existence"
type: THOUGHT
en_content: "In a perverse generation they question God's Existence, when it's their existence and survival that has a question mark behind them."
parent: "topic.PHILOSOPHY"
tags:
- existence
- god
- survival
- skepticism
- philosophy
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Aug-2012b)
CREATE (t:THOUGHT {
    name: "thought.QUESTIONING GODS EXISTENCE",
    alias: "Thought: Questioning Gods Existence",
    parent: "topic.PHILOSOPHY",
    tags: ['existence', 'god', 'survival', 'skepticism', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.QUESTIONING GODS EXISTENCE",
    en_title: "Questioning Gods Existence",
    en_content: "In a perverse generation they question God's Existence, when it's their existence and survival that has a question mark behind them.",
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
WHERE t.name = "thought.QUESTIONING GODS EXISTENCE" AND c.name = "content.QUESTIONING GODS EXISTENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.QUESTIONING GODS EXISTENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.QUESTIONING GODS EXISTENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >QUESTIONING GODS EXISTENCE" }]->(child);
```
