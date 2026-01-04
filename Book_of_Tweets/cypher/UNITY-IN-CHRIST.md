---
name: "thought.UNITY IN CHRIST"
alias: "Thought: Unity In Christ"
type: THOUGHT
en_content: "True unity of spirit, soul, body, family, community and nation lies only in Jesus Christ."
parent: "topic.THE GODHEAD"
tags:
- unity
- jesus
- christ
- community
- connection
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.UNITY IN CHRIST",
    alias: "Thought: Unity In Christ",
    parent: "topic.THE GODHEAD",
    tags: ['unity', 'jesus', 'christ', 'community', 'connection'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.UNITY IN CHRIST",
    en_title: "Unity In Christ",
    en_content: "True unity of spirit, soul, body, family, community and nation lies only in Jesus Christ.",
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
WHERE t.name = "thought.UNITY IN CHRIST" AND c.name = "content.UNITY IN CHRIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNITY IN CHRIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.UNITY IN CHRIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >UNITY IN CHRIST" }]->(child);
```
