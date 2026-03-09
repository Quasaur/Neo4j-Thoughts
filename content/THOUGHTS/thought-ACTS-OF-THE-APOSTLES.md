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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ACTS OF THE APOSTLES" AND c.name = "content.ACTS OF THE APOSTLES"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.ACTS OF THE APOSTLES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-BIBLE" AND child.name = "thought.ACTS OF THE APOSTLES"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-BIBLE->ACTS OF THE APOSTLES"}]->(child);
```
