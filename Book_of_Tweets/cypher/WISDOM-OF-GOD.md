---
name: "thought.WISDOM OF GOD"
alias: "Thought: Wisdom Of God"
type: THOUGHT
en_content: "God is older, wiser, smarter, more intelligent and more powerful than you."
parent: "topic.THE GODHEAD"
tags:
- god
- wisdom
- power
- majesty
- intelligence
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Nov-2011b)
CREATE (t:THOUGHT {
    name: "thought.WISDOM OF GOD",
    alias: "Thought: Wisdom Of God",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'wisdom', 'power', 'majesty', 'intelligence'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.WISDOM OF GOD",
    en_title: "Wisdom Of God",
    en_content: "God is older, wiser, smarter, more intelligent and more powerful than you.",
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
WHERE t.name = "thought.WISDOM OF GOD" AND c.name = "content.WISDOM OF GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WISDOM OF GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.WISDOM OF GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >WISDOM OF GOD" }]->(child);
```
