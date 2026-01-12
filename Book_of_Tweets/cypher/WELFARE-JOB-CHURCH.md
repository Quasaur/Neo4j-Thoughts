---
name: "thought.WELFARE JOB CHURCH"
alias: "Thought: Welfare Job Church"
type: THOUGHT
en_content: "Welfare is not the job of government; it's the job of the Church (Matthew 25:31-46)."
parent: "topic.RELIGION"
tags:
- welfare
- church
- government
- religion
- society
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Jul-2013)
CREATE (t:THOUGHT {
    name: "thought.WELFARE JOB CHURCH",
    alias: "Thought: Welfare Job Church",
    parent: "topic.RELIGION",
    tags: ['welfare', 'church', 'government', 'religion', 'society'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.WELFARE JOB CHURCH",
    en_title: "Welfare Job Church",
    en_content: "Welfare is not the job of government; it's the job of the Church (Matthew 25:31-46).",
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
WHERE t.name = "thought.WELFARE JOB CHURCH" AND c.name = "content.WELFARE JOB CHURCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WELFARE JOB CHURCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.WELFARE JOB CHURCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >WELFARE JOB CHURCH" }]->(child);
```
