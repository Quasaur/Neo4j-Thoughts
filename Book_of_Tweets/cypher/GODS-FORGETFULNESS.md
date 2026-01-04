---
name: "thought.GODS FORGETFULNESS"
alias: "Thought: Gods Forgetfulness"
type: THOUGHT
parent: "topic.GRACE"
tags:
- forgiveness
- memory
- grace
- peace
- character
level: 3
neo4j: true
insert: true
---
# Gods Forgetfulness

> [!Thought-en]
> Don't bring to mind what God has decided to forget.

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.GODS FORGETFULNESS",
    alias: "Thought: Gods Forgetfulness",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'memory', 'grace', 'peace', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GODS FORGETFULNESS",
    en_title: "Gods Forgetfulness",
    en_content: "Don't bring to mind what God has decided to forget.",
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
WHERE t.name = "thought.GODS FORGETFULNESS" AND c.name = "content.GODS FORGETFULNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS FORGETFULNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.GODS FORGETFULNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >GODS FORGETFULNESS" }]->(child);
```