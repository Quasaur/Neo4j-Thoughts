---
type: THOUGHT
name: "thought.GODS SUPERIOR OFFER"
alias: "Thought: Gods Superior Offer"
parent: "topic.THE GODHEAD"
en_content: "God has FAR MORE to offer me than I have to offer Him."
tags: ["god", "offer", "value", "grace", "majesty"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Mar-2012)
CREATE (t:THOUGHT {    name: "thought.GODS SUPERIOR OFFER",
    alias: "Thought: Gods Superior Offer",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'offer', 'value', 'grace', 'majesty'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GODS SUPERIOR OFFER",
    ctype: "THOUGHT",
    en_title: "Gods Superior Offer",
    en_content: "God has FAR MORE to offer me than I have to offer Him.",
    es_title: "La Oferta Superior de Dios",
    es_content: "Dios tiene MUCHO MÁS que ofrecerme de lo que yo tengo que ofrecerle a Él.",
    fr_title: "L'Offre Supérieure de Dieu",
    fr_content: "Dieu a BIEN PLUS à m'offrir que ce que j'ai à Lui offrir.",
    hi_title: "परमेश्वर का श्रेष्ठ प्रस्ताव",
    hi_content: "परमेश्वर के पास मुझे देने के लिए उससे कहीं अधिक है जितना मेरे पास उन्हें देने के लिए है।",
    zh_title: "Shàngdì de Chāoyuè Gòngxiàn",
    zh_content: "Shàngdì néng gěi wǒ de bǐ wǒ néng gěi Tā de yào duō de duō."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GODS SUPERIOR OFFER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GODS SUPERIOR OFFER"
RETURN t, parent;
```
