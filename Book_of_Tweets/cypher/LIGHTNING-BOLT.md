---
name: "thought.LIGHTNING BOLT"
alias: "Thought: Lightning Bolt"
type: THOUGHT
en_content: "A single lightning bolt can be 5 miles in length and hotter than the surface of the Sun...God is Great!"
parent: "topic.CREATION"
tags:
- creation
- power
- lightning
- nature
- majesty
level: 2
neo4j: true
insert: true
---
# Lightning Bolt

> [!Thought-en]
> A single lightning bolt can be 5 miles in length and hotter than the surface of the Sun...God is Great!

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2011b)
CREATE (t:THOUGHT {
    name: "thought.LIGHTNING BOLT",
    alias: "Thought: Lightning Bolt",
    parent: "topic.CREATION",
    tags: ['creation', 'power', 'lightning', 'nature', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIGHTNING BOLT",
    en_title: "Lightning Bolt",
    en_content: "A single lightning bolt can be 5 miles in length and hotter than the surface of the Sun...God is Great!",
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
WHERE t.name = "thought.LIGHTNING BOLT" AND c.name = "content.LIGHTNING BOLT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIGHTNING BOLT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.LIGHTNING BOLT"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >LIGHTNING BOLT" }]->(child);
```