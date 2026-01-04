---
name: "thought.GORGEOUS DIVINITY"
alias: "Thought: Gorgeous Divinity"
type: THOUGHT
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
# Gorgeous Divinity

> [!Thought-en]
> God is overwhelmingly gorgeous...both inside and out!

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Aug-2012)
CREATE (t:THOUGHT {
    name: "thought.GORGEOUS DIVINITY",
    alias: "Thought: Gorgeous Divinity",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'aesthetics', 'holiness', 'character', 'divinity'],
    notes: "",
    level: 6
});

CREATE (c:CONTENT {
    name: "content.GORGEOUS DIVINITY",
    en_title: "Gorgeous Divinity",
    en_content: "God is overwhelmingly gorgeous...both inside and out!",
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
WHERE t.name = "thought.GORGEOUS DIVINITY" AND c.name = "content.GORGEOUS DIVINITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GORGEOUS DIVINITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.GORGEOUS DIVINITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "BEAUTY >GORGEOUS DIVINITY" }]->(child);
```