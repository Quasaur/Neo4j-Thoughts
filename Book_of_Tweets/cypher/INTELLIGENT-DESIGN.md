---
name: "thought.INTELLIGENT DESIGN"
alias: "Thought: Intelligent Design"
type: THOUGHT
en_content: "INTELLIGENT DESIGN!"
parent: "topic.CREATION"
tags:
- creation
- design
- intelligence
- truth
- science
level: 2
neo4j: true
insert: true
---
# Intelligent Design

> [!Thought-en]
> INTELLIGENT DESIGN!

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.INTELLIGENT DESIGN",
    alias: "Thought: Intelligent Design",
    parent: "topic.CREATION",
    tags: ['creation', 'design', 'intelligence', 'truth', 'science'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INTELLIGENT DESIGN",
    en_title: "Intelligent Design",
    en_content: "INTELLIGENT DESIGN!",
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
WHERE t.name = "thought.INTELLIGENT DESIGN" AND c.name = "content.INTELLIGENT DESIGN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INTELLIGENT DESIGN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.INTELLIGENT DESIGN"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >INTELLIGENT DESIGN" }]->(child);
```