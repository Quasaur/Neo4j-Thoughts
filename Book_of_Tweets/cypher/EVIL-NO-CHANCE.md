---
name: "thought.EVIL NO CHANCE"
alias: "Thought: Evil No Chance"
type: THOUGHT
en_content: "Look at God. Evil never had a chance!"
parent: "topic.THE GODHEAD"
tags:
- god
- evil
- victory
- majesty
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.EVIL NO CHANCE",
    alias: "Thought: Evil No Chance",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'evil', 'victory', 'majesty', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.EVIL NO CHANCE",
    en_title: "Evil No Chance",
    en_content: "Look at God. Evil never had a chance!",
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
WHERE t.name = "thought.EVIL NO CHANCE" AND c.name = "content.EVIL NO CHANCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EVIL NO CHANCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.EVIL NO CHANCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >EVIL NO CHANCE" }]->(child);
```
