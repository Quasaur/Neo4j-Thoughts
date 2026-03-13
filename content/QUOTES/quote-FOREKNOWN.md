---
type: QUOTE
name: "quote.FOREKNOWN"
alias: "Quote: Foreknown"
parent: "topic.DIVINESOVEREIGNTY"
source: "The Narrow Way"
en_content: "To save you from the coming Wrath GOD must KNOW you."
tags: ["foreknowledge", "god", "intimacy", "jesus_christ", "eternity"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FOREKNOWN",
    alias: "Quote: Foreknown",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ["foreknowledge", "god", "intimacy", "jesus_christ", "eternity"],
    source: "The Narrow Way",
    booklink: "https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FOREKNOWN",
    ctype: "QUOTE",
    en_title: "Quote: Foreknown",
    en_content: "To save you from the coming Wrath GOD must KNOW you.",
 es_title: "Cita: Preconocido",
 es_content: "Para salvarte de la ira venidera, DIOS debe CONOCERTE.",
 fr_title: "Citation : Préconnu",
 fr_content: "Pour vous sauver de la colère à venir, DIEU doit vous CONNAÎTRE.",
 hi_title: "उद्धरण: अज्ञात",
 hi_content: "आपको आने वाले क्रोध से बचाने के लिए भगवान को आपको अवश्य जानना चाहिए।",
 zh_title: "yǐn yòng ：yǐ zhī",
 zh_content: "wèi le jiāng nǐ cóng jí jiāng dào lái de fèn nù zhōng zhěng jiù chū lái ， shàng dì bì xū rèn shí nǐ 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.FOREKNOWN"})
MATCH (c:CONTENT {name: "content.FOREKNOWN"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FOREKNOWN"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:QUOTE {name: "quote.FOREKNOWN"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE SOVEREIGNTY->FOREKNOWN"}]->(child);

```
