---
name: "thought.JESUS NON NEGOTIABLE"
alias: "Thought: Jesus Non Negotiable"
type: THOUGHT
en_content: "I must have Jesus...everything else is negotiable."
parent: "topic.SPIRITUALITY"
tags:
- jesus
- priority
- spirituality
- commitment
- devotion
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2012c)
CREATE (t:THOUGHT {
    name: "thought.JESUS NON NEGOTIABLE",
    alias: "Thought: Jesus Non Negotiable",
    parent: "topic.SPIRITUALITY",
    tags: ['jesus', 'priority', 'spirituality', 'commitment', 'devotion'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.JESUS NON NEGOTIABLE",
    en_title: "Jesus Non Negotiable",
    en_content: "I must have Jesus...everything else is negotiable.",
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
WHERE t.name = "thought.JESUS NON NEGOTIABLE" AND c.name = "content.JESUS NON NEGOTIABLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.JESUS NON NEGOTIABLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.JESUS NON NEGOTIABLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >JESUS NON NEGOTIABLE" }]->(child);
```
