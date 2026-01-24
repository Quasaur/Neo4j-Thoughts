---
name: "thought.GODS SUPERIOR OFFER"
alias: "Thought: Gods Superior Offer"
type: THOUGHT
en_content: "God has FAR MORE to offer me than I have to offer Him."
parent: "topic.THE GODHEAD"
tags:
- god
- offer
- value
- grace
- majesty
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.GODS SUPERIOR OFFER",
    alias: "Thought: Gods Superior Offer",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'offer', 'value', 'grace', 'majesty'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS SUPERIOR OFFER",
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

MATCH (t:THOUGHT {name: "thought.GODS SUPERIOR OFFER"})
MATCH (c:CONTENT {name: "content.GODS SUPERIOR OFFER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS SUPERIOR OFFER" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GODS SUPERIOR OFFER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GODS SUPERIOR OFFER" }]->(child);
```
