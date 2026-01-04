---
name: topic.ANTHROPOLOGY
alias: "Topic: The Study of Humanity Throughout its History"
type: TOPIC
parent: topic.HUMANITY
tags:
- cultural
- physical
- archaeology
- linquistic
neo4j: true
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.ANTHROPOLOGY",
    alias: "Topic: The Study of Humanity Throughout its History",
    parent: "topic.HUMANITY",
    tags: ["cultural", "physical", "archaeology", "linquistic", "study"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.ANTHROPOLOGY",
    en_title: "ANTHROPOLOGY",
    en_content: "The study of human beings and their ancestors through time and space and in relation to physical character, environmental and social relations, and culture.",
    es_title: "ANTROPOLOGÍA",
    es_content: "El estudio de los seres humanos y sus antepasados a través del tiempo y el espacio y en relación con el carácter físico, las relaciones ambientales y sociales, y la cultura.",
    fr_title: "ANTHROPOLOGIE",
    fr_content: "L'étude des êtres humains et de leurs ancêtres à travers le temps et l'espace et en relation avec le caractère physique, les relations environnementales et sociales, et la culture.",
    hi_title: "मानव विज्ञान",
    hi_content: "समय और स्थान के आर-पार, और शारीरिक चरित्र, पर्यावरणीय और सामाजिक संबंधों, और संस्कृति के संबंध में मनुष्यों और उनके पूर्वजों का अध्ययन।",
    zh_title: "Rénlèixué",
    zh_content: "Rénlèi jí qí zǔxiān tōngguò shíjiān hé kōngjiān, bìng qiě zài wùlǐ tèzhēng, huánjìng hé shèhuì guānxì yǐjí wénhuà fāngmiàn de yánjiū."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.ANTHROPOLOGY" AND d.name = "desc.ANTHROPOLOGY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ANTHROPOLOGY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.HUMANITY" AND c.name = "topic.ANTHROPOLOGY"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->ANTHROPOLOGY"}]->(c);

```
