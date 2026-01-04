---
name: "thought.FAITH IN EVOLUTION"
alias: "Thought: Faith In Evolution"
type: THOUGHT
parent: "topic.FAITH"
tags:
- faith
- evolution
- design
- creation
- science
level: 4
neo4j: true
insert: true
---
# Faith In Evolution

> [!Thought-en]
> Evolution requires FAR MORE FAITH than Intelligent Design.

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Nov-2010d)
CREATE (t:THOUGHT {
    name: "thought.FAITH IN EVOLUTION",
    alias: "Thought: Faith In Evolution",
    parent: "topic.FAITH",
    tags: ['faith', 'evolution', 'design', 'creation', 'science'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH IN EVOLUTION",
    en_title: "Faith In Evolution",
    en_content: "Evolution requires FAR MORE FAITH than Intelligent Design.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FAITH IN EVOLUTION" AND c.name = "content.FAITH IN EVOLUTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAITH IN EVOLUTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.FAITH IN EVOLUTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >FAITH IN EVOLUTION" }]->(child);
```