---
name: topic.HEALTH
alias: "Topic: Health and Nutrition"
type: TOPIC
parent: topic.HUMANITY
tags:
- nutrition
- exercise
- lifestyle
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.HEALTH",
    alias: "Topic: Health and Nutrition",
    parent: "topic.HUMANITY",
    tags: ["nutrition", "exercise", "lifestyle"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.HEALTH",
    en_title: "HEALTH",
    en_content: "The condition of being sound in body, mind, or spirit; freedom from physical disease or pain; the general condition of the body.",
    es_title: "SALUD",
    es_content: "La condición de estar sano de cuerpo, mente o espíritu; libertad de enfermedad física o dolor; la condición general del cuerpo.",
    fr_title: "SANTÉ",
    fr_content: "L’état d’être sain de corps, d’esprit ou d’âme ; l’absence de maladie physique ou de douleur ; l’état général du corps.",
    hi_title: "स्वास्थ्य",
    hi_content: "शरीर, मन या आत्मा के स्वस्थ होने की स्थिति; शारीरिक रोग या दर्द से मुक्ति; शरीर की सामान्य स्थिति।",
    zh_title: "Jiànkāng",
    zh_content: "Shēntǐ, xīnzhì huò jīngshén jiànquán de zhuàngtài; méiyǒu shēntǐ jíbìng huò téngtòng; shēntǐ de zǒngtǐ zhuàngkuàng."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.HEALTH" AND d.name = "desc.HEALTH"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.HEALTH"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.HUMANITY" AND c.name = "topic.HEALTH"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->HEALTH"}]->(c);

```
