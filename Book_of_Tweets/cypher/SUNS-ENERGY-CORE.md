---
name: "thought.SUNS ENERGY CORE"
alias: "Thought: Suns Energy Core"
type: THOUGHT
en_content: "Energy generated in the Sun's core takes a million years to reach its surface: God is great!"
parent: "topic.CREATION"
tags:
- science
- sun
- energy
- creation
- time
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.SUNS ENERGY CORE",
    alias: "Thought: Suns Energy Core",
    parent: "topic.CREATION",
    tags: ['science', 'sun', 'energy', 'creation', 'time'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SUNS ENERGY CORE",
    en_title: "Suns Energy Core",
    en_content: "Energy generated in the Sun's core takes a million years to reach its surface: God is great!",
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
WHERE t.name = "thought.SUNS ENERGY CORE" AND c.name = "content.SUNS ENERGY CORE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SUNS ENERGY CORE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.SUNS ENERGY CORE"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >SUNS ENERGY CORE" }]->(child);
```
