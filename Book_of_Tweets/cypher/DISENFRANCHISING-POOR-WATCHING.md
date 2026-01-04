---
name: "thought.DISENFRANCHISING POOR WATCHING"
alias: "Thought: Disenfranchising Poor Watching"
type: THOUGHT
en_content: "To those that continue to disenfranchise the poor and minorities: GOD IS WATCHING."
parent: "topic.MORALITY"
tags:
- poor
- minorities
- watching
- justice
- morality
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.DISENFRANCHISING POOR WATCHING",
    alias: "Thought: Disenfranchising Poor Watching",
    parent: "topic.MORALITY",
    tags: ['poor', 'minorities', 'watching', 'justice', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DISENFRANCHISING POOR WATCHING",
    en_title: "Disenfranchising Poor Watching",
    en_content: "To those that continue to disenfranchise the poor and minorities: GOD IS WATCHING.",
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
WHERE t.name = "thought.DISENFRANCHISING POOR WATCHING" AND c.name = "content.DISENFRANCHISING POOR WATCHING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DISENFRANCHISING POOR WATCHING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.DISENFRANCHISING POOR WATCHING"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >DISENFRANCHISING POOR WATCHING" }]->(child);
```
