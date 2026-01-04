---
name: "thought.UNIVERSE INSIDE GOD"
alias: "Thought: Universe Inside God"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- universe
- god
- presence
- infinity
- divinity
level: 1
neo4j: true
insert: true
---
# Universe Inside God

> [!Thought-en]
> You do know that all of us--yeah, the entire Universe--is inside of God, right? Jeremiah 23:24

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013e)
CREATE (t:THOUGHT {
    name: "thought.UNIVERSE INSIDE GOD",
    alias: "Thought: Universe Inside God",
    parent: "topic.THE GODHEAD",
    tags: ['universe', 'god', 'presence', 'infinity', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.UNIVERSE INSIDE GOD",
    en_title: "Universe Inside God",
    en_content: "You do know that all of us--yeah, the entire Universe--is inside of God, right? Jeremiah 23:24",
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
WHERE t.name = "thought.UNIVERSE INSIDE GOD" AND c.name = "content.UNIVERSE INSIDE GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNIVERSE INSIDE GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.UNIVERSE INSIDE GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >UNIVERSE INSIDE GOD" }]->(child);
```