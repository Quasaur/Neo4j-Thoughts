---
name: topic.FAITH
alias: "Topic: That Faith by which One is Aligned with the Spirit and Will of God"
type: TOPIC
parent: topic.ATTITUDE
tags:
- truth
- doctrine
- belief
- confidence
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.FAITH",
    alias: "Topic: That Faith by which One is Aligned with the Spirit and Will of God",
    parent: "topic.ATTITUDE",
    tags: ["truth", "doctrine", "belief", "confidence"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.FAITH",
    en_title: "FAITH",
    en_content: "Confidence in the Words of God that inspires intent, speech and action.",
    es_title: "FE",
    es_content: "Confianza en las Palabras de Dios que inspiran intención, palabra y acción.",
    fr_title: "FOI",
    fr_content: "Confiance dans les paroles de Dieu qui inspirent l’intention, la parole et l’action.",
    hi_title: "आस्था",
    hi_content: "परमेश्वर के वचनों में विश्वास जो इरादे, भाषण और कार्य को प्रेरित करता है।",
    zh_title: "Xìnyǎng",
    zh_content: "Duì shàngdì zhī yán de xìnxīn kěyǐ jīfā yìtú, yányǔ hé xíngdòng."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.FAITH"})
MATCH (d:DESCRIPTION {name: "desc.FAITH"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.FAITH"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.ATTITUDE"
MATCH (c:TOPIC)
WHERE c.name = "topic.FAITH"
MERGE (p)-[:HAS_CHILD {name: "edge.ATTITUDE->FAITH"}]->(c);

```
