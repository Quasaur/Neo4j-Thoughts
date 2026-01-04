---
name: "thought.PRAYER AS RELIEF"
alias: "Thought: Prayer As Relief"
type: THOUGHT
en_content: "Prayer is my relief."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- relief
- pain
- spirituality
- comfort
level: 2
neo4j: true
insert: true
---
# Prayer As Relief

> [!Thought-en]
> Prayer is my relief.

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013c)
CREATE (t:THOUGHT {
    name: "thought.PRAYER AS RELIEF",
    alias: "Thought: Prayer As Relief",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'relief', 'pain', 'spirituality', 'comfort'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER AS RELIEF",
    en_title: "Prayer As Relief",
    en_content: "Prayer is my relief.",
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
WHERE t.name = "thought.PRAYER AS RELIEF" AND c.name = "content.PRAYER AS RELIEF"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER AS RELIEF" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER AS RELIEF"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER AS RELIEF" }]->(child);
```