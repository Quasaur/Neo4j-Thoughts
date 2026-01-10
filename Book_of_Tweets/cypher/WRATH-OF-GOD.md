---
name: "thought.WRATH OF GOD"
alias: "Thought: Wrath Of God"
type: THOUGHT
en_content: "The worst thing Earth must face is not Antichrist, but The Wrath of God."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- wrath
- god
- judgment
- earth
- sovereignty
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.WRATH OF GOD",
    alias: "Thought: Wrath Of God",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['wrath', 'god', 'judgment', 'earth', 'sovereignty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WRATH OF GOD",
    en_title: "Wrath Of God",
    en_content: "The worst thing Earth must face is not Antichrist, but The Wrath of God.",
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
WHERE t.name = "thought.WRATH OF GOD" AND c.name = "content.WRATH OF GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WRATH OF GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.WRATH OF GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >WRATH OF GOD" }]->(child);
```
