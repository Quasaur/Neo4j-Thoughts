---
name: topic.HISTORY
alias: "Topic: Chronology"
type: TOPIC
parent: topic.HUMANITY
tags:
- annals
- chronicles
- biography
- records
- journal
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.HISTORY",
    alias: "Topic: Chronology",
    parent: "topic.HUMANITY",
    tags: ["annals", "chronicles", "biography", "records", "journal"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.HISTORY",
    en_title: "HISTORY",
    en_content: "An account of important events in the order in which they happened",
    es_title: "HISTORIA",
    es_content: "Un relato de eventos importantes en el orden en que ocurrieron.",
    fr_title: "HISTOIRE",
    fr_content: "Un récit d'événements importants dans l'ordre où ils se sont produits.",
    hi_title: "इतिहास",
    hi_content: "महत्वपूर्ण घटनाओं का एक विवरण जिस क्रम में वे घटित हुए।",
    zh_title: "Lìshǐ",
    zh_content: "Ànzhào shìjiàn fāshēng de shùnxù duì zhòngyào shìjiàn de jìshù."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.HISTORY"})
MATCH (d:DESCRIPTION {name: "desc.HISTORY"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.HISTORY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.HUMANITY"
MATCH (c:TOPIC)
WHERE c.name = "topic.HISTORY"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->HISTORY"}]->(c);

```
