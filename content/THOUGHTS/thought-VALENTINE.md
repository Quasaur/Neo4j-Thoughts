---
type: THOUGHT
name: "thought.VALENTINE"
alias: "Thought: Valentine"
parent: "topic.PSYCHOLOGY"
tags: ["valentine", "couples", "romance", "relationships", "love"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.VALENTINE",
    alias: "Thought: Valentine",
    parent: "topic.PSYCHOLOGY",
    tags: ["valentine", "couples", "romance", "relationships", "love"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.VALENTINE",
    ctype: "THOUGHT",
    en_title: "Valentine",
 es_title: "ENAMORADO",
 fr_title: "VALENTIN",
 hi_title: "प्रेमी",
 zh_title: "qíng rén jié",
    en_content: "",
 es_content: "En este San Valentín me pregunto: ¿Cómo puedo evitar dar por sentado a mi esposa?
¿Por qué Dios escogió a esta mujer para mí?\""""",
 fr_content: "En ce jour de la Saint-Valentin, je me demande : « Comment puis-je éviter de prendre ma femme pour acquise ?
Pourquoi Dieu a-t-il choisi cette femme pour moi ? »",
 hi_content: "इस सेंट वैलेंटाइन दिवस पर मैं अपने आप से पूछता हूं \"मैं अपनी पत्नी को हल्के में लेने से कैसे बच सकता हूं?
भगवान ने मेरे लिए इस महिला को क्यों चुना?\""मैं अपनी पत्नी को हल्के में लेने से कैसे बच सकता हूं?
भगवान ने मेरे लिए इस महिला को क्यों चुना?\""मैं अपनी पत्नी को हल्के में लेने से कैसे बच सकता हूं?
भगवान ने मेरे लिए इस महिला को क्यों चुना?\""मैं अपनी पत्नी को हल्के में लेने से कैसे बच सकता हूं?
भगवान ने मेरे लिए इस महिला को क्यों चुना?\"",
 zh_content: "zài zhè ge qíng rén jié ， wǒ wèn zì jǐ ：“ wǒ zěn yàng cái néng bì miǎn bǎ wǒ de qī zǐ shì wèi lǐ suǒ dāng rán ？
 wèi shén me shàng dì yào wèi wǒ tiāo xuǎn zhè ge nǚ rén ？”"मैं अपनी पत्नी को हल्के में लेने से कैसे बच सकता हूं?\nभगवान ने मेरे लिए इस महिला को क्यों चुना?\"""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VALENTINE" AND c.name = "content.VALENTINE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.VALENTINE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.VALENTINE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->VALENTINE"}]->(child);
```