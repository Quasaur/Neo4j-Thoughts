---
type: TOPIC
name: "topic.POLITICAL SCIENCE"
alias: "Topic: Politics"
parent: "topic.SOCIAL SCIENCES"
en_content: "The systematic study of power, governance, public institutions, political behavior, and the processes through which societies make collective decisions. It analyzes how authority is organized, exercised, contested, and justified within and between communities."
tags: ["power", "governance", "institutions", "policy", "behavior"]
ptopic: "[[topic-SOCIAL-SCIENCES]]"
level: 5
neo4j: true
verified: true
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.POLITICAL SCIENCE",
    alias: "Topic: Politics",
    parent: "topic.SOCIAL SCIENCES",
    tags: ["power", "governance", "institutions", "policy", "behavior"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.POLITICAL SCIENCE",
    en_title: "Political Science",
    en_content: "The systematic study of power, governance, public institutions, political behavior, and the processes through which societies make collective decisions. It analyzes how authority is organized, exercised, contested, and justified within and between communities.",
    es_title: "Tema: Política",
    es_content: "El estudio sistemático del poder, la gobernanza, las instituciones públicas, el comportamiento político y los procesos a través de los cuales las sociedades toman decisiones colectivas. Analiza cómo se organiza, ejerce, disputa y justifica la autoridad dentro y entre las comunidades.",
    fr_title: "Sujet : Politique",
    fr_content: "L'étude systématique du pouvoir, de la gouvernance, des institutions publiques, du comportement politique et des processus par lesquels les sociétés prennent des décisions collectives. Elle analyse la manière dont l'autorité est organisée, exercée, contestée et justifiée au sein des communautés et entre elles.",
    hi_title: "विषय: राजनीति",
    hi_content: "शक्ति, शासन, सार्वजनिक संस्थानों, राजनीतिक व्यवहार और उन प्रक्रियाओं का व्यवस्थित अध्ययन जिनके माध्यम से समाज सामूहिक निर्णय लेते हैं। यह विश्लेषण करता है कि समुदायों के भीतर और उनके बीच सत्ता को कैसे व्यवस्थित किया जाता है, उसका प्रयोग कैसे किया जाता है, उसे कैसे चुनौती दी जाती है और उसे कैसे सही ठहराया जाता है।",
    zh_title: "Zhǔtí: Zhèngzhì",
    zh_content: "duì quán lì 、 zhì lǐ 、 gōng gòng jī gòu 、 zhèng zhì xíng wéi yǐ jí shè huì jí tǐ jué cè guò chéng de xì tǒng yán jiū . tā fēn xī le shè qū nèi bù hé shè qū zhī jiān quán lì rú hé zǔ zhī 、 xíng shǐ 、 jìng zhēng hé hé lǐ huà ."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.POLITICAL SCIENCE"})
MATCH (d:DESCRIPTION {name: "desc.POLITICAL SCIENCE"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.POLITICAL SCIENCE"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.SOCIAL SCIENCES"
MATCH (c:TOPIC)
WHERE c.name = "topic.POLITICAL SCIENCE"
MERGE (p)-[:HAS_CHILD {name: "edge.SOCIAL SCIENCE->POLITICAL SCIENCE"}]->(c);

```
