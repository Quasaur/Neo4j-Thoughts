---
type: TOPIC
name: "topic.ASTROPHYSICS"
alias: "Topic: The Physics of Astronomy"
parent: "topic.COSMOLOGY"
en_content: "A branch of astronomy dealing especially with the behavior, physical properties, and dynamic processes of celestial objects and phenomena."
tags: ["space_time", "radiation", "nucleosynthesis", "high_energy", "cosmic_plasma"]
ptopic: "[[topic-COSMOLOGY]]"
level: 5
neo4j: true
verified: true
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.ASTROPHYSICS",
    alias: "Topic: The Physics of Astronomy",
    parent: "topic.COSMOLOGY",
    tags: ["space_time", "radiation", "nucleosynthesis", "high_energy", "cosmic_plasma"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.ASTROPHYSICS",
    en_title: "Topic: The Physics of Astronomy",
    en_content: "A branch of astronomy dealing especially with the behavior, physical properties, and dynamic processes of celestial objects and phenomena.",
    es_title: "Tema: La física de la astronomía",
    es_content: "Rama de la astronomía que se ocupa especialmente del comportamiento, las propiedades físicas y los procesos dinámicos de los objetos y fenómenos celestes.",
    fr_title: "Sujet : La physique de l'astronomie",
    fr_content: "Branche de l'astronomie qui étudie notamment le comportement, les propriétés physiques et les processus dynamiques des objets et phénomènes célestes.",
    hi_title: "विषय: खगोल विज्ञान का भौतिकी",
    hi_content: "खगोल विज्ञान की एक शाखा जो विशेष रूप से खगोलीय वस्तुओं और घटनाओं के व्यवहार, भौतिक गुणों और गतिशील प्रक्रियाओं से संबंधित है।",
    zh_title: "Zhǔtí: Tiānwénxué wùlǐ xué",
    zh_content: "tiānwénxué de yīgè fēnzhī, zhǔyào yánjiū tiāntǐ de xíngwéi, wùlǐ xìngzhì hé dònglì xué guòchéng."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.ASTROPHYSICS"})
MATCH (d:DESCRIPTION {name: "desc.ASTROPHYSICS"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ASTROPHYSICS"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.COSMOLOGY"
MATCH (c:TOPIC)
WHERE c.name = "topic.ASTROPHYSICS"
MERGE (p)-[:HAS_CHILD {name: "edge.COSMOLOGY->ASTROPHYSICS"}]->(c);

```
