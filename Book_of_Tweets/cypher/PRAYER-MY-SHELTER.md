---
name: "thought.PRAYER MY SHELTER"
alias: "Thought: Prayer My Shelter"
type: THOUGHT
en_content: "Prayer is my shelter...my fortress...my stress-free zone...my dessert."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- shelter
- fortress
- stress
- spirituality
level: 2
neo4j: true
insert: true
---
# Prayer My Shelter

> [!Thought-en]
> Prayer is my shelter...my fortress...my stress-free zone...my dessert.

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013d)
CREATE (t:THOUGHT {
    name: "thought.PRAYER MY SHELTER",
    alias: "Thought: Prayer My Shelter",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'shelter', 'fortress', 'stress', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER MY SHELTER",
    en_title: "Prayer My Shelter",
    en_content: "Prayer is my shelter...my fortress...my stress-free zone...my dessert.",
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
WHERE t.name = "thought.PRAYER MY SHELTER" AND c.name = "content.PRAYER MY SHELTER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER MY SHELTER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER MY SHELTER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER MY SHELTER" }]->(child);
```