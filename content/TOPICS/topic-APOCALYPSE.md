---
name: topic.APOCALYPSE
alias: "Topic: ESCHATOLOGY"
type: TOPIC
parent: topic.HISTORY
tags:
- eschatology
- last_day
- end_of_the_world
neo4j: true
ptopic: "[[topic-HISTORY]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.APOCALYPSE",
    alias: "Topic: ESCHATOLOGY",
    parent: "topic.HISTORY",
    tags: ["eschatology", "last_day", "end_of_the_world"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.APOCALYPSE",
    en_title: "APOCALYPSE",
    en_content: "Eschatology; the End of all things.",
    es_title: "APOCALIPSIS",
    es_content: "Escatología; el fin de todas las cosas.",
    fr_title: "APOCALYPSE",
    fr_content: "Eschatologie ; la fin de toutes choses.",
    hi_title: "कयामत",
    hi_content: "परलोकविद्या; सभी चीजों का अंत।",
    zh_title: "Qǐshì",
    zh_content: "Mòshìlùn; wànwù de zhōngjié."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.APOCALYPSE" AND d.name = "desc.APOCALYPSE"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.APOCALYPSE"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.HISTORY" AND c.name = "topic.APOCALYPSE"
MERGE (p)-[:HAS_CHILD {name: "edge.HISTORY->APOCALYPSE"}]->(c);

```
