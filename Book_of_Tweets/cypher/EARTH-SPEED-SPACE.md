---
name: "thought.EARTH SPEED SPACE"
alias: "Thought: Earth Speed Space"
type: THOUGHT
en_content: "The Earth is tearing thru space at over 667,000 MPH, and we're not dead ...God is great!"
parent: "topic.CREATION"
tags:
- creation
- science
- earth
- speed
- majesty
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2011c)
CREATE (t:THOUGHT {
    name: "thought.EARTH SPEED SPACE",
    alias: "Thought: Earth Speed Space",
    parent: "topic.CREATION",
    tags: ['creation', 'science', 'earth', 'speed', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EARTH SPEED SPACE",
    en_title: "Earth Speed Space",
    en_content: "The Earth is tearing thru space at over 667,000 MPH, and we're not dead ...God is great!",
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
WHERE t.name = "thought.EARTH SPEED SPACE" AND c.name = "content.EARTH SPEED SPACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EARTH SPEED SPACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.EARTH SPEED SPACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >EARTH SPEED SPACE" }]->(child);
```
