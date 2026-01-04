---
name: "thought.WITNESSING GODS PRESENCE"
alias: "Thought: Witnessing Gods Presence"
type: THOUGHT
parent: "topic.WORSHIP"
tags:
- presence
- healing
- miracles
- worship
- assembly
level: 3
neo4j: true
insert: true
---
# Witnessing Gods Presence

> [!Thought-en]
> We assemble to witness the manifestation of God's Presence; it is there that sins are forgiven, yokes are broken and bodies are healed.

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2011a)
CREATE (t:THOUGHT {
    name: "thought.WITNESSING GODS PRESENCE",
    alias: "Thought: Witnessing Gods Presence",
    parent: "topic.WORSHIP",
    tags: ['presence', 'healing', 'miracles', 'worship', 'assembly'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WITNESSING GODS PRESENCE",
    en_title: "Witnessing Gods Presence",
    en_content: "We assemble to witness the manifestation of God's Presence; it is there that sins are forgiven, yokes are broken and bodies are healed.",
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
WHERE t.name = "thought.WITNESSING GODS PRESENCE" AND c.name = "content.WITNESSING GODS PRESENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WITNESSING GODS PRESENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WORSHIP" AND child.name = "thought.WITNESSING GODS PRESENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "WORSHIP >WITNESSING GODS PRESENCE" }]->(child);
```