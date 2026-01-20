---
name: topic.MERCY
alias: "Topic: Compassion"
type: TOPIC
parent: topic.LAW
tags:
- compassion
- leniency
- clemency
- empathy
- sympathy
neo4j: true
ptopic: "[[topic-LAW]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.MERCY",
    alias: "Topic: Compassion",
    parent: "topic.LAW",
    tags: ["compassion", "leniency", "clemency", "empathy", "sympathy"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.MERCY",
    en_title: "MERCY",
    en_content: "Compassion or forbearance shown to an offender or to one subject to another’s power.",
    es_title: "MISERICORDIA",
    es_content: "Compasión o tolerancia mostrada a un ofensor o a uno sujeto al poder de otro.",
    fr_title: "MISÉRICORDE",
    fr_content: "Compassion ou indulgence témoignée à un délinquant ou à une personne soumise au pouvoir d'autrui.",
    hi_title: "दया",
    hi_content: "किसी अपराधी या किसी अन्य की शक्ति के अधीन व्यक्ति के प्रति दिखाई गई करुणा या सहनशीलता।",
    zh_title: "Cíbēi",
    zh_content: "Duì zuìfàn huò shòu tā rén quánlì zhī pèi zhě fǎn xiǎn de cíbēi huò rěnràng."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.MERCY"})
MATCH (d:DESCRIPTION {name: "desc.MERCY"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.MERCY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.LAW"
MATCH (c:TOPIC)
WHERE c.name = "topic.MERCY"
MERGE (p)-[:HAS_CHILD {name: "edge.LAW->MERCY"}]->(c);

```
