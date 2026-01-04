---
name: "thought.EARTH STORMS"
alias: "Thought: Earth Storms"
type: THOUGHT
parent: "topic.CREATION"
tags:
- creation
- earth
- storms
- power
- majesty
level: 2
neo4j: true
insert: true
---
# Earth Storms

> [!Thought-en]
> Earth has about 16 million storms per year...God is Great!

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2011a)
CREATE (t:THOUGHT {
    name: "thought.EARTH STORMS",
    alias: "Thought: Earth Storms",
    parent: "topic.CREATION",
    tags: ['creation', 'earth', 'storms', 'power', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EARTH STORMS",
    en_title: "Earth Storms",
    en_content: "Earth has about 16 million storms per year...God is Great!",
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
WHERE t.name = "thought.EARTH STORMS" AND c.name = "content.EARTH STORMS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EARTH STORMS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.EARTH STORMS"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >EARTH STORMS" }]->(child);
```