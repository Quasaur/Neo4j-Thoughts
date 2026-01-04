---
name: "thought.GOD HIDING PLAIN SIGHT"
alias: "Thought: God Hiding Plain Sight"
type: THOUGHT
en_content: "Sure, God is hiding...in plain sight."
parent: "topic.THE GODHEAD"
tags:
- hidden
- sight
- god
- presence
- divinity
level: 1
neo4j: true
insert: true
---
# God Hiding Plain Sight

> [!Thought-en]
> Sure, God is hiding...in plain sight.

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013f)
CREATE (t:THOUGHT {
    name: "thought.GOD HIDING PLAIN SIGHT",
    alias: "Thought: God Hiding Plain Sight",
    parent: "topic.THE GODHEAD",
    tags: ['hidden', 'sight', 'god', 'presence', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD HIDING PLAIN SIGHT",
    en_title: "God Hiding Plain Sight",
    en_content: "Sure, God is hiding...in plain sight.",
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
WHERE t.name = "thought.GOD HIDING PLAIN SIGHT" AND c.name = "content.GOD HIDING PLAIN SIGHT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD HIDING PLAIN SIGHT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD HIDING PLAIN SIGHT"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD HIDING PLAIN SIGHT" }]->(child);
```