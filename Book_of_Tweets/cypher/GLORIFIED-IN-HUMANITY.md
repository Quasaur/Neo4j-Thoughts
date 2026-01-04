---
name: "thought.GLORIFIED IN HUMANITY"
alias: "Thought: Glorified In Humanity"
type: THOUGHT
en_content: "God WILL be glorified in Humanity: either by rewarding obedience, faith and courage...or by punishing rebellion, unbelief and cowardice."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- glory
- humanity
- obedience
- rebellion
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Mar-2014)
CREATE (t:THOUGHT {
    name: "thought.GLORIFIED IN HUMANITY",
    alias: "Thought: Glorified In Humanity",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['glory', 'humanity', 'obedience', 'rebellion'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLORIFIED IN HUMANITY",
    en_title: "Glorified In Humanity",
    en_content: "God WILL be glorified in Humanity: either by rewarding obedience, faith and courage...or by punishing rebellion, unbelief and cowardice.",
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
WHERE t.name = "thought.GLORIFIED IN HUMANITY" AND c.name = "content.GLORIFIED IN HUMANITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GLORIFIED IN HUMANITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.GLORIFIED IN HUMANITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >GLORIFIED IN HUMANITY" }]->(child);
```
