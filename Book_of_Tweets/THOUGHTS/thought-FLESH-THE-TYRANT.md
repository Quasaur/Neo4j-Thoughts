---
type: THOUGHT
name: "thought.FLESH THE TYRANT"
alias: "Thought: Flesh The Tyrant"
parent: "topic.HUMANITY"
en_content: "The Flesh is a tyrant."
tags: ["flesh", "tyrant", "sin", "humanity", "character"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Feb-2012b)
CREATE (t:THOUGHT {    name: "thought.FLESH THE TYRANT",
    alias: "Thought: Flesh The Tyrant",
    parent: "topic.HUMANITY",
    tags: ['flesh', 'tyrant', 'sin', 'humanity', 'character'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.FLESH THE TYRANT",
    ctype: "THOUGHT",
    en_title: "Flesh The Tyrant",
    en_content: "The Flesh is a tyrant.",
    es_title: "La Carne El Tirano",
    es_content: "La Carne es un tirano.",
    fr_title: "La Chair Le Tyran",
    fr_content: "La Chair est un tyran.",
    hi_title: "शरीर अत्याचारी",
    hi_content: "शरीर एक अत्याचारी है।",
    zh_title: "Ròutǐ Bàozhǔ",
    zh_content: "Ròutǐ shì yīgè bàozhǔ."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FLESH THE TYRANT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->FLESH THE TYRANT"
RETURN t, parent;
```
