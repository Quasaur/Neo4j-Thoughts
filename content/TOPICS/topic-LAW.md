---
name: topic.LAW
alias: "Topic: Jurisprudence"
type: TOPIC
parent: topic.MORALITY
tags:
- ordiance
- legislation
- regulation
- statute
- act
neo4j: true
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.LAW",
    alias: "Topic: Jurisprudence",
    parent: "topic.MORALITY",
    tags: ["ordiance", "legislation", "regulation", "statute", "act"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.LAW",
    en_title: "LAW",
    en_content: "A binding custom or practice of a community formally recognized as binding or enforced by a controlling authority.",
    es_title: "LEY",
    es_content: "Una costumbre o práctica vinculante de una comunidad formalmente reconocida como vinculante o impuesta por una autoridad controladora.",
    fr_title: "LOI",
    fr_content: "Une coutume ou une pratique contraignante d'une communauté officiellement reconnue comme contraignante ou appliquée par une autorité de contrôle.",
    hi_title: "कानून",
    hi_content: "किसी समुदाय का बाध्यकारी रिवाज या अभ्यास जिसे औपचारिक रूप से बाध्यकारी माना जाता है या किसी नियंत्रक प्राधिकरण द्वारा लागू किया जाता है।",
    zh_title: "Fǎlǜ",
    zh_content: "Shèqū de bǎngdìng xísú huò shíjiàn, bèi zhèngshì rènkě wéi bǎngdìng huò yóu kòngzhì jīgòu zhíxíng."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.LAW" AND d.name = "desc.LAW"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.LAW"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.MORALITY" AND c.name = "topic.LAW"
MERGE (p)-[:HAS_CHILD {name: "edge.MORALITY->LAW"}]->(c);

```
