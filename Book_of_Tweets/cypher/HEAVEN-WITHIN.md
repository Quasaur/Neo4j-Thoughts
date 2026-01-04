---
name: "thought.HEAVEN WITHIN"
alias: "Thought: Heaven Within"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- heaven
- spirituality
- eternity
- transformation
- presence
level: 2
neo4j: true
insert: true
---
# Heaven Within

> [!Thought-en]
> If Heaven isn't in us, then we can't go to Heaven.

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2010b)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN WITHIN",
    alias: "Thought: Heaven Within",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'spirituality', 'eternity', 'transformation', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEAVEN WITHIN",
    en_title: "Heaven Within",
    en_content: "If Heaven isn't in us, then we can't go to Heaven.",
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
WHERE t.name = "thought.HEAVEN WITHIN" AND c.name = "content.HEAVEN WITHIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN WITHIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HEAVEN WITHIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEAVEN WITHIN" }]->(child);
```