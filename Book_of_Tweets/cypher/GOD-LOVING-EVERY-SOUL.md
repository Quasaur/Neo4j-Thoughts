---
name: "thought.GOD LOVING EVERY SOUL"
alias: "Thought: God Loving Every Soul"
type: THOUGHT
en_content: "There is no soul created by God that He did not love."
parent: "topic.THE GODHEAD"
tags:
- love
- soul
- creation
- god
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Jul-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD LOVING EVERY SOUL",
    alias: "Thought: God Loving Every Soul",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'soul', 'creation', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD LOVING EVERY SOUL",
    en_title: "God Loving Every Soul",
    en_content: "There is no soul created by God that He did not love.",
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
WHERE t.name = "thought.GOD LOVING EVERY SOUL" AND c.name = "content.GOD LOVING EVERY SOUL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD LOVING EVERY SOUL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD LOVING EVERY SOUL"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD LOVING EVERY SOUL" }]->(child);
```
