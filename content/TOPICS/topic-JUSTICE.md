---
name: topic.JUSTICE
alias: "Topic: Equity Between All Peoples"
type: TOPIC
parent: topic.LAW
tags:
- equity
- fairness
- impartiality
- equitability
- honor
neo4j: true
ptopic: "[[topic-LAW]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.JUSTICE",
    alias: "Topic: Equity Between All Peoples",
    parent: "topic.LAW",
    tags: ["equity", "fairness", "impartiality", "equitability", "honor"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.JUSTICE",
    en_title: "JUSTICE",
    en_content: "The practice or instance of giving to others what is their due.",
    es_title: "JUSTICIA",
    es_content: "La práctica o instancia de dar a otros lo que les corresponde.",
    fr_title: "JUSTICE",
    fr_content: "La pratique ou l'exemple de donner aux autres ce qui leur est dû.",
    hi_title: "न्याय",
    hi_content: "दूसरों को उनका हक देने का अभ्यास या उदाहरण।",
    zh_title: "Zhèngyì",
    zh_content: "Gěiyǔ tārén yīng dé zhī wù de shíjiàn huò shílì."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.JUSTICE" AND d.name = "desc.JUSTICE"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.JUSTICE"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.LAW" AND c.name = "topic.JUSTICE"
MERGE (p)-[:HAS_CHILD {name: "edge.LAW->JUSTICE"}]->(c);

```
