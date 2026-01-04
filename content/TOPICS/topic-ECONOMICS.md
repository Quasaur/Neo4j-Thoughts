---
name: topic.ECONOMICS
alias: "Topic: Commerce"
type: TOPIC
parent: topic.HUMANITY
tags:
- consumption
- production
- distribution
neo4j: true
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.ECONOMICS",
    alias: "Topic: Commerce",
    parent: "topic.HUMANITY",
    tags: ["consumption", "production", "distribution"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.ECONOMICS",
    en_title: "ECONOMICS",
    en_content: "Social science concerned chiefly with description and analysis of the production, distribution, and consumption of goods and services.",
    es_title: "ECONOMÍA",
    es_content: "Ciencia social preocupada principalmente por la descripción y el análisis de la producción, distribución y consumo de bienes y servicios.",
    fr_title: "ÉCONOMIE",
    fr_content: "Science sociale concernée principalement par la description et l'analyse de la production, de la distribution et de la consommation de biens et services.",
    hi_title: "अर्थशास्त्र",
    hi_content: "सामाजिक विज्ञान मुख्य रूप से वस्तुओं और सेवाओं के उत्पादन, वितरण और उपभोग के विवरण और विश्लेषण से संबंधित है।",
    zh_title: "Jīngjì",
    zh_content: "Shèhuì kēxué zhǔyào guānzhù shāngpǐn hé fúwù de shēngchǎn, fēnpèi hé xiāofèi de miáoshù hé fēnxī."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.ECONOMICS" AND d.name = "desc.ECONOMICS"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ECONOMICS"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.HUMANITY" AND c.name = "topic.ECONOMICS"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->ECONOMICS"}]->(c);

```
