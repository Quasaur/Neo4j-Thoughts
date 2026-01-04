---
name: "thought.ALWAYS ADVENTIST"
alias: "Thought: Always Adventist"
type: THOUGHT
en_content: "A part of me will always be Adventist, I guess (smile)."
parent: "topic.RELIGION"
tags:
- identity
- religion
- adventism
- reflection
- faith
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.ALWAYS ADVENTIST",
    alias: "Thought: Always Adventist",
    parent: "topic.RELIGION",
    tags: ['identity', 'religion', 'adventism', 'reflection', 'faith'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ALWAYS ADVENTIST",
    en_title: "Always Adventist",
    en_content: "A part of me will always be Adventist, I guess (smile).",
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
WHERE t.name = "thought.ALWAYS ADVENTIST" AND c.name = "content.ALWAYS ADVENTIST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALWAYS ADVENTIST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.ALWAYS ADVENTIST"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >ALWAYS ADVENTIST" }]->(child);
```
