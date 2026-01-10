---
name: "thought.DEFINE FAITH WILL"
alias: "Thought: Define Faith Will"
type: THOUGHT
en_content: "New Definition of Faith: KNOWING God's Will for me in every situation."
parent: "topic.FAITH"
tags:
- faith
- will
- god
- knowledge
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Feb-2014)
CREATE (t:THOUGHT {
    name: "thought.DEFINE FAITH WILL",
    alias: "Thought: Define Faith Will",
    parent: "topic.FAITH",
    tags: ['faith', 'will', 'god', 'knowledge'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE FAITH WILL",
    en_title: "Define Faith Will",
    en_content: "New Definition of Faith: KNOWING God's Will for me in every situation.",
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
WHERE t.name = "thought.DEFINE FAITH WILL" AND c.name = "content.DEFINE FAITH WILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE FAITH WILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.DEFINE FAITH WILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >DEFINE FAITH WILL" }]->(child);
```
