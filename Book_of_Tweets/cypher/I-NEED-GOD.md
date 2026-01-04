---
name: "thought.I NEED GOD"
alias: "Thought: I Need God"
type: THOUGHT
en_content: "Revelation 20:11, 12: I don't need a universe to exist; I just need God."
parent: "topic.SPIRITUALITY"
tags:
- existence
- spirituality
- god
- eternity
- presence
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2011c)
CREATE (t:THOUGHT {
    name: "thought.I NEED GOD",
    alias: "Thought: I Need God",
    parent: "topic.SPIRITUALITY",
    tags: ['existence', 'spirituality', 'god', 'eternity', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.I NEED GOD",
    en_title: "I Need God",
    en_content: "Revelation 20:11, 12: I don't need a universe to exist; I just need God.",
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
WHERE t.name = "thought.I NEED GOD" AND c.name = "content.I NEED GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.I NEED GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.I NEED GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >I NEED GOD" }]->(child);
```
