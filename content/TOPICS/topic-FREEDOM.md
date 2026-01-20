---
name: topic.FREEDOM
alias: "Topic: Free to be Moral"
type: TOPIC
parent: topic.LAW
tags:
- free
- choice
- options
- unrestrained
- decisions
neo4j: true
ptopic: "[[topic-LAW]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.FREEDOM",
    alias: "Topic: Free to be Moral",
    parent: "topic.LAW",
    tags: ["free", "choice", "options", "unrestrained", "decisions"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.FREEDOM",
    en_title: "FREEDOM",
    en_content: "The absence of necessity, coercion, or constraint in choice or action with the framework of morality and law.",
    es_title: "LIBERTAD",
    es_content: "La ausencia de necesidad, coacción o restricción en la elección o acción dentro del marco de la moralidad y la ley.",
    fr_title: "LIBERTÉ",
    fr_content: "L'absence de nécessité, de coercition ou de contrainte dans le choix ou l'action dans le cadre de la moralité et de la loi.",
    hi_title: "आज़ादी",
    hi_content: "नैतिकता और कानून के ढांचे के भीतर पसंद या कार्रवाई में आवश्यकता, जबरदस्ती या बाधा की अनुपस्थिति।",
    zh_title: "Zìyóu",
    zh_content: "Zài dàodé hé fǎlǜ de kuàngjià nèi, xuǎnzé huò xíngdòng zhōng quēfá bìyào, qiǎngpò huò yuēshù."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.FREEDOM"})
MATCH (d:DESCRIPTION {name: "desc.FREEDOM"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.FREEDOM"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.LAW"
MATCH (c:TOPIC)
WHERE c.name = "topic.FREEDOM"
MERGE (p)-[:HAS_CHILD {name: "edge.LAW->FREEDOM"}]->(c);

```
