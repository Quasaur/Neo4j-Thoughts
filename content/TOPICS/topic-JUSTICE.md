---
type: TOPIC
name: "topic.JUSTICE"
alias: "Topic: Equity Between All Peoples"
parent: "topic.LAW"
en_content: "The practice or instance of giving to others what is their due."
tags: ["equity", "fairness", "impartiality", "equitability", "honor"]
ptopic: "[[topic-LAW]]"
level: 5
neo4j: true
verified: true
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
    en_title: "Topic: Equity Between All Peoples",
    en_content: "The practice or instance of giving to others what is their due.",
    es_title: "Tema: Equidad entre todos los pueblos",
    es_content: "La práctica o instancia de dar a otros lo que les corresponde.",
    fr_title: "Sujet : L'équité entre tous les peuples",
    fr_content: "La pratique ou l'exemple de donner aux autres ce qui leur est dû.",
    hi_title: "विषय: सभी लोगों के बीच समानता",
    hi_content: "दूसरों को उनका हक देने का अभ्यास या उदाहरण।",
    zh_title: "Zhǔtí: Rén rén píngděng",
    zh_content: "Gěiyǔ tārén yīng dé zhī wù de shíjiàn huò shílì."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.JUSTICE"})
MATCH (d:DESCRIPTION {name: "desc.JUSTICE"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.JUSTICE"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.LAW"
MATCH (c:TOPIC)
WHERE c.name = "topic.JUSTICE"
MERGE (p)-[:HAS_CHILD {name: "edge.LAW->JUSTICE"}]->(c);

```
