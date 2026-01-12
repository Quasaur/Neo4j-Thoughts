---
name: "thought.NOTHING WITHOUT GOD"
alias: "Thought: Nothing Without God"
type: THOUGHT
en_content: "You are NOTHING without God; You are EVERYTHING to God."
parent: "topic.HUMANITY"
tags:
- humanity
- god
- value
- identity
- dependence
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.NOTHING WITHOUT GOD",
    alias: "Thought: Nothing Without God",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'god', 'value', 'identity', 'dependence'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOTHING WITHOUT GOD",
    en_title: "Nothing Without God",
    en_content: "You are NOTHING without God; You are EVERYTHING to God.",
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
WHERE t.name = "thought.NOTHING WITHOUT GOD" AND c.name = "content.NOTHING WITHOUT GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING WITHOUT GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.NOTHING WITHOUT GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >NOTHING WITHOUT GOD" }]->(child);
```
