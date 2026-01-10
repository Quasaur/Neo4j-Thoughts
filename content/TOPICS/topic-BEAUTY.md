---
name: topic.BEAUTY
alias: "Topic: Beauty of Body or Character"
type: TOPIC
parent: topic.HEALTH
tags:
- attractiveness
- loveliness
- comeliness
neo4j: true
ptopic: "[[topic-HEALTH]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.BEAUTY",
    alias: "Topic: Beauty of Body or Character",
    parent: "topic.HEALTH",
    tags: ["attractiveness", "loveliness", "comeliness"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.BEAUTY",
    en_title: "BEAUTY",
    en_content: "The quality or group of qualities in a person or thing that gives pleasure to the senses or the mind; a person (especially a woman) who is beautiful; an excellent or appealing quality.",
    es_title: "BELLEZA",
    es_content: "La cualidad o grupo de cualidades de una persona o cosa que da placer a los sentidos o a la mente; una persona (especialmente una mujer) que es bella; una cualidad excelente o atractiva.",
    fr_title: "BEAUTÉ",
    fr_content: "La qualité ou le groupe de qualités d'une personne ou d'une chose qui procure du plaisir aux sens ou à l'esprit ; une personne (en particulier une femme) qui est belle ; une qualité excellente ou attrayante.",
    hi_title: "सुंदरता",
    hi_content: "किसी व्यक्ति या वस्तु में वह गुण या गुणों का समूह जो इन्द्रियों या मन को प्रसन्नता देता है; कोई व्यक्ति (विशेषकर स्त्री) जो सुन्दर है; कोई उत्कृष्ट या आकर्षक गुण।",
    zh_title: "Měilì",
    zh_content: "Gèrén huò yī jiàn shìwù de pǐnzhí huò pǐnzhí qún, néng gěi gǎnguān huò xīnlíng dàilái yúyuè; měilì de rén (yóuqí shì nǚrén); yōuxiù huò yǒu xīyǐnlì de pǐnzhí."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.BEAUTY" AND d.name = "desc.BEAUTY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.BEAUTY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.HEALTH" AND c.name = "topic.BEAUTY"
MERGE (p)-[:HAS_CHILD {name: "edge.HEALTH->BEAUTY"}]->(c);

```
