---
name: "thought.LIMITLESS DIVINE POWER"
alias: "Thought: Limitless Divine Power"
type: THOUGHT
en_content: "ABSOLUTE POWER: Besides His Own Limitless Power, everyone else's power is also at God's Disposal...even Satan's."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- power
- sovereignty
- god
- disposal
- control
level: 2
neo4j: true
insert: true
---
# Limitless Divine Power

> [!Thought-en]
> ABSOLUTE POWER: Besides His Own Limitless Power, everyone else's power is also at God's Disposal...even Satan's.

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011e)
CREATE (t:THOUGHT {
    name: "thought.LIMITLESS DIVINE POWER",
    alias: "Thought: Limitless Divine Power",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['power', 'sovereignty', 'god', 'disposal', 'control'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIMITLESS DIVINE POWER",
    en_title: "Limitless Divine Power",
    en_content: "ABSOLUTE POWER: Besides His Own Limitless Power, everyone else's power is also at God's Disposal...even Satan's.",
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
WHERE t.name = "thought.LIMITLESS DIVINE POWER" AND c.name = "content.LIMITLESS DIVINE POWER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIMITLESS DIVINE POWER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.LIMITLESS DIVINE POWER"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >LIMITLESS DIVINE POWER" }]->(child);
```