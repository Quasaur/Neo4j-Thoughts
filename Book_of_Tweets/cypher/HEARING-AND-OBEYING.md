---
name: "thought.HEARING AND OBEYING"
alias: "Thought: Hearing And Obeying"
type: THOUGHT
en_content: "Half the battle: Hearing God's Voice; the Other Half: obeying it."
parent: "topic.SPIRITUALITY"
tags:
- obedience
- guidance
- spirituality
- listening
- faith
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Aug-2010)
CREATE (t:THOUGHT {
    name: "thought.HEARING AND OBEYING",
    alias: "Thought: Hearing And Obeying",
    parent: "topic.SPIRITUALITY",
    tags: ['obedience', 'guidance', 'spirituality', 'listening', 'faith'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEARING AND OBEYING",
    en_title: "Hearing And Obeying",
    en_content: "Half the battle: Hearing God's Voice; the Other Half: obeying it.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HEARING AND OBEYING" AND c.name = "content.HEARING AND OBEYING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEARING AND OBEYING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HEARING AND OBEYING"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEARING AND OBEYING" }]->(child);
```
