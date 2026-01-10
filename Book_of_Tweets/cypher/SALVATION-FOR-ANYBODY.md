---
name: "thought.SALVATION FOR ANYBODY"
alias: "Thought: Salvation For Anybody"
type: THOUGHT
en_content: "Salvation is not for everybody, yet God can save anybody!"
parent: "topic.GRACE"
tags:
- salvation
- grace
- power
- god
- hope
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.SALVATION FOR ANYBODY",
    alias: "Thought: Salvation For Anybody",
    parent: "topic.GRACE",
    tags: ['salvation', 'grace', 'power', 'god', 'hope'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SALVATION FOR ANYBODY",
    en_title: "Salvation For Anybody",
    en_content: "Salvation is not for everybody, yet God can save anybody!",
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
WHERE t.name = "thought.SALVATION FOR ANYBODY" AND c.name = "content.SALVATION FOR ANYBODY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SALVATION FOR ANYBODY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.SALVATION FOR ANYBODY"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >SALVATION FOR ANYBODY" }]->(child);
```
