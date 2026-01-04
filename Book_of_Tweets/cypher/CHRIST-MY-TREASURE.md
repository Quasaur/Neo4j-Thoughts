---
name: "thought.CHRIST MY TREASURE"
alias: "Thought: Christ My Treasure"
type: THOUGHT
en_content: "Christ is my Treasure, my Fortune, my Wealth, my NestEgg and my Riches!"
parent: "topic.THE GODHEAD"
tags:
- christ
- wealth
- treasure
- divinity
- value
level: 1
neo4j: true
insert: true
---
# Christ My Treasure

> [!Thought-en]
> Christ is my Treasure, my Fortune, my Wealth, my NestEgg and my Riches!

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-May-2012)
CREATE (t:THOUGHT {
    name: "thought.CHRIST MY TREASURE",
    alias: "Thought: Christ My Treasure",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'wealth', 'treasure', 'divinity', 'value'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CHRIST MY TREASURE",
    en_title: "Christ My Treasure",
    en_content: "Christ is my Treasure, my Fortune, my Wealth, my NestEgg and my Riches!",
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
WHERE t.name = "thought.CHRIST MY TREASURE" AND c.name = "content.CHRIST MY TREASURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRIST MY TREASURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.CHRIST MY TREASURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CHRIST MY TREASURE" }]->(child);
```