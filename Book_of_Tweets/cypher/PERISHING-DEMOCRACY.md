---
name: "thought.PERISHING DEMOCRACY"
alias: "Thought: Perishing Democracy"
type: THOUGHT
en_content: "Government of, by and for the People is perishing from the Earth!"
parent: "topic.MORALITY"
tags:
- government
- democracy
- perishing
- society
- morality
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jul-2013b)
CREATE (t:THOUGHT {
    name: "thought.PERISHING DEMOCRACY",
    alias: "Thought: Perishing Democracy",
    parent: "topic.MORALITY",
    tags: ['government', 'democracy', 'perishing', 'society', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PERISHING DEMOCRACY",
    en_title: "Perishing Democracy",
    en_content: "Government of, by and for the People is perishing from the Earth!",
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
WHERE t.name = "thought.PERISHING DEMOCRACY" AND c.name = "content.PERISHING DEMOCRACY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PERISHING DEMOCRACY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.PERISHING DEMOCRACY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >PERISHING DEMOCRACY" }]->(child);
```
