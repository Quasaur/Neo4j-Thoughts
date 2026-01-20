---
name: "thought.SHOWING MERCY"
alias: "Thought: Showing Mercy"
type: THOUGHT
en_content: "Everybody wants Mercy...few show Mercy."
parent: "topic.MORALITY"
tags:
- mercy
- morality
- character
- compassion
- judgment
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jan-2011)
CREATE (t:THOUGHT {
    name: "thought.SHOWING MERCY",
    alias: "Thought: Showing Mercy",
    parent: "topic.MORALITY",
    tags: ['mercy', 'morality', 'character', 'compassion', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SHOWING MERCY",
    en_title: "Showing Mercy",
    en_content: "Everybody wants Mercy...few show Mercy.",
    es_title: "Mostrar Misericordia",
    es_content: "Todos quieren Misericordia...pocos muestran Misericordia.",
    fr_title: "Faire Miséricorde",
    fr_content: "Tout le monde veut la Miséricorde...peu font Miséricorde.",
    hi_title: "दया दिखाना",
    hi_content: "सभी दया चाहते हैं...कुछ ही दया दिखाते हैं।",
    zh_title: "Xian Shi Ci Bei",
    zh_content: "Ren Ren Dou Xiang Yao Ci Bei...Que Shao You Ren Xian Shi Ci Bei."
});

MATCH (t:THOUGHT {name: "thought.SHOWING MERCY"})
MATCH (c:CONTENT {name: "content.SHOWING MERCY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHOWING MERCY" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.SHOWING MERCY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SHOWING MERCY" }]->(child);
```
