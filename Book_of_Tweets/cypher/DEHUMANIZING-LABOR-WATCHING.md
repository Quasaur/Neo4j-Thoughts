---
name: "thought.DEHUMANIZING LABOR WATCHING"
alias: "Thought: Dehumanizing Labor Watching"
type: THOUGHT
en_content: "To those that continue to dehumanize blue and white collar laborers: GOD IS WATCHING."
parent: "topic.MORALITY"
tags:
- labor
- dehumanization
- watching
- justice
- morality
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jul-2013b)
CREATE (t:THOUGHT {
    name: "thought.DEHUMANIZING LABOR WATCHING",
    alias: "Thought: Dehumanizing Labor Watching",
    parent: "topic.MORALITY",
    tags: ['labor', 'dehumanization', 'watching', 'justice', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEHUMANIZING LABOR WATCHING",
    en_title: "Dehumanizing Labor Watching",
    en_content: "To those that continue to dehumanize blue and white collar laborers: GOD IS WATCHING.",
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
WHERE t.name = "thought.DEHUMANIZING LABOR WATCHING" AND c.name = "content.DEHUMANIZING LABOR WATCHING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEHUMANIZING LABOR WATCHING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.DEHUMANIZING LABOR WATCHING"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >DEHUMANIZING LABOR WATCHING" }]->(child);
```
