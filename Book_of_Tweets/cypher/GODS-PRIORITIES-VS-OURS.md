---
name: "thought.GODS PRIORITIES VS OURS"
alias: "Thought: Gods Priorities Vs Ours"
type: THOUGHT
en_content: "The things that are important to God are rarely important to us."
parent: "topic.THE GODHEAD"
tags:
- priorities
- importance
- god
- humanity
level: 1
neo4j: true
insert: true
---
# Gods Priorities Vs Ours

> [!Thought-en]
> The things that are important to God are rarely important to us.

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.GODS PRIORITIES VS OURS",
    alias: "Thought: Gods Priorities Vs Ours",
    parent: "topic.THE GODHEAD",
    tags: ['priorities', 'importance', 'god', 'humanity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS PRIORITIES VS OURS",
    en_title: "Gods Priorities Vs Ours",
    en_content: "The things that are important to God are rarely important to us.",
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
WHERE t.name = "thought.GODS PRIORITIES VS OURS" AND c.name = "content.GODS PRIORITIES VS OURS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS PRIORITIES VS OURS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS PRIORITIES VS OURS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS PRIORITIES VS OURS" }]->(child);
```