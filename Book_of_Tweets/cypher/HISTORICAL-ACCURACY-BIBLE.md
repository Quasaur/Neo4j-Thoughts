---
name: "thought.HISTORICAL ACCURACY BIBLE"
alias: "Thought: Historical Accuracy Bible"
type: THOUGHT
en_content: "The God in The Bible is described as Truth; therefore The Bible itself must be HISTORICALLY ACCURATE."
parent: "topic.TRUTH"
tags:
- truth
- bible
- history
- accuracy
- revelation
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.HISTORICAL ACCURACY BIBLE",
    alias: "Thought: Historical Accuracy Bible",
    parent: "topic.TRUTH",
    tags: ['truth', 'bible', 'history', 'accuracy', 'revelation'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HISTORICAL ACCURACY BIBLE",
    en_title: "Historical Accuracy Bible",
    en_content: "The God in The Bible is described as Truth; therefore The Bible itself must be HISTORICALLY ACCURATE.",
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
WHERE t.name = "thought.HISTORICAL ACCURACY BIBLE" AND c.name = "content.HISTORICAL ACCURACY BIBLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HISTORICAL ACCURACY BIBLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.HISTORICAL ACCURACY BIBLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >HISTORICAL ACCURACY BIBLE" }]->(child);
```
