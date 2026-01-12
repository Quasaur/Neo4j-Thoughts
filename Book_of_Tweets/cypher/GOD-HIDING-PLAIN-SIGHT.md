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
ptopic: 
---

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
    es_title: "Dios Escondido a Plena Vista",
    es_content: "Claro, Dios se está escondiendo...a plena vista.",
    fr_title: "Dieu Se Cache au Grand Jour",
    fr_content: "Bien sûr, Dieu se cache...au grand jour.",
    hi_title: "परमेश्वर सामने छुपा हुआ है",
    hi_content: "हाँ, परमेश्वर छुप रहा है...बिल्कुल सामने।",
    zh_title: "Shàngdì cáng zài míngxiǎn chù",
    zh_content: "dānggrán, Shàngdì zài duǒcáng...jiù zài míngxiǎn chù."
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
