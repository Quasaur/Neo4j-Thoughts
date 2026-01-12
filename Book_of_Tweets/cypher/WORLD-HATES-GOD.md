---
name: "thought.WORLD HATES GOD"
alias: "Thought: World Hates God"
type: THOUGHT
en_content: "God loves the world. The world hates God. This is not going to end well for the world."
parent: "topic.HUMANITY"
tags:
- world
- hate
- god
- judgment
- humanity
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.WORLD HATES GOD",
    alias: "Thought: World Hates God",
    parent: "topic.HUMANITY",
    tags: ['world', 'hate', 'god', 'judgment', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WORLD HATES GOD",
    en_title: "World Hates God",
    en_content: "God loves the world. The world hates God. This is not going to end well for the world.",
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
WHERE t.name = "thought.WORLD HATES GOD" AND c.name = "content.WORLD HATES GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WORLD HATES GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.WORLD HATES GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >WORLD HATES GOD" }]->(child);
```
