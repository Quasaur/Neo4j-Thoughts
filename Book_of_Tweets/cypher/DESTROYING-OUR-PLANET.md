---
name: "thought.DESTROYING OUR PLANET"
alias: "Thought: Destroying Our Planet"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- technology
- greed
- environment
- planet
- destruction
level: 3
neo4j: true
insert: true
---
# Destroying Our Planet

> [!Thought-en]
> Our technology, industry and greed are destroying our planet.

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2013b)
CREATE (t:THOUGHT {
    name: "thought.DESTROYING OUR PLANET",
    alias: "Thought: Destroying Our Planet",
    parent: "topic.MORALITY",
    tags: ['technology', 'greed', 'environment', 'planet', 'destruction'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DESTROYING OUR PLANET",
    en_title: "Destroying Our Planet",
    en_content: "Our technology, industry and greed are destroying our planet.",
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
WHERE t.name = "thought.DESTROYING OUR PLANET" AND c.name = "content.DESTROYING OUR PLANET"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DESTROYING OUR PLANET" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.DESTROYING OUR PLANET"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >DESTROYING OUR PLANET" }]->(child);
```