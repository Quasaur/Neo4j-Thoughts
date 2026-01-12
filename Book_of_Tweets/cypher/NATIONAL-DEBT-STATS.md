---
name: "thought.NATIONAL DEBT STATS"
alias: "Thought: National Debt Stats"
type: THOUGHT
en_content: "The National Debt: $16 TRILLION...that's $30 million every second for a year!!!"
parent: "topic.MORALITY"
tags:
- debt
- economics
- morality
- society
- judgment
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.NATIONAL DEBT STATS",
    alias: "Thought: National Debt Stats",
    parent: "topic.MORALITY",
    tags: ['debt', 'economics', 'morality', 'society', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NATIONAL DEBT STATS",
    en_title: "National Debt Stats",
    en_content: "The National Debt: $16 TRILLION...that's $30 million every second for a year!!!",
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
WHERE t.name = "thought.NATIONAL DEBT STATS" AND c.name = "content.NATIONAL DEBT STATS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NATIONAL DEBT STATS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.NATIONAL DEBT STATS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >NATIONAL DEBT STATS" }]->(child);
```
