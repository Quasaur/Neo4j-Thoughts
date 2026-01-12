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
neo4j: false
ptopic: 
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
    es_title: "Iglesia Trabajo Bienestar",
    es_content: "El bienestar no es el trabajo del gobierno; es el trabajo de la Iglesia (Mateo 25:31-46).",
    fr_title: "Église Travail Aide Sociale",
    fr_content: "L'aide sociale n'est pas le travail du gouvernement; c'est le travail de l'Église (Matthieu 25:31-46).",
    hi_title: "कल्याण कार्य चर्च",
    hi_content: "कल्याण सरकार का काम नहीं है; यह चर्च का काम है (मत्ती 25:31-46)।",
    zh_title: "Fulizhi Gongzuo Jiaohui",
    zh_content: "Fulizhi bushi zhengfu de gongzuo; zhe shi jiaohui de gongzuo (Mataifuyin 25:31-46)."
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
