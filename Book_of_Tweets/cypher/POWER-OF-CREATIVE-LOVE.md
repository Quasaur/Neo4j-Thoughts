---
name: "thought.POWER OF CREATIVE LOVE"
alias: "Thought: Power Of Creative Love"
type: THOUGHT
en_content: "Love is not weak. Love created this insanely huge universe by simply SPEAKING!"
parent: "topic.THE GODHEAD"
tags:
- love
- creation
- power
- universe
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Jan-2012a)
CREATE (t:THOUGHT {
    name: "thought.POWER OF CREATIVE LOVE",
    alias: "Thought: Power Of Creative Love",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'creation', 'power', 'universe', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.POWER OF CREATIVE LOVE",
    en_title: "Power Of Creative Love",
    en_content: "Love is not weak. Love created this insanely huge universe by simply SPEAKING!",
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
WHERE t.name = "thought.POWER OF CREATIVE LOVE" AND c.name = "content.POWER OF CREATIVE LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.POWER OF CREATIVE LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.POWER OF CREATIVE LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >POWER OF CREATIVE LOVE" }]->(child);
```
