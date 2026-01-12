---
name: "thought.UNDERSTANDING SIN HELL"
alias: "Thought: Understanding Sin Hell"
type: THOUGHT
en_content: "You will never understand how God feels about sin until you look into Hell."
parent: "topic.EVIL"
tags:
- sin
- hell
- judgment
- god
- character
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Aug-2012)
CREATE (t:THOUGHT {
    name: "thought.UNDERSTANDING SIN HELL",
    alias: "Thought: Understanding Sin Hell",
    parent: "topic.EVIL",
    tags: ['sin', 'hell', 'judgment', 'god', 'character'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.UNDERSTANDING SIN HELL",
    en_title: "Understanding Sin Hell",
    en_content: "You will never understand how God feels about sin until you look into Hell.",
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
WHERE t.name = "thought.UNDERSTANDING SIN HELL" AND c.name = "content.UNDERSTANDING SIN HELL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNDERSTANDING SIN HELL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.UNDERSTANDING SIN HELL"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >UNDERSTANDING SIN HELL" }]->(child);
```
