---
type: QUOTE
name: "quote.PRAYER"
alias: "Quote: Prayer"
parent: "topic.WORSHIP"
en_content: "To your soul GOD BECOMES MORE REAL AND YOU (and your circumstances and situations) BECOME LESS REAL.",
 es_title: "Cita: ORACIÓN",
 es_content: "Para tu alma DIOS SE VUELVE MÁS REAL Y TÚ (y tus circunstancias y situaciones) SE VUELVE MENOS REAL.",
 fr_title: "Citation : PRIÈRE",
 fr_content: "Pour votre âme, DIEU DEVIENT PLUS RÉEL ET VOUS (ainsi que vos circonstances et situations) DEVENEZ MOINS RÉEL.",
 hi_title: "उद्धरण: प्रार्थना",
 hi_content: "आपकी आत्मा के लिए ईश्वर अधिक वास्तविक हो जाता है और आप (और आपकी परिस्थितियाँ और परिस्थितियाँ) कम वास्तविक हो जाते हैं।",
 zh_title: "yǐn yòng ： qí dǎo",
 zh_content: "duì yú nǐ de líng hún lái shuō ， shàng dì biàn dé gèng jiā zhēn shí ， ér nǐ （ yǐ jí nǐ de huán jìng hé chǔ jìng ） biàn dé bù nà me zhēn shí 。"
tags: ["pray", "real", "god", "self", "circumstance"]
ptopic: "[[topic-WORSHIP]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.PRAYER",
    alias: "Quote: Prayer",
    parent: "topic.WORSHIP",
    tags: ["pray", "real", "god", "self", "circumstance"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PRAYER",
    ctype: "QUOTE",
    en_title: "Prayer",
    en_content: "To your soul GOD BECOMES MORE REAL AND YOU (and your circumstances and situations) BECOME LESS REAL.",
 es_title: "Cita: ORACIÓN",
 es_content: "Para tu alma DIOS SE VUELVE MÁS REAL Y TÚ (y tus circunstancias y situaciones) SE VUELVE MENOS REAL.",
 fr_title: "Citation : PRIÈRE",
 fr_content: "Pour votre âme, DIEU DEVIENT PLUS RÉEL ET VOUS (ainsi que vos circonstances et situations) DEVENEZ MOINS RÉEL.",
 hi_title: "उद्धरण: प्रार्थना",
 hi_content: "आपकी आत्मा के लिए ईश्वर अधिक वास्तविक हो जाता है और आप (और आपकी परिस्थितियाँ और परिस्थितियाँ) कम वास्तविक हो जाते हैं।",
 zh_title: "yǐn yòng ： qí dǎo",
 zh_content: "duì yú nǐ de líng hún lái shuō ， shàng dì biàn dé gèng jiā zhēn shí ， ér nǐ （ yǐ jí nǐ de huán jìng hé chǔ jìng ） biàn dé bù nà me zhēn shí 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.PRAYER"})
MATCH (c:CONTENT {name: "content.PRAYER"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.PRAYER"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.WORSHIP"})
MATCH (child:QUOTE {name: "quote.PRAYER"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.WORSHIP->PRAYER"}]->(child);

```
