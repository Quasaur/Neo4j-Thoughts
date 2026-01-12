---
name: "thought.CREATORS SUFFERING"
alias: "Thought: Creators Suffering"
type: THOUGHT
en_content: "Better for all of us to have gone to Hell than for Our Precious Creator to have suffered the way He did."
parent: "topic.THE GODHEAD"
tags:
- suffering
- atonement
- love
- sacrifice
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011c)
CREATE (t:THOUGHT {
    name: "thought.CREATORS SUFFERING",
    alias: "Thought: Creators Suffering",
    parent: "topic.THE GODHEAD",
    tags: ['suffering', 'atonement', 'love', 'sacrifice', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CREATORS SUFFERING",
    en_title: "Creators Suffering",
    en_content: "Better for all of us to have gone to Hell than for Our Precious Creator to have suffered the way He did.",
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
WHERE t.name = "thought.CREATORS SUFFERING" AND c.name = "content.CREATORS SUFFERING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CREATORS SUFFERING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.CREATORS SUFFERING"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CREATORS SUFFERING" }]->(child);
```
