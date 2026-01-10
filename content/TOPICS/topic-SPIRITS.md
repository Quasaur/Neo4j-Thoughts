---
name: topic.SPIRITS
alias: "Topic Children of the Holy Spirit"
type: TOPIC
parent: topic.CREATION
tags:
- life
- attitude
- supernatural
- being
- incorporeals
neo4j: true
ptopic: "[[topic-CREATION]]"
level: 3
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.SPIRITS",
    alias: "Topic Children of the Holy Spirit",
    parent: "topic.CREATION",
    tags: ["life", "attitude", "supernatural", "being", "incorporeals"],
    level: 3
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.SPIRITS",
    en_title: "SPIRITS",
    en_content: "The animating or vital Principle held to give life to physical organisms; supernatural being or essence.",
    es_title: "ESPÍRITUS",
    es_content: "El Principio animador o vital que se sostiene que da vida a los organismos físicos; ser o esencia sobrenatural.",
    fr_title: "ESPRITS",
    fr_content: "Le Principe animateur ou vital tenu pour donner la vie aux organismes physiques ; être ou essence surnaturel.",
    hi_title: "आत्मायें",
    hi_content: "वह चेतन या प्राणदायक सिद्धांत जिसे भौतिक जीवों को जीवन देने वाला माना जाता है; अलौकिक प्राणी या सार।",
    zh_title: "Línglèi",
    zh_content: "Wéichí wùlǐ shēngwù shēngmìng de qūdòng huò shēngmìng yuánzé; chāozìrán de cúnzài huò běnzhì."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.SPIRITS" AND d.name = "desc.SPIRITS"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.SPIRITS"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.CREATION" AND c.name = "topic.SPIRITS"
MERGE (p)-[:HAS_CHILD {name: "edge.CREATION->SPIRITS"}]->(c);

```
