---
type: TOPIC
name: "topic.HEALTH"
alias: "Topic: Health and Nutrition"
parent: "topic.HUMANITY"
en_content: "The condition of being sound in body, mind, or spirit; freedom from physical disease or pain; the general condition of the body."
tags: ["nutrition", "exercise", "lifestyle", "physique", "mental"]
ptopic: "[[topic-HUMANITY]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.HEALTH",
    alias: "Topic: Health and Nutrition",
    parent: "topic.HUMANITY",
    tags: ["nutrition", "exercise", "lifestyle", "physique", "mental"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.HEALTH",
    en_title: "Topic: Health and Nutrition",
    en_content: "The condition of being sound in body, mind, or spirit; freedom from physical disease or pain; the general condition of the body.",
    es_title: "Tema: Salud y Nutrición",
    es_content: "La condición de estar sano de cuerpo, mente o espíritu; libertad de enfermedad física o dolor; la condición general del cuerpo.",
    fr_title: "Sujet : Santé et nutrition",
    fr_content: "L’état d’être sain de corps, d’esprit ou d’âme ; l’absence de maladie physique ou de douleur ; l’état général du corps.",
    hi_title: "विषय: स्वास्थ्य और पोषण",
    hi_content: "शरीर, मन या आत्मा के स्वस्थ होने की स्थिति; शारीरिक रोग या दर्द से मुक्ति; शरीर की सामान्य स्थिति।",
    zh_title: "Zhǔtí: Jiànkāng yǔ yíngyǎng",
    zh_content: "Shēntǐ, xīnzhì huò jīngshén jiànquán de zhuàngtài; méiyǒu shēntǐ jíbìng huò téngtòng; shēntǐ de zǒngtǐ zhuàngkuàng."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.HEALTH"})
MATCH (d:DESCRIPTION {name: "desc.HEALTH"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.HEALTH"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.HUMANITY"
MATCH (c:TOPIC)
WHERE c.name = "topic.HEALTH"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->HEALTH"}]->(c);

```
