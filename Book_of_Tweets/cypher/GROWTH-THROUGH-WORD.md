---
name: "thought.GROWTH THROUGH WORD"
alias: "Thought: Growth Through Word"
type: THOUGHT
en_content: "I cannot grow as a Christian without consistently hearing and speaking God's Word."
parent: "topic.SPIRITUALITY"
tags:
- growth
- word
- christianity
- spirituality
- hearing
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Apr-2012c)
CREATE (t:THOUGHT {
    name: "thought.GROWTH THROUGH WORD",
    alias: "Thought: Growth Through Word",
    parent: "topic.SPIRITUALITY",
    tags: ['growth', 'word', 'christianity', 'spirituality', 'hearing'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GROWTH THROUGH WORD",
    en_title: "Growth Through Word",
    en_content: "I cannot grow as a Christian without consistently hearing and speaking God's Word.",
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
WHERE t.name = "thought.GROWTH THROUGH WORD" AND c.name = "content.GROWTH THROUGH WORD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GROWTH THROUGH WORD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.GROWTH THROUGH WORD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >GROWTH THROUGH WORD" }]->(child);
```
