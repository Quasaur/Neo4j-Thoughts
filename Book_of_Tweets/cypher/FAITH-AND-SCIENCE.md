---
name: "thought.FAITH AND SCIENCE"
alias: "Thought: Faith And Science"
type: THOUGHT
en_content: "The Standard Model (Inflation, Dark Matter/Energy/Flow) takes more FAITH than to believe God holds the universe together by His Word."
parent: "topic.FAITH"
tags:
- faith
- science
- standard_model
- creation
- belief
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2010)
CREATE (t:THOUGHT {
    name: "thought.FAITH AND SCIENCE",
    alias: "Thought: Faith And Science",
    parent: "topic.FAITH",
    tags: ['faith', 'science', 'standard_model', 'creation', 'belief'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH AND SCIENCE",
    en_title: "Faith And Science",
    en_content: "The Standard Model (Inflation, Dark Matter/Energy/Flow) takes more FAITH than to believe God holds the universe together by His Word.",
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
WHERE t.name = "thought.FAITH AND SCIENCE" AND c.name = "content.FAITH AND SCIENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAITH AND SCIENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.FAITH AND SCIENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >FAITH AND SCIENCE" }]->(child);
```
