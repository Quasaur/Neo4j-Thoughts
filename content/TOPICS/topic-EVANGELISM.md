---
name: topic.EVANGELISM
alias: "Topic: Fishers of Men"
type: TOPIC
parent: topic.THE-GOSPEL
tags:
- faithsharing
- persuasion
- discipling
- goodnews
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 3
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.EVANGELISM",
    alias: "Topic: Fishers of Men",
    parent: "topic.THE-GOSPEL",
    tags: ["faithsharing", "persuasion", "discipling", "goodnews"],
    level: 3
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.EVANGELISM",
    en_title: "EVANGELISM",
    en_content: "The winning or revival of personal commitments to Christ; making disciples of all nations; militant or crusading zeal.",
    es_title: "EVANGELISMO",
    es_content: "La obtención o reavivamiento de compromisos personales con Cristo; hacer discípulos de todas las naciones; celo militante o de cruzada.",
    fr_title: "ÉVANGÉLISME",
    fr_content: "La conquête ou le renouveau d’engagements personnels envers le Christ ; faire des disciples de toutes les nations ; zèle militant ou de croisade.",
    hi_title: "इंजीलवाद",
    hi_content: "मसीह के प्रति व्यक्तिगत प्रतिबद्धताओं की जीत या पुनरुद्धार; सभी देशों के लोगों को शिष्य बनाना; उग्रवादी या धर्मयुद्ध उत्साह।",
    zh_title: "Fúyīn chuánjiào",
    zh_content: "Yíngdé huò fùxīng duì jīdū de gèrén chéngnuò; shǐ wàn mín chéngwéi méntú; hàozhàn huò shízìjūn de rèqíng."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.EVANGELISM"})
MATCH (d:DESCRIPTION {name: "desc.EVANGELISM"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.EVANGELISM"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.THE-GOSPEL"
MATCH (c:TOPIC)
WHERE c.name = "topic.EVANGELISM"
MERGE (p)-[:HAS_CHILD {name: "edge.THE-GOSPEL->EVANGELISM"}]->(c);

```
