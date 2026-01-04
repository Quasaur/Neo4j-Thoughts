---
name: "thought.HEAVEN AS SUN"
alias: "Thought: Heaven As Sun"
type: THOUGHT
en_content: "What is Heaven like? The center of the Sun!"
parent: "topic.SPIRITUALITY"
tags:
- heaven
- sun
- metaphor
- eternity
- light
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN AS SUN",
    alias: "Thought: Heaven As Sun",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'sun', 'metaphor', 'eternity', 'light'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEAVEN AS SUN",
    en_title: "Heaven As Sun",
    en_content: "What is Heaven like? The center of the Sun!",
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
WHERE t.name = "thought.HEAVEN AS SUN" AND c.name = "content.HEAVEN AS SUN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN AS SUN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HEAVEN AS SUN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEAVEN AS SUN" }]->(child);
```
