---
name: "thought.PURPOSELESS EXISTENCE"
alias: "Thought: Purposeless Existence"
type: THOUGHT
en_content: "What is so scientific about saying that Existence has no purpose?"
parent: "topic.PHILOSOPHY"
tags:
- purpose
- science
- existence
- philosophy
- meaning
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.PURPOSELESS EXISTENCE",
    alias: "Thought: Purposeless Existence",
    parent: "topic.PHILOSOPHY",
    tags: ['purpose', 'science', 'existence', 'philosophy', 'meaning'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PURPOSELESS EXISTENCE",
    en_title: "Purposeless Existence",
    en_content: "What is so scientific about saying that Existence has no purpose?",
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
WHERE t.name = "thought.PURPOSELESS EXISTENCE" AND c.name = "content.PURPOSELESS EXISTENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PURPOSELESS EXISTENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.PURPOSELESS EXISTENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >PURPOSELESS EXISTENCE" }]->(child);
```
