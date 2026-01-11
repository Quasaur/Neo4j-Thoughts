---
name: "thought.ACTS_OF_THE_APOSTLES"
alias: "Thought: Acts of the Apostles"
type: THOUGHT
parent: topic.THE-BIBLE
tags:
- bible
- luke
- chronology
- geography
- accuracy
neo4j: true
ptopic: "[[topic-THE-BIBLE]]"
level: 5
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ACTS_OF_THE_APOSTLES",
    alias: "Thought: Acts of the Apostles",
    parent: "topic.THE-BIBLE",
    tags: ["bible", "luke", "chronology", "geography", "accuracy"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.ACTS_OF_THE_APOSTLES",
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
WHERE t.name = "thought.ACTS_OF_THE_APOSTLES" AND c.name = "content.ACTS_OF_THE_APOSTLES"
MERGE (t)-[:HAS_CONTENT {name: "edge.ACTS_OF_THE_APOSTLES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-BIBLE" AND child.name = "thought.ACTS_OF_THE_APOSTLES"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-BIBLE->ACTS_OF_THE_APOSTLES"}]->(child);
```
