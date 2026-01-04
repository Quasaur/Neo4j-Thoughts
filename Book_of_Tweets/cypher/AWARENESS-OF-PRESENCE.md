---
name: "thought.AWARENESS OF PRESENCE"
alias: "Thought: Awareness Of Presence"
type: THOUGHT
en_content: "Many believe they are aware of God's Wrath but few are aware of God's Loving Presence."
parent: "topic.THE GODHEAD"
tags:
- presence
- wrath
- awareness
- god
- divinity
level: 1
neo4j: true
insert: true
---
# Awareness Of Presence

> [!Thought-en]
> Many believe they are aware of God's Wrath but few are aware of God's Loving Presence.

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.AWARENESS OF PRESENCE",
    alias: "Thought: Awareness Of Presence",
    parent: "topic.THE GODHEAD",
    tags: ['presence', 'wrath', 'awareness', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.AWARENESS OF PRESENCE",
    en_title: "Awareness Of Presence",
    en_content: "Many believe they are aware of God's Wrath but few are aware of God's Loving Presence.",
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
WHERE t.name = "thought.AWARENESS OF PRESENCE" AND c.name = "content.AWARENESS OF PRESENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.AWARENESS OF PRESENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.AWARENESS OF PRESENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >AWARENESS OF PRESENCE" }]->(child);
```