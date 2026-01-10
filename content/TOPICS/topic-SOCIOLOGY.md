---
name: topic.SOCIOLOGY
alias: "Topic: Social Structures Built by the Masses"
type: TOPIC
parent: topic.HUMANITY
tags:
- humanity
- relations
- interactions
- groups
- organization
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.SOCIOLOGY",
    alias: "Topic: Social Structures Built by the Masses",
    parent: "topic.HUMANITY",
    tags: ["humanity", "relations", "interactions", "groups", "organization"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.SOCIOLOGY",
    en_title: "SOCIOLOGY",
    en_content: "The science of society, social institutions, and social relationships.",
    es_title: "SOCIOLOGÍA",
    es_content: "La ciencia de la sociedad, las instituciones sociales y las relaciones sociales.",
    fr_title: "SOCIOLOGIE",
    fr_content: "La science de la société, des institutions sociales et des relations sociales.",
    hi_title: "समाजशास्त्र",
    hi_content: "समाज, सामाजिक संस्थाओं और सामाजिक संबंधों का विज्ञान।",
    zh_title: "Shèhuì xué",
    zh_content: "Shèhuì, shèhuì zhìdù hé shèhuì guānxì de kēxué."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.SOCIOLOGY" AND d.name = "desc.SOCIOLOGY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.SOCIOLOGY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.HUMANITY" AND c.name = "topic.SOCIOLOGY"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->SOCIOLOGY"}]->(c);

```
