---
name: "thought.ETERNAL IMMORTALITY"
alias: "Thought: Eternal Immortality"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- eternity
- immortality
- life
- death
- divinity
level: 1
neo4j: true
insert: true
---
# Eternal Immortality

> [!Thought-en]
> If you die eternally, you're already dead; if you live eternally, you were always immortal!

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-May-2012b)
CREATE (t:THOUGHT {
    name: "thought.ETERNAL IMMORTALITY",
    alias: "Thought: Eternal Immortality",
    parent: "topic.THE GODHEAD",
    tags: ['eternity', 'immortality', 'life', 'death', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ETERNAL IMMORTALITY",
    en_title: "Eternal Immortality",
    en_content: "If you die eternally, you're already dead; if you live eternally, you were always immortal!",
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
WHERE t.name = "thought.ETERNAL IMMORTALITY" AND c.name = "content.ETERNAL IMMORTALITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ETERNAL IMMORTALITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ETERNAL IMMORTALITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >ETERNAL IMMORTALITY" }]->(child);
```