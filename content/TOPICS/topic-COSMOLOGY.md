---
type: TOPIC
name: "topic.COSMOLOGY"
alias: "Topic: Humanity's World Views"
parent: "topic.HUMANITY"
en_content: "The study of the social belief systems humans have held across different times and places. Scientific cosmology involves studying the universe through astronomy and physics."
tags: ["metaphysics", "astronomy", "universe", "social", "scientific"]
ptopic: "[[topic-HUMANITY]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.COSMOLOGY",
    alias: "Topic: Humanity's World Views",
    parent: "topic.HUMANITY",
    tags: ["metaphysics", "astronomy", "universe", "social", "scientific"],
    level: 3
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.COSMOLOGY",
    en_title: "Topic: Humanity's World Views",
    en_content: "The study of the social belief systems humans have held across different times and places. Scientific cosmology involves studying the universe through astronomy and physics.",
    es_title: "Tema: Visiones del mundo de la humanidad",
    es_content: "El estudio de los sistemas de creencias sociales que los humanos han mantenido a través de diferentes tiempos y lugares. La cosmología científica implica estudiar el universo a través de la astronomía y la física.",
    fr_title: "Sujet : Les visions du monde de l'humanité",
    fr_content: "L'étude des systèmes de croyances sociales que les humains ont eus à travers différents temps et lieux. La cosmologie scientifique implique l'étude de l'univers à travers l'astronomie et la physique.",
    hi_title: "विषय: दुनिया के बारे में इंसानियत का नज़रिया",
    hi_content: "विभिन्न समयों और स्थानों में मनुष्यों द्वारा रखे गए सामाजिक विश्वास प्रणालियों का अध्ययन। वैज्ञानिक ब्रह्मांड विज्ञान में खगोल विज्ञान और भौतिकी के माध्यम से ब्रह्मांड का अध्ययन करना शामिल है।",
    zh_title: "Zhǔtí: Rénlèi de shìjièguān",
    zh_content: "Rénlèi zài bùtóng shíjiān hé dìdiǎn chíyǒu de shèhuì xìnyǎng xìtǒng de yánjiū. Kēxué yǔzhòu xué shèjí tōngguò tiānwénxué hé wùlǐxué yánjiū yǔzhòu."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.COSMOLOGY"})
MATCH (d:DESCRIPTION {name: "desc.COSMOLOGY"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.COSMOLOGY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.HUMANITY"
MATCH (c:TOPIC)
WHERE c.name = "topic.COSMOLOGY"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->COSMOLOGY"}]->(c);

```
