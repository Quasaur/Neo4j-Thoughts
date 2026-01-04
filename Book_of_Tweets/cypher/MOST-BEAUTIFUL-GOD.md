---
name: "thought.MOST BEAUTIFUL GOD"
alias: "Thought: Most Beautiful God"
type: THOUGHT
en_content: "There is no being God has created that is more handsome, beautiful or gorgeous than Himself."
parent: "topic.BEAUTY"
tags:
- beauty
- aesthetics
- holiness
- character
- divinity
level: 6
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-May-2012)
CREATE (t:THOUGHT {
    name: "thought.MOST BEAUTIFUL GOD",
    alias: "Thought: Most Beautiful God",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'aesthetics', 'holiness', 'character', 'divinity'],
    notes: "",
    level: 6
});

CREATE (c:CONTENT {
    name: "content.MOST BEAUTIFUL GOD",
    en_title: "Most Beautiful God",
    en_content: "There is no being God has created that is more handsome, beautiful or gorgeous than Himself.",
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
WHERE t.name = "thought.MOST BEAUTIFUL GOD" AND c.name = "content.MOST BEAUTIFUL GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MOST BEAUTIFUL GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.MOST BEAUTIFUL GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "BEAUTY >MOST BEAUTIFUL GOD" }]->(child);
```
