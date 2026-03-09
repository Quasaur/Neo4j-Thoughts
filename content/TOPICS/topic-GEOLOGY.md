---
type: TOPIC
name: "topic.GEOLOGY"
alias: "Topic: Rock Strata"
parent: "topic.HUMANITY"
en_content: "Study of the solid matter of a celestial body."
tags: ["rocks", "strata", "layers", "earth", "land"]
ptopic: "[[topic-HUMANITY]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.GEOLOGY",
    alias: "Topic: Rock Strata",
    parent: "topic.HUMANITY",
    tags: ["rocks", "strata", "layers", "earth", "land"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.GEOLOGY",
    en_title: "Topic: Rock Strata",
    en_content: "Study of the solid matter of a celestial body.",
    es_title: "Tema: Estratos rocosos",
    es_content: "Estudio de la materia sólida de un cuerpo celeste.",
    fr_title: "Sujet : Strates rocheuses",
    fr_content: "Étude de la matiere solide d'un corps céleste.",
    hi_title: "विषय: चट्टानी स्तर",
    hi_content: "किसी आकाशीय पिंड के ठोस पदार्थ का अध्ययन।",
    zh_title: "Zhǔtí: Yáncéng",
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
