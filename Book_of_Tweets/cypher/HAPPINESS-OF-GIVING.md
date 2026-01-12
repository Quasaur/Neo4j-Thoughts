---
name: "thought.HAPPINESS OF GIVING"
alias: "Thought: Happiness Of Giving"
type: THOUGHT
en_content: "God is happier than everyone else because He gives more than anyone else."
parent: "topic.THE GODHEAD"
tags:
- giving
- happiness
- god
- character
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Nov-2011b)
CREATE (t:THOUGHT {
    name: "thought.HAPPINESS OF GIVING",
    alias: "Thought: Happiness Of Giving",
    parent: "topic.THE GODHEAD",
    tags: ['giving', 'happiness', 'god', 'character', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.HAPPINESS OF GIVING",
    en_title: "Happiness Of Giving",
    en_content: "God is happier than everyone else because He gives more than anyone else.",
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
WHERE t.name = "thought.HAPPINESS OF GIVING" AND c.name = "content.HAPPINESS OF GIVING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HAPPINESS OF GIVING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.HAPPINESS OF GIVING"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >HAPPINESS OF GIVING" }]->(child);
```
