---
name: "thought.HEAVEN HOME WITHIN"
alias: "Thought: Heaven Home Within"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- heaven
- home
- spirituality
- transformation
- presence
level: 2
neo4j: true
insert: true
---
# Heaven Home Within

> [!Thought-en]
> Before I can go Home to Heaven, Heaven must find a home in me.

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN HOME WITHIN",
    alias: "Thought: Heaven Home Within",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'home', 'spirituality', 'transformation', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEAVEN HOME WITHIN",
    en_title: "Heaven Home Within",
    en_content: "Before I can go Home to Heaven, Heaven must find a home in me.",
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
WHERE t.name = "thought.HEAVEN HOME WITHIN" AND c.name = "content.HEAVEN HOME WITHIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN HOME WITHIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HEAVEN HOME WITHIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEAVEN HOME WITHIN" }]->(child);
```