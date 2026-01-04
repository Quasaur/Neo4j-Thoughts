---
name: "thought.EXPERIENCING GOD"
alias: "Thought: Experiencing God"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- experience
- god
- life
- death
- presence
level: 2
neo4j: true
insert: true
---
# Experiencing God

> [!Thought-en]
> You don't want to live your entire life and die without experiencing God.

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jan-2012a)
CREATE (t:THOUGHT {
    name: "thought.EXPERIENCING GOD",
    alias: "Thought: Experiencing God",
    parent: "topic.SPIRITUALITY",
    tags: ['experience', 'god', 'life', 'death', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EXPERIENCING GOD",
    en_title: "Experiencing God",
    en_content: "You don't want to live your entire life and die without experiencing God.",
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
WHERE t.name = "thought.EXPERIENCING GOD" AND c.name = "content.EXPERIENCING GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EXPERIENCING GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.EXPERIENCING GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >EXPERIENCING GOD" }]->(child);
```