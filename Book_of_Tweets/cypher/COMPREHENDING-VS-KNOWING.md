---
name: "thought.COMPREHENDING VS KNOWING"
alias: "Thought: Comprehending Vs Knowing"
type: THOUGHT
en_content: "If I could comprehend Him, He wouldn't be God; but I can know Him."
parent: "topic.THE GODHEAD"
tags:
- knowledge
- comprehension
- god
- divinity
- relationship
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.COMPREHENDING VS KNOWING",
    alias: "Thought: Comprehending Vs Knowing",
    parent: "topic.THE GODHEAD",
    tags: ['knowledge', 'comprehension', 'god', 'divinity', 'relationship'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.COMPREHENDING VS KNOWING",
    en_title: "Comprehending Vs Knowing",
    en_content: "If I could comprehend Him, He wouldn't be God; but I can know Him.",
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
WHERE t.name = "thought.COMPREHENDING VS KNOWING" AND c.name = "content.COMPREHENDING VS KNOWING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.COMPREHENDING VS KNOWING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.COMPREHENDING VS KNOWING"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >COMPREHENDING VS KNOWING" }]->(child);
```
