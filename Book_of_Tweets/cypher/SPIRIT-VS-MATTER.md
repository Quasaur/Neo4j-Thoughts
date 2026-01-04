---
name: "thought.SPIRIT VS MATTER"
alias: "Thought: Spirit Vs Matter"
type: THOUGHT
en_content: "SPIRIT is far older, stronger and eternally more powerful than matter."
parent: "topic.PHILOSOPHY"
tags:
- spirit
- matter
- eternity
- philosophy
- power
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2011d)
CREATE (t:THOUGHT {
    name: "thought.SPIRIT VS MATTER",
    alias: "Thought: Spirit Vs Matter",
    parent: "topic.PHILOSOPHY",
    tags: ['spirit', 'matter', 'eternity', 'philosophy', 'power'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SPIRIT VS MATTER",
    en_title: "Spirit Vs Matter",
    en_content: "SPIRIT is far older, stronger and eternally more powerful than matter.",
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
WHERE t.name = "thought.SPIRIT VS MATTER" AND c.name = "content.SPIRIT VS MATTER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPIRIT VS MATTER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.SPIRIT VS MATTER"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >SPIRIT VS MATTER" }]->(child);
```
