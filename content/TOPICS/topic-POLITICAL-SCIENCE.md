---
name: "topic.POLITICAL SCIENCE"
alias: "Topic: Politics"
type: TOPIC
parent: "topic.SOCIAL SCIENCES"
en_content: "The systematic study of power, governance, public institutions, political behavior, and the processes through which societies make collective decisions. It analyzes how authority is organized, exercised, contested, and justified within and between communities."
tags:
- power
- governance
- institutions
- policy
- behavior
neo4j: true
ptopic: "[[topic-SOCIAL-SCIENCES]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.POLITICAL-SCIENCE",
    alias: "Topic Politics",
    parent: "topic.SOCIAL SCIENCES",
    tags: ["power", "governance", "institutions", "policy", "behavior"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.POLITICAL-SCIENCE",
    en_title: "Political Science",
    en_content: "The systematic study of power, governance, public institutions, political behavior, and the processes through which societies make collective decisions. It analyzes how authority is organized, exercised, contested, and justified within and between communities.",
    es_title: "Ciencia Política",
    es_content: "El estudio sistemático del poder, la gobernanza, las instituciones públicas, el comportamiento político y los procesos a través de los cuales las sociedades toman decisiones colectivas. Analiza cómo se organiza, ejerce, disputa y justifica la autoridad dentro y entre las comunidades.",
    fr_title: "Science politique",
    fr_content: "L'étude systématique du pouvoir, de la gouvernance, des institutions publiques, du comportement politique et des processus par lesquels les sociétés prennent des décisions collectives. Elle analyse la manière dont l'autorité est organisée, exercée, contestée et justifiée au sein des communautés et entre elles.",
    hi_title: "राजनीति विज्ञान",
    hi_content: "शक्ति, शासन, सार्वजनिक संस्थानों, राजनीतिक व्यवहार और उन प्रक्रियाओं का व्यवस्थित अध्ययन जिनके माध्यम से समाज सामूहिक निर्णय लेते हैं। यह विश्लेषण करता है कि समुदायों के भीतर और उनके बीच सत्ता को कैसे व्यवस्थित किया जाता है, उसका प्रयोग कैसे किया जाता है, उसे कैसे चुनौती दी जाती है और उसे कैसे सही ठहराया जाता है।",
    zh_title: "Zhèngzhì xué",
    zh_content: "政治学
政治学是对权力、治理、公共机构、政治行为以及社会做出集体决策的过程进行的系统研究。它分析权力如何在社会内部和不同社会之间被组织、行使、争夺和合法化。"
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.POLITICAL-SCIENCE"})
MATCH (d:DESCRIPTION {name: "desc.POLITICAL-SCIENCE"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.POLITICAL-SCIENCE"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.SOCIAL SCIENCES"
MATCH (c:TOPIC)
WHERE c.name = "topic.POLITICAL-SCIENCE"
MERGE (p)-[:HAS_CHILD {name: "edge.SOCIAL SCIENCE->POLITICAL-SCIENCE"}]->(c);

```
