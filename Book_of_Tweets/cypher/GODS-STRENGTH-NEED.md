---
name: "thought.GODS STRENGTH NEED"
alias: "Thought: Gods Strength Need"
type: THOUGHT
en_content: "\"I don't need your strength...you need Mine.\" -- God"
parent: "topic.SPIRITUALITY"
tags:
- strength
- dependence
- god
- spirituality
- power
level: 2
neo4j: true
insert: true
---
# Gods Strength Need

> [!Thought-en]
> "I don't need your strength...you need Mine." -- God

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Dec-2011a)
CREATE (t:THOUGHT {
    name: "thought.GODS STRENGTH NEED",
    alias: "Thought: Gods Strength Need",
    parent: "topic.SPIRITUALITY",
    tags: ['strength', 'dependence', 'god', 'spirituality', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GODS STRENGTH NEED",
    en_title: "Gods Strength Need",
    en_content: "\"I don't need your strength...you need Mine.\" -- God",
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
WHERE t.name = "thought.GODS STRENGTH NEED" AND c.name = "content.GODS STRENGTH NEED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS STRENGTH NEED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.GODS STRENGTH NEED"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >GODS STRENGTH NEED" }]->(child);
```