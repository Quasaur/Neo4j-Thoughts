---
name: "thought.DESTROYING THE EARTH"
alias: "Thought: Destroying The Earth"
type: THOUGHT
en_content: "God will destroy us for destroying the Earth (Revelation 11:18)."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- judgment
- earth
- destruction
- sovereignty
- bible
level: 2
neo4j: true
insert: true
---
# Destroying The Earth

> [!Thought-en]
> God will destroy us for destroying the Earth (Revelation 11:18).

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2013c)
CREATE (t:THOUGHT {
    name: "thought.DESTROYING THE EARTH",
    alias: "Thought: Destroying The Earth",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['judgment', 'earth', 'destruction', 'sovereignty', 'bible'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DESTROYING THE EARTH",
    en_title: "Destroying The Earth",
    en_content: "God will destroy us for destroying the Earth (Revelation 11:18).",
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
WHERE t.name = "thought.DESTROYING THE EARTH" AND c.name = "content.DESTROYING THE EARTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DESTROYING THE EARTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.DESTROYING THE EARTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >DESTROYING THE EARTH" }]->(child);
```