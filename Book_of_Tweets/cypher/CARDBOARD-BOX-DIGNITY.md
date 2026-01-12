---
name: "thought.CARDBOARD BOX DIGNITY"
alias: "Thought: Cardboard Box Dignity"
type: THOUGHT
en_content: "I'd rather live in a cardboard box than to earn 6 figures and be treated like a pet!"
parent: "topic.HUMANITY"
tags:
- dignity
- wealth
- humanity
- character
- choice
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012d)
CREATE (t:THOUGHT {
    name: "thought.CARDBOARD BOX DIGNITY",
    alias: "Thought: Cardboard Box Dignity",
    parent: "topic.HUMANITY",
    tags: ['dignity', 'wealth', 'humanity', 'character', 'choice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CARDBOARD BOX DIGNITY",
    en_title: "Cardboard Box Dignity",
    en_content: "I'd rather live in a cardboard box than to earn 6 figures and be treated like a pet!",
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
WHERE t.name = "thought.CARDBOARD BOX DIGNITY" AND c.name = "content.CARDBOARD BOX DIGNITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CARDBOARD BOX DIGNITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.CARDBOARD BOX DIGNITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >CARDBOARD BOX DIGNITY" }]->(child);
```
