---
name: "thought.GLOBAL WARMING ILLUSION"
alias: "Thought: Global Warming Illusion"
type: THOUGHT
en_content: "Do you still believe global warming is an illusion?"
parent: "topic.CREATION"
tags:
- creation
- environment
- climate
- earth
- stewardship
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.GLOBAL WARMING ILLUSION",
    alias: "Thought: Global Warming Illusion",
    parent: "topic.CREATION",
    tags: ['creation', 'environment', 'climate', 'earth', 'stewardship'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLOBAL WARMING ILLUSION",
    en_title: "Global Warming Illusion",
    en_content: "Do you still believe global warming is an illusion?",
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
WHERE t.name = "thought.GLOBAL WARMING ILLUSION" AND c.name = "content.GLOBAL WARMING ILLUSION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GLOBAL WARMING ILLUSION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.GLOBAL WARMING ILLUSION"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >GLOBAL WARMING ILLUSION" }]->(child);
```
