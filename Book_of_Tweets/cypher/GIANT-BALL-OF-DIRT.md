---
name: "thought.GIANT BALL OF DIRT"
alias: "Thought: Giant Ball Of Dirt"
type: THOUGHT
en_content: "We are living on a GIANT BALL OF DIRT...God is great!"
parent: "topic.CREATION"
tags:
- creation
- earth
- perspective
- power
- majesty
level: 2
neo4j: true
insert: true
---
# Giant Ball Of Dirt

> [!Thought-en]
> We are living on a GIANT BALL OF DIRT...God is great!

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.GIANT BALL OF DIRT",
    alias: "Thought: Giant Ball Of Dirt",
    parent: "topic.CREATION",
    tags: ['creation', 'earth', 'perspective', 'power', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GIANT BALL OF DIRT",
    en_title: "Giant Ball Of Dirt",
    en_content: "We are living on a GIANT BALL OF DIRT...God is great!",
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
WHERE t.name = "thought.GIANT BALL OF DIRT" AND c.name = "content.GIANT BALL OF DIRT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GIANT BALL OF DIRT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.GIANT BALL OF DIRT"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >GIANT BALL OF DIRT" }]->(child);
```