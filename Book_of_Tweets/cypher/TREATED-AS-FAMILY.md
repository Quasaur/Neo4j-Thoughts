---
name: "thought.TREATED AS FAMILY"
alias: "Thought: Treated As Family"
type: THOUGHT
parent: "topic.GRACE"
tags:
- family
- grace
- identity
- god
- love
level: 3
neo4j: true
insert: true
---
# Treated As Family

> [!Thought-en]
> God has always treated me as family, whether I deserved it or not.

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-May-2012)
CREATE (t:THOUGHT {
    name: "thought.TREATED AS FAMILY",
    alias: "Thought: Treated As Family",
    parent: "topic.GRACE",
    tags: ['family', 'grace', 'identity', 'god', 'love'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TREATED AS FAMILY",
    en_title: "Treated As Family",
    en_content: "God has always treated me as family, whether I deserved it or not.",
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
WHERE t.name = "thought.TREATED AS FAMILY" AND c.name = "content.TREATED AS FAMILY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TREATED AS FAMILY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.TREATED AS FAMILY"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >TREATED AS FAMILY" }]->(child);
```