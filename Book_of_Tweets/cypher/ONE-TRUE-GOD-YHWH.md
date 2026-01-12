---
name: "thought.ONE TRUE GOD YHWH"
alias: "Thought: One True God Yhwh"
type: THOUGHT
en_content: "I believe there is One True God -- YHWH; and Jesus Christ is His Living Word! Hebrews 1:1-4"
parent: "topic.THE GODHEAD"
tags:
- god
- jesus
- word
- trinity
- truth
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.ONE TRUE GOD YHWH",
    alias: "Thought: One True God Yhwh",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'jesus', 'word', 'trinity', 'truth'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ONE TRUE GOD YHWH",
    en_title: "One True God Yhwh",
    en_content: "I believe there is One True God -- YHWH; and Jesus Christ is His Living Word! Hebrews 1:1-4",
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
WHERE t.name = "thought.ONE TRUE GOD YHWH" AND c.name = "content.ONE TRUE GOD YHWH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ONE TRUE GOD YHWH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ONE TRUE GOD YHWH"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >ONE TRUE GOD YHWH" }]->(child);
```
