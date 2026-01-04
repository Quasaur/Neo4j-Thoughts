---
name: "thought.AVOIDING GOD AND CHURCH"
alias: "Thought: Avoiding God And Church"
type: THOUGHT
en_content: "Why do African American men avoid God and His Church???"
parent: "topic.RELIGION"
tags:
- church
- religion
- race
- avoid
- faith
level: 3
neo4j: true
insert: true
---
# Avoiding God And Church

> [!Thought-en]
> Why do African American men avoid God and His Church???

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012b)
CREATE (t:THOUGHT {
    name: "thought.AVOIDING GOD AND CHURCH",
    alias: "Thought: Avoiding God And Church",
    parent: "topic.RELIGION",
    tags: ['church', 'religion', 'race', 'avoid', 'faith'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AVOIDING GOD AND CHURCH",
    en_title: "Avoiding God And Church",
    en_content: "Why do African American men avoid God and His Church???",
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
WHERE t.name = "thought.AVOIDING GOD AND CHURCH" AND c.name = "content.AVOIDING GOD AND CHURCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.AVOIDING GOD AND CHURCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.AVOIDING GOD AND CHURCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >AVOIDING GOD AND CHURCH" }]->(child);
```