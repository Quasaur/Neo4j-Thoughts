---
name: topic.ENTITLEMENT
alias: "Topic: Arrogance"
type: TOPIC
parent: topic.ATTITUDE
tags:
- entitled
- privilege
- right
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.ENTITLEMENT",
    alias: "Topic: Arrogance",
    parent: "topic.ATTITUDE",
    tags: ["entitled", "privilege", "right"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.ENTITLEMENT",
    en_title: "ENTITLEMENT",
    en_content: "Law, contract or belief that one is deserving of or entitled to certain rights, benefits and privileges.",
    es_title: "DERECHO",
    es_content: "Ley, contrato o creencia de que uno merece o tiene derecho a ciertos derechos, beneficios y privilegios.",
    fr_title: "DROIT",
    fr_content: "Loi, contrat ou croyance selon laquelle on mérite ou a droit à certains droits, avantages et privilèges.",
    hi_title: "अधिकार",
    hi_content: "कानून, अनुबंध या विश्वास है कि कोई कुछ अधिकारों, लाभों और विशेषाधिकारों का हकदार है।",
    zh_title: "Quánlì",
    zh_content: "Fǎlǜ, hétóng huò xìnniàn, jí yīgè rén yǒu zīgé huò yǒu quán xiǎngyǒu mǒu xiē quánlì, fúlì hé tèquán."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.ENTITLEMENT"})
MATCH (d:DESCRIPTION {name: "desc.ENTITLEMENT"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.ENTITLEMENT"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.ATTITUDE"
MATCH (c:TOPIC)
WHERE c.name = "topic.ENTITLEMENT"
MERGE (p)-[:HAS_CHILD {name: "edge.ATTITUDE->ENTITLEMENT"}]->(c);

```
