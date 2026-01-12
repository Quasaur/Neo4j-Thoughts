---
name: "thought.SALARY VS VALUE"
alias: "Thought: Salary Vs Value"
type: THOUGHT
en_content: "What's more valuable: my salary or me?"
parent: "topic.HUMANITY"
tags:
- value
- identity
- humanity
- wealth
- morality
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012c)
CREATE (t:THOUGHT {
    name: "thought.SALARY VS VALUE",
    alias: "Thought: Salary Vs Value",
    parent: "topic.HUMANITY",
    tags: ['value', 'identity', 'humanity', 'wealth', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SALARY VS VALUE",
    en_title: "Salary Vs Value",
    en_content: "What's more valuable: my salary or me?",
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
WHERE t.name = "thought.SALARY VS VALUE" AND c.name = "content.SALARY VS VALUE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SALARY VS VALUE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.SALARY VS VALUE"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >SALARY VS VALUE" }]->(child);
```
