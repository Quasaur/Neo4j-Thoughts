---
name: "thought.DANGER OF TRUTH"
alias: "Thought: Danger Of Truth"
type: THOUGHT
en_content: "Truth is a dangerous thing...yet so is a lie."
parent: "topic.TRUTH"
tags:
- truth
- lie
- danger
- philosophy
- morality
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.DANGER OF TRUTH",
    alias: "Thought: Danger Of Truth",
    parent: "topic.TRUTH",
    tags: ['truth', 'lie', 'danger', 'philosophy', 'morality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DANGER OF TRUTH",
    en_title: "Danger Of Truth",
    en_content: "Truth is a dangerous thing...yet so is a lie.",
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
WHERE t.name = "thought.DANGER OF TRUTH" AND c.name = "content.DANGER OF TRUTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DANGER OF TRUTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.DANGER OF TRUTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >DANGER OF TRUTH" }]->(child);
```
