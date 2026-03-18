---
type: THOUGHT
name: "thought.ACTS OF THE APOSTLES"
alias: "Thought: Acts of the Apostles"
parent: "topic.THE BIBLE"
en_content: "The Acts of the Apostles mentions thirty-two countries, fifty-four cities and nine islands without a factual or historical error."
tags: ["bible", "luke", "chronology", "geography", "accuracy"]
ptopic: "[[topic-THE BIBLE]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ACTS OF THE APOSTLES",
    alias: "Thought: Acts of the Apostles",
    parent: "topic.THE BIBLE",
    tags: ["bible", "luke", "chronology", "geography", "accuracy"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.ACTS OF THE APOSTLES",
    ctype: "THOUGHT",
    en_title: "Acts of the Apostles",
    en_content: "The Acts of the Apostles mentions thirty-two countries, fifty-four cities and nine islands without a factual or historical error.",
    es_title: "Hechos de los Apóstoles",
    es_content: "Los Hechos de los Apóstoles mencionan treinta y dos países, cincuenta y cuatro ciudades y nueve islas sin ningún error fáctico o histórico.",
    fr_title: "Actes des Apôtres",
    fr_content: "Les Actes des Apôtres mentionnent trente-deux pays, cinquante-quatre villes et neuf îles sans erreur factuelle ou historique.",
    hi_title: "प्रेरितों के कार्य",
    hi_content: "प्रेरितों के अधिनियम में बिना किसी तथ्यात्मक या ऐतिहासिक त्रुटि के बत्तीस देशों, चौवन शहरों और नौ द्वीपों का उल्लेख है।",
    zh_title: "shǐ tú xíng chuán",
    zh_content: "《 shǐ tú xíng chuán 》 tí dào le sān shí èr gè guó jiā 、 wǔ shí sì gè chéng shì hé jiǔ gè dǎo yǔ ， méi yǒu rèn hé shì shí huò lì shǐ cuò wù 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ACTS OF THE APOSTLES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-BIBLE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE BIBLE->ACTS OF THE APOSTLES"
RETURN t, parent;
```
