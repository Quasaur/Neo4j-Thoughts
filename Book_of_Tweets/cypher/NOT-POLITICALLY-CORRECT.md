---
name: "thought.NOT POLITICALLY CORRECT"
alias: "Thought: Not Politically Correct"
type: THOUGHT
en_content: "God is not politically correct."
parent: "topic.THE GODHEAD"
tags:
- truth
- politics
- character
- god
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.NOT POLITICALLY CORRECT",
    alias: "Thought: Not Politically Correct",
    parent: "topic.THE GODHEAD",
    tags: ['truth', 'politics', 'character', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NOT POLITICALLY CORRECT",
    en_title: "Not Politically Correct",
    en_content: "God is not politically correct.",
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
WHERE t.name = "thought.NOT POLITICALLY CORRECT" AND c.name = "content.NOT POLITICALLY CORRECT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOT POLITICALLY CORRECT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NOT POLITICALLY CORRECT"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NOT POLITICALLY CORRECT" }]->(child);
```
