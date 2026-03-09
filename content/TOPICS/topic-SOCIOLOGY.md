---
type: TOPIC
name: "topic.SOCIOLOGY"
alias: "Topic: Social Structures"
parent: "topic.SOCIAL SCIENCES"
en_content: "The science of society, social institutions, and social relationships."
tags: ["humanity", "relations", "interactions", "groups", "organization"]
ptopic: "[[topic-SOCIAL-SCIENCES]]"
level: 5
neo4j: true
verified: true
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.SOCIOLOGY",
    alias: "Topic: Social Structures",
    parent: "topic.SOCIAL SCIENCES",
    tags: ["humanity", "relations", "interactions", "groups", "organization"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.SOCIOLOGY",
    en_title: "Topic: Social Structures",
    en_content: "The science of society, social institutions, and social relationships.",
    es_title: "Tema: Estructuras sociales",
    es_content: "La ciencia de la sociedad, las instituciones sociales y las relaciones sociales.",
    fr_title: "Sujet : Structures sociales",
    fr_content: "La science de la société, des institutions sociales et des relations sociales.",
    hi_title: "विषय: सामाजिक संरचनाएं",
    hi_content: "समाज, सामाजिक संस्थाओं और सामाजिक संबंधों का विज्ञान।",
    zh_title: "Zhǔtí: Shèhuì jiégòu",
    zh_content: "Shèhuì, shèhuì zhìdù hé shèhuì guānxì de kēxué."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.SOCIOLOGY"})
MATCH (d:DESCRIPTION {name: "desc.SOCIOLOGY"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.SOCIOLOGY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.SOCIAL SCIENCES"
MATCH (c:TOPIC)
WHERE c.name = "topic.SOCIOLOGY"
MERGE (p)-[:HAS_CHILD {name: "edge.SOCIAL SCIENCES->SOCIOLOGY"}]->(c);

```
