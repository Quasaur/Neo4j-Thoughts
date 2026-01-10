---
name: "thought.UNEMPLOYMENT STATS"
alias: "Thought: Unemployment Stats"
type: THOUGHT
en_content: "White Unemployment : 9%...Black Unemployment : 16%."
parent: "topic.MORALITY"
tags:
- justice
- economy
- race
- society
- morality
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2011c)
CREATE (t:THOUGHT {
    name: "thought.UNEMPLOYMENT STATS",
    alias: "Thought: Unemployment Stats",
    parent: "topic.MORALITY",
    tags: ['justice', 'economy', 'race', 'society', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNEMPLOYMENT STATS",
    en_title: "Unemployment Stats",
    en_content: "White Unemployment : 9%...Black Unemployment : 16%.",
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
WHERE t.name = "thought.UNEMPLOYMENT STATS" AND c.name = "content.UNEMPLOYMENT STATS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNEMPLOYMENT STATS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.UNEMPLOYMENT STATS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >UNEMPLOYMENT STATS" }]->(child);
```
