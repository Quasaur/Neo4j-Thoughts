---
type: TOPIC
name: "topic.FAITH"
alias: "Topic: Faith from the Spirit, Will and Word of God"
parent: "topic.ATTITUDE"
en_content: "Confidence in the Words of God that inspires intent, speech and action."
tags: ["truth", "doctrine", "belief", "confidence", "trust"]
ptopic: "[[topic-ATTITUDE]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.FAITH",
    alias: "Topic: Faith from the Spirit, Will and Word of God",
    parent: "topic.ATTITUDE",
    tags: ["truth", "doctrine", "belief", "confidence", "trust"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.FAITH",
    en_title: "Topic: Faith from the Spirit, Will and Word of God",
    en_content: "Confidence in the Words of God that inspires intent, speech and action.",
    es_title: "Tema: Fe desde el Espíritu, Voluntad y Palabra de Dios",
    es_content: "Confianza en las Palabras de Dios que inspiran intención, palabra y acción.",
    fr_title: "Sujet : La foi issue de l'Esprit, de la Volonté et de la Parole de Dieu",
    fr_content: "Confiance dans les paroles de Dieu qui inspirent l’intention, la parole et l’action.",
    hi_title: "विषय: ईश्वर की आत्मा, इच्छा और वचन से विश्वास",
    hi_content: "परमेश्वर के वचनों में विश्वास जो इरादे, भाषण और कार्य को प्रेरित करता है।",
    zh_title: "zhǔ tí : lái zì shén de líng 、 zhǐ yì hé huà yǔ de xìn xīn",
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
