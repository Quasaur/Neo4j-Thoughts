---
name: "thought.EVOLUTION AS RELIGION"
alias: "Thought: Evolution As Religion"
type: THOUGHT
en_content: "Evolution is a RELIGION, evidence for which has been dwindling as scientific observation has grown more sophisticated."
parent: "topic.PHILOSOPHY"
tags:
- evolution
- religion
- philosophy
- truth
- science
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Nov-2010c)
CREATE (t:THOUGHT {
    name: "thought.EVOLUTION AS RELIGION",
    alias: "Thought: Evolution As Religion",
    parent: "topic.PHILOSOPHY",
    tags: ['evolution', 'religion', 'philosophy', 'truth', 'science'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVOLUTION AS RELIGION",
    en_title: "Evolution As Religion",
    en_content: "Evolution is a RELIGION, evidence for which has been dwindling as scientific observation has grown more sophisticated.",
    es_title: "La evolución como religión",
    es_content: "La evolución es una RELIGIÓN, cuya evidencia ha ido disminuyendo a medida que la observación científica se ha vuelto más sofisticada.",
    fr_title: "L'évolution en tant que religion",
    fr_content: "L’évolution est une RELIGION dont les preuves diminuent à mesure que l’observation scientifique devient plus sophistiquée.",
    hi_title: "धर्म के रूप में विकास",
    hi_content: "विकास एक धर्म है, जिसके प्रमाण कम होते जा रहे हैं क्योंकि वैज्ञानिक अवलोकन अधिक परिष्कृत हो गया है।",
    zh_title: "作为宗教的进化论",
    zh_content: "进化论是一种宗教，随着科学观察变得更加复杂，其证据却在不断减少。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVOLUTION AS RELIGION" AND c.name = "content.EVOLUTION AS RELIGION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EVOLUTION AS RELIGION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.EVOLUTION AS RELIGION"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >EVOLUTION AS RELIGION" }]->(child);
```
