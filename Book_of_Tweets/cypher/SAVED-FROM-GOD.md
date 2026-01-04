---
name: "thought.SAVED FROM GOD"
alias: "Thought: Saved From God"
type: THOUGHT
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- salvation
- sovereignty
- power
- judgment
- mercy
level: 2
neo4j: true
insert: true
---
# Saved From God

> [!Thought-en]
> God can save you from anybody...but who can save you from God?

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Nov-2010)
CREATE (t:THOUGHT {
    name: "thought.SAVED FROM GOD",
    alias: "Thought: Saved From God",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['salvation', 'sovereignty', 'power', 'judgment', 'mercy'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SAVED FROM GOD",
    en_title: "Saved From God",
    en_content: "God can save you from anybody...but who can save you from God?",
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
WHERE t.name = "thought.SAVED FROM GOD" AND c.name = "content.SAVED FROM GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SAVED FROM GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.SAVED FROM GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >SAVED FROM GOD" }]->(child);
```