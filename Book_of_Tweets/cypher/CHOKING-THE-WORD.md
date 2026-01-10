---
name: "thought.CHOKING THE WORD"
alias: "Thought: Choking The Word"
type: THOUGHT
en_content: "Like weeds choke a flower, the cares of this life and the deceitfulness of riches choke the Word of God in my heart, and make it unfruitful."
parent: "topic.FAITH"
tags:
- faith
- word
- riches
- temptation
- growth
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.CHOKING THE WORD",
    alias: "Thought: Choking The Word",
    parent: "topic.FAITH",
    tags: ['faith', 'word', 'riches', 'temptation', 'growth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHOKING THE WORD",
    en_title: "Choking The Word",
    en_content: "Like weeds choke a flower, the cares of this life and the deceitfulness of riches choke the Word of God in my heart, and make it unfruitful.",
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
WHERE t.name = "thought.CHOKING THE WORD" AND c.name = "content.CHOKING THE WORD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHOKING THE WORD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.CHOKING THE WORD"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >CHOKING THE WORD" }]->(child);
```
