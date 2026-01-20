---
name: topic.ASTROPHYSICS
alias: "Topic: The Physics of Astronomy"
type: TOPIC
parent: topic.COSMOLOGY
en_content: "A branch of astronomy dealing especially with the behavior, physical properties, and dynamic processes of celestial objects and phenomena."
tags:
- space_time
- radiation
- nucleosynthesis
- high_energy
- cosmic_plasma
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.ASTROPHYSICS",
    alias: "Topic: This History of Humanity's World Views",
    parent: "topic.COSMOLOGY",
    tags: ["space_time", "radiation", "nucleosynthesis", "high_energy", "cosmic_plasma"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.ASTROPHYSICS",
    en_title: "Astrophysics",
    en_content: "A branch of astronomy dealing especially with the behavior, physical properties, and dynamic processes of celestial objects and phenomena.",
    es_title: "Astrofísica",
    es_content: "Rama de la astronomía que se ocupa especialmente del comportamiento, las propiedades físicas y los procesos dinámicos de los objetos y fenómenos celestes.",
    fr_title: "Astrophysique",
    fr_content: "Branche de l'astronomie qui étudie notamment le comportement, les propriétés physiques et les processus dynamiques des objets et phénomènes célestes.",
    hi_title: "एस्ट्रोफिजिक्स",
    hi_content: "खगोल विज्ञान की एक शाखा जो विशेष रूप से खगोलीय वस्तुओं और घटनाओं के व्यवहार, भौतिक गुणों और गतिशील प्रक्रियाओं से संबंधित है।",
    zh_title: "Tiāntǐ wùlǐ xué",
    zh_content: "tiānwénxué de yīgè fēnzhī, zhǔyào yánjiū tiāntǐ de xíngwéi, wùlǐ xìngzhì hé dònglì xué guòchéng."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.ASTROPHYSICS"})
MATCH (d:DESCRIPTION {name: "desc.ASTROPHYSICS"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.COSMOLOGY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.COSMOLOGY"
MATCH (c:TOPIC)
WHERE c.name = "topic.ASTROPHYSICS"
MERGE (p)-[:HAS_CHILD {name: "edge.COSMOLOGY->ASTROPHYSICS"}]->(c);

```
