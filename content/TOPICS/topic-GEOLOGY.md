---
name: topic.GEOLOGY
alias: "Topic Rock Strata"
type: TOPIC
parent: topic.HUMANITY
tags:
- rocks
- strata
- layers
- earth
- land
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.GEOLOGY",
    alias: "Topic Rock Strata",
    parent: "topic.HUMANITY",
    tags: ["rocks", "strata", "layers", "earth", "land"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.GEOLOGY",
    en_title: "GEOLOGY",
    en_content: "Study of the solid matter of a celestial body.",
    es_title: "GEOLOGÍA",
    es_content: "Estudio de la materia sólida de un cuerpo celeste.",
    fr_title: "GÉOLOGIE",
    fr_content: "Étude de la matiere solide d'un corps céleste.",
    hi_title: "भूगर्भ शास्त्र",
    hi_content: "किसी आकाशीय पिंड के ठोस पदार्थ का अध्ययन।",
    zh_title: "Dìzhì",
    zh_content: "Tiāntǐ gùtǐ wùzhí de yánjiū."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.GEOLOGY"})
MATCH (d:DESCRIPTION {name: "desc.GEOLOGY"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.GEOLOGY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.HUMANITY"
MATCH (c:TOPIC)
WHERE c.name = "topic.GEOLOGY"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->GEOLOGY"}]->(c);

```
