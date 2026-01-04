---
name: "thought.SUN ENERGY"
alias: "Thought: Sun Energy"
type: THOUGHT
parent: "topic.CREATION"
tags:
- creation
- sun
- power
- matter
- majesty
level: 2
neo4j: true
insert: true
---
# Sun Energy

> [!Thought-en]
> The Sun releases 5 million tons of matter per second...God is Great!

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2011c)
CREATE (t:THOUGHT {
    name: "thought.SUN ENERGY",
    alias: "Thought: Sun Energy",
    parent: "topic.CREATION",
    tags: ['creation', 'sun', 'power', 'matter', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SUN ENERGY",
    en_title: "Sun Energy",
    en_content: "The Sun releases 5 million tons of matter per second...God is Great!",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SUN ENERGY" AND c.name = "content.SUN ENERGY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SUN ENERGY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.SUN ENERGY"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >SUN ENERGY" }]->(child);
```