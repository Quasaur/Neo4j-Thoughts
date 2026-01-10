---
name: "thought.GOD SAVES BREAKING"
alias: "Thought: God Saves Breaking"
type: THOUGHT
en_content: "God will save you...after He breaks you. Matthew 21:44"
parent: "topic.GRACE"
tags:
- salvation
- breaking
- grace
- god
- transformation
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD SAVES BREAKING",
    alias: "Thought: God Saves Breaking",
    parent: "topic.GRACE",
    tags: ['salvation', 'breaking', 'grace', 'god', 'transformation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GOD SAVES BREAKING",
    en_title: "God Saves Breaking",
    en_content: "God will save you...after He breaks you. Matthew 21:44",
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
WHERE t.name = "thought.GOD SAVES BREAKING" AND c.name = "content.GOD SAVES BREAKING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD SAVES BREAKING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.GOD SAVES BREAKING"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >GOD SAVES BREAKING" }]->(child);
```
