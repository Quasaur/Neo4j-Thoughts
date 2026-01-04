---
name: "thought.GREATER THAN BEING LOVED"
alias: "Thought: Greater Than Being Loved"
type: THOUGHT
en_content: "What could be greater than being loved? Being able to love!"
parent: "topic.LOVE"
tags:
- love
- sacrifice
- ability
- emotion
- divinity
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.GREATER THAN BEING LOVED",
    alias: "Thought: Greater Than Being Loved",
    parent: "topic.LOVE",
    tags: ['love', 'sacrifice', 'ability', 'emotion', 'divinity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GREATER THAN BEING LOVED",
    en_title: "Greater Than Being Loved",
    en_content: "What could be greater than being loved? Being able to love!",
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
WHERE t.name = "thought.GREATER THAN BEING LOVED" AND c.name = "content.GREATER THAN BEING LOVED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GREATER THAN BEING LOVED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LOVE" AND child.name = "thought.GREATER THAN BEING LOVED"
MERGE (parent)-[:HAS_THOUGHT { "name": "LOVE >GREATER THAN BEING LOVED" }]->(child);
```
