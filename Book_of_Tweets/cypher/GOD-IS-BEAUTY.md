---
name: "thought.GOD IS BEAUTY"
alias: "Thought: God Is Beauty"
type: THOUGHT
en_content: "God is Beauty. Apart from Him we are ugly."
parent: "topic.BEAUTY"
tags:
- beauty
- aesthetics
- divinity
- holiness
- character
level: 5
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Jul-2011)
CREATE (t:THOUGHT {
    name: "thought.GOD IS BEAUTY",
    alias: "Thought: God Is Beauty",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'aesthetics', 'divinity', 'holiness', 'character'],
    notes: "",
    level: 5
});

CREATE (c:CONTENT {
    name: "content.GOD IS BEAUTY",
    en_title: "God Is Beauty",
    en_content: "God is Beauty. Apart from Him we are ugly.",
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
WHERE t.name = "thought.GOD IS BEAUTY" AND c.name = "content.GOD IS BEAUTY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD IS BEAUTY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.GOD IS BEAUTY"
MERGE (parent)-[:HAS_THOUGHT { "name": "BEAUTY >GOD IS BEAUTY" }]->(child);
```
