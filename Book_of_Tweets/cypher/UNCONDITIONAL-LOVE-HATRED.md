---
name: "thought.UNCONDITIONAL LOVE HATRED"
alias: "Thought: Unconditional Love Hatred"
type: THOUGHT
en_content: "God's Love is unconditional...as is His Hatred of evil."
parent: "topic.THE GODHEAD"
tags:
- love
- hatred
- evil
- character
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.UNCONDITIONAL LOVE HATRED",
    alias: "Thought: Unconditional Love Hatred",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'hatred', 'evil', 'character', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL LOVE HATRED",
    en_title: "Unconditional Love Hatred",
    en_content: "God's Love is unconditional...as is His Hatred of evil.",
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
WHERE t.name = "thought.UNCONDITIONAL LOVE HATRED" AND c.name = "content.UNCONDITIONAL LOVE HATRED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNCONDITIONAL LOVE HATRED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.UNCONDITIONAL LOVE HATRED"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >UNCONDITIONAL LOVE HATRED" }]->(child);
```
