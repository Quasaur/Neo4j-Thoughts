---
name: "thought.BIBLE AS HISTORY"
alias: "Thought: Bible As History"
type: THOUGHT
en_content: "The Bible says that God cannot lie. If therefore the Bible is not an ACCURATE HISTORICAL DOCUMENT, then it cannot be inspired by God."
parent: "topic.TRUTH"
tags:
- bible
- truth
- history
- inspiration
- document
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.BIBLE AS HISTORY",
    alias: "Thought: Bible As History",
    parent: "topic.TRUTH",
    tags: ['bible', 'truth', 'history', 'inspiration', 'document'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BIBLE AS HISTORY",
    en_title: "Bible As History",
    en_content: "The Bible says that God cannot lie. If therefore the Bible is not an ACCURATE HISTORICAL DOCUMENT, then it cannot be inspired by God.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BIBLE AS HISTORY" AND c.name = "content.BIBLE AS HISTORY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BIBLE AS HISTORY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.BIBLE AS HISTORY"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >BIBLE AS HISTORY" }]->(child);
```
