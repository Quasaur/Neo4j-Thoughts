---
name: "thought.MEANINGLESS LIFE LIE"
alias: "Thought: Meaningless Life Lie"
type: THOUGHT
en_content: "Religion: if no one's right, and everyone's wrong, then life is both meaningless AND a lie."
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- meaning
- religion
- truth
- skepticism
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jan-2012b)
CREATE (t:THOUGHT {
    name: "thought.MEANINGLESS LIFE LIE",
    alias: "Thought: Meaningless Life Lie",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'meaning', 'religion', 'truth', 'skepticism'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MEANINGLESS LIFE LIE",
    en_title: "Meaningless Life Lie",
    en_content: "Religion: if no one's right, and everyone's wrong, then life is both meaningless AND a lie.",
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
WHERE t.name = "thought.MEANINGLESS LIFE LIE" AND c.name = "content.MEANINGLESS LIFE LIE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MEANINGLESS LIFE LIE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.MEANINGLESS LIFE LIE"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >MEANINGLESS LIFE LIE" }]->(child);
```
