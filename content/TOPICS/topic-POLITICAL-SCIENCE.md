---
name: topic.POLITICAL-SCIENCE
alias: "Topic Political Theory"
type: TOPIC
parent: topic.HUMANITY
tags:
- patriotism
- chauvinism
- nativism
- governing
- power
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.POLITICAL-SCIENCE",
    alias: "Topic Political Theory",
    parent: "topic.HUMANITY",
    tags: ["patriotism", "chauvinism", "nativism", "governing", "power"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.POLITICAL-SCIENCE",
    en_title: "POLITICAL SCIENCE",
    en_content: "Exalting one nation above all others and placing primary emphasis on promotion of its culture and interests as opposed to those of other nations.",
    es_title: "CIENCIA POLÍTICA",
    es_content: "Exaltar una nación por encima de todas las demás y poner énfasis principal en la promoción de su cultura e intereses en oposición a los de otras naciones.",
    fr_title: "SCIENCE POLITIQUE",
    fr_content: "Exalter une nation au-dessus de toutes les autres et mettre l'accent principalement sur la promotion de sa culture et de ses intérêts par opposition à ceux des autres nations.",
    hi_title: "राजनीति विज्ञान",
    hi_content: "एक राष्ट्र को अन्य सभी से ऊपर उठाना और अन्य राष्ट्रों की संस्कृति और हितों के विपरीत अपनी संस्कृति और हितों को बढ़ावा देने पर प्राथमिक जोर देना।",
    zh_title: "Zhèngzhì xué",
    zh_content: "Gāojǔ yīgè guójiā chāoguò suǒyǒu qítā guójiā, bìngqiě shǒu yào qiángdiào cùjìn qí wénhuà hé lìyì, yǔ qítā guójiā xiāngfǎn."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.POLITICAL-SCIENCE"})
MATCH (d:DESCRIPTION {name: "desc.POLITICAL-SCIENCE"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.POLITICAL-SCIENCE"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.HUMANITY"
MATCH (c:TOPIC)
WHERE c.name = "topic.POLITICAL-SCIENCE"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->POLITICAL-SCIENCE"}]->(c);

```
