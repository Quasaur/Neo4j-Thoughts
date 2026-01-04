---
name: "thought.HEAVY DIVINE WILL"
alias: "Thought: Heavy Divine Will"
type: THOUGHT
en_content: "The Will of God is far too heavy for frail human hands to budge it in any direction; answered prayer is ALWAYS an Act of Divine Mercy."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- will
- prayer
- mercy
- sovereignty
- power
level: 2
neo4j: true
insert: true
---
# Heavy Divine Will

> [!Thought-en]
> The Will of God is far too heavy for frail human hands to budge it in any direction; answered prayer is ALWAYS an Act of Divine Mercy.

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011d)
CREATE (t:THOUGHT {
    name: "thought.HEAVY DIVINE WILL",
    alias: "Thought: Heavy Divine Will",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['will', 'prayer', 'mercy', 'sovereignty', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEAVY DIVINE WILL",
    en_title: "Heavy Divine Will",
    en_content: "The Will of God is far too heavy for frail human hands to budge it in any direction; answered prayer is ALWAYS an Act of Divine Mercy.",
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
WHERE t.name = "thought.HEAVY DIVINE WILL" AND c.name = "content.HEAVY DIVINE WILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVY DIVINE WILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.HEAVY DIVINE WILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >HEAVY DIVINE WILL" }]->(child);
```