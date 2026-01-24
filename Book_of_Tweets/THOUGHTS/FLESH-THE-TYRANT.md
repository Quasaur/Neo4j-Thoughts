---
name: "thought.FLESH THE TYRANT"
alias: "Thought: Flesh The Tyrant"
type: THOUGHT
en_content: "The Flesh is a tyrant."
parent: "topic.HUMANITY"
tags:
- flesh
- tyrant
- sin
- humanity
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.FLESH THE TYRANT",
    alias: "Thought: Flesh The Tyrant",
    parent: "topic.HUMANITY",
    tags: ['flesh', 'tyrant', 'sin', 'humanity', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FLESH THE TYRANT",
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

MATCH (t:THOUGHT {name: "thought.FLESH THE TYRANT"})
MATCH (c:CONTENT {name: "content.FLESH THE TYRANT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FLESH THE TYRANT" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.FLESH THE TYRANT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->FLESH THE TYRANT" }]->(child);
```
