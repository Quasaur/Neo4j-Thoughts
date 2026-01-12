---
name: "thought.SHOULD BE VS WILL BE"
alias: "Thought: Should Be Vs Will Be"
type: THOUGHT
en_content: "Everything is as it should be, but not as it will be."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- time
- prophecy
- destiny
- future
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Aug-2013c)
CREATE (t:THOUGHT {
    name: "thought.SHOULD BE VS WILL BE",
    alias: "Thought: Should Be Vs Will Be",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'time', 'prophecy', 'destiny', 'future'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SHOULD BE VS WILL BE",
    en_title: "Should Be Vs Will Be",
    en_content: "Everything is as it should be, but not as it will be.",
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
WHERE t.name = "thought.SHOULD BE VS WILL BE" AND c.name = "content.SHOULD BE VS WILL BE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHOULD BE VS WILL BE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.SHOULD BE VS WILL BE"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >SHOULD BE VS WILL BE" }]->(child);
```
