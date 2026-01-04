---
name: "thought.THREE TYPES OF HUMANITY"
alias: "Thought: Three Types Of Humanity"
type: THOUGHT
en_content: "Humanity: (1) those who place God 1st; (2) those who give God a priority other than 1st; (3) those who give God no priority at all."
parent: "topic.HUMANITY"
tags:
- humanity
- priority
- god
- world
- classification
level: 3
neo4j: true
insert: true
---
# Three Types Of Humanity

> [!Thought-en]
> Humanity: (1) those who place God 1st; (2) those who give God a priority other than 1st; (3) those who give God no priority at all.

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.THREE TYPES OF HUMANITY",
    alias: "Thought: Three Types Of Humanity",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'priority', 'god', 'world', 'classification'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.THREE TYPES OF HUMANITY",
    en_title: "Three Types Of Humanity",
    en_content: "Humanity: (1) those who place God 1st; (2) those who give God a priority other than 1st; (3) those who give God no priority at all.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THREE TYPES OF HUMANITY" AND c.name = "content.THREE TYPES OF HUMANITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.THREE TYPES OF HUMANITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.THREE TYPES OF HUMANITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >THREE TYPES OF HUMANITY" }]->(child);
```