---
name: "thought.GOD LOVES HOMOSEXUALS"
alias: "Thought: God Loves Homosexuals"
type: THOUGHT
en_content: "God loves homosexuals."
parent: "topic.THE GODHEAD"
tags:
- love
- character
- god
- humanity
- inclusion
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD LOVES HOMOSEXUALS",
    alias: "Thought: God Loves Homosexuals",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'character', 'god', 'humanity', 'inclusion'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD LOVES HOMOSEXUALS",
    en_title: "God Loves Homosexuals",
    en_content: "God loves homosexuals.",
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
WHERE t.name = "thought.GOD LOVES HOMOSEXUALS" AND c.name = "content.GOD LOVES HOMOSEXUALS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD LOVES HOMOSEXUALS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD LOVES HOMOSEXUALS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD LOVES HOMOSEXUALS" }]->(child);
```
