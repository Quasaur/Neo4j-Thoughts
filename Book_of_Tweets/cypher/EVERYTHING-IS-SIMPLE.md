---
name: "thought.EVERYTHING IS SIMPLE"
alias: "Thought: Everything Is Simple"
type: THOUGHT
en_content: "To God complexity itself does not exists...everything is simple to God."
parent: "topic.THE GODHEAD"
tags:
- simplicity
- complexity
- knowledge
- divinity
- god
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.EVERYTHING IS SIMPLE",
    alias: "Thought: Everything Is Simple",
    parent: "topic.THE GODHEAD",
    tags: ['simplicity', 'complexity', 'knowledge', 'divinity', 'god'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.EVERYTHING IS SIMPLE",
    en_title: "Everything Is Simple",
    en_content: "To God complexity itself does not exists...everything is simple to God.",
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
WHERE t.name = "thought.EVERYTHING IS SIMPLE" AND c.name = "content.EVERYTHING IS SIMPLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EVERYTHING IS SIMPLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.EVERYTHING IS SIMPLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >EVERYTHING IS SIMPLE" }]->(child);
```
