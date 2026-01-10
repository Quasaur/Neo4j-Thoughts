---
name: '"thought.ACCURATE THEOLOGY"'
alias: '"Thought: Accurate Theology, Easier Life"'
type: THOUGHT
en_content: '"The more accurate our theology, the easier the Christian life gets."'
parent: topic.TRUTH
tags:
  - theology
  - truth
  - christianity
  - clarity
  - wisdom
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Apr-2012b)
CREATE (t:THOUGHT {
    name: "thought.ACCURATE THEOLOGY",
    alias: "Thought: Accurate Theology,  Easier Life",
    parent: "topic.TRUTH",
    tags: ['theology', 'truth', 'christianity', 'clarity', 'wisdom'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ACCURATE THEOLOGY",
    en_title: "Accurate Theology",
    en_content: "The more accurate our theology, the easier the Christian life gets.",
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
WHERE t.name = "thought.ACCURATE THEOLOGY" AND c.name = "content.ACCURATE THEOLOGY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ACCURATE THEOLOGY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.ACCURATE THEOLOGY"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >ACCURATE THEOLOGY" }]->(child);
```
