---
name: "thought.TRUTH EXPOSES LIES"
alias: "Thought: Truth Exposes Lies"
type: THOUGHT
en_content: "Truth is dangerous because it exposes lies that people believe to be true; and many would rather kill Truth than abandon their lies."
parent: "topic.TRUTH"
tags:
- truth
- lie
- deception
- danger
- reality
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.TRUTH EXPOSES LIES",
    alias: "Thought: Truth Exposes Lies",
    parent: "topic.TRUTH",
    tags: ['truth', 'lie', 'deception', 'danger', 'reality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TRUTH EXPOSES LIES",
    en_title: "Truth Exposes Lies",
    en_content: "Truth is dangerous because it exposes lies that people believe to be true; and many would rather kill Truth than abandon their lies.",
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
WHERE t.name = "thought.TRUTH EXPOSES LIES" AND c.name = "content.TRUTH EXPOSES LIES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRUTH EXPOSES LIES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.TRUTH EXPOSES LIES"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >TRUTH EXPOSES LIES" }]->(child);
```
