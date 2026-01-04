---
name: "thought.MAJORITY OF THREE"
alias: "Thought: Majority Of Three"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- godhead
- life
- death
- goodness
level: 1
neo4j: true
insert: true
---
# Majority Of Three

> [!Thought-en]
> The Godhead is a Majority of Three: Their LIFE far outweighs all Death in the Cosmos...and their GOODNESS overwhelms all Evil!

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jun-2014)
CREATE (t:THOUGHT {
    name: "thought.MAJORITY OF THREE",
    alias: "Thought: Majority Of Three",
    parent: "topic.THE GODHEAD",
    tags: ['godhead', 'life', 'death', 'goodness'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MAJORITY OF THREE",
    en_title: "Majority Of Three",
    en_content: "The Godhead is a Majority of Three: Their LIFE far outweighs all Death in the Cosmos...and their GOODNESS overwhelms all Evil!",
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
WHERE t.name = "thought.MAJORITY OF THREE" AND c.name = "content.MAJORITY OF THREE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MAJORITY OF THREE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MAJORITY OF THREE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >MAJORITY OF THREE" }]->(child);
```