---
type: QUOTE
name: "quote.NOT WITHOUT HUMILITY"
alias: "Quote: Not Without Humility"
parent: "topic.ATTITUDE"
source: "The Narrow Way"
en_content: "What i wish to remind us all is that THERE'S NO SALVATION WITHOUT REPENTANCE AND THERE'S NO REPENTANCE WITHOUT HUMILITY."
tags: ["repentance", "gift", "humble", "essential", "heart"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NOT WITHOUT HUMILITY",
    alias: "Quote: Not Without Humility",
    parent: "topic.ATTITUDE",
    tags: ["repentance", "gift", "humble", "essential", "heart"],
    source: "The Narrow Way",
    booklink: "https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NOT WITHOUT HUMILITY",
    ctype: "QUOTE",
    en_title: "Quote: Not Without Humility",
    en_content: "What i wish to remind us all is that THERE'S NO SALVATION WITHOUT REPENTANCE AND THERE'S NO REPENTANCE WITHOUT HUMILITY.",
 es_title: "Cita: No sin humildad",
 es_content: "Lo que deseo recordarnos a todos es que NO HAY SALVACIÓN SIN ARREPENTIMIENTO Y NO HAY ARREPENTIMIENTO SIN HUMILDAD.",
 fr_title: "Citation : Pas sans humilité",
 fr_content: "Ce que je souhaite nous rappeler à tous, c'est qu'IL N'Y A PAS DE SALUT SANS REPENTANCE ET IL N'Y A PAS DE REPENTANCE SANS HUMILITÉ.",
 hi_title: "उद्धरण: विनम्रता के बिना नहीं",
 hi_content: "मैं हम सभी को यह याद दिलाना चाहता हूं कि पश्चाताप के बिना कोई मुक्ति नहीं है और विनम्रता के बिना कोई पश्चाताप नहीं है।",
 zh_title: "yǐn yòng ：bìng fēi méi yǒu qiān xū",
 zh_content: "wǒ xiǎng tí xǐng wǒ men dà jiā de shì ， méi yǒu huǐ gǎi jiù méi yǒu jiù shú ， méi yǒu qiān bēi jiù méi yǒu huǐ gǎi 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.NOT WITHOUT HUMILITY"})
MATCH (c:CONTENT {name: "content.NOT WITHOUT HUMILITY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NOT WITHOUT HUMILITY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MATCH (child:QUOTE {name: "quote.NOT WITHOUT HUMILITY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.ATTITUDE->NOT WITHOUT HUMILITY"}]->(child);

```
