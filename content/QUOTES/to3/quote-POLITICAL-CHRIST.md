---
type: QUOTE
name: "quote.POLITICAL_CHRIST"
alias: "Quote: Quote: POLITICAL CHRIST"
parent: "topic.POLITICAL-SCIENCE"
en_content: "I state that not only is Jesus' Authority spiritual, but political and economic as well.",
 es_title: "Cita: CRISTO POLÍTICO",
 es_content: "Afirmo que la Autoridad de Jesús no sólo es espiritual, sino también política y económica.",
 fr_title: "Citation : CHRIST POLITIQUE",
 fr_content: "Je déclare que l'autorité de Jésus est non seulement spirituelle, mais aussi politique et économique.",
 hi_title: "उद्धरण: राजनीतिक मसीह",
 hi_content: "मैं कहता हूं कि यीशु का अधिकार न केवल आध्यात्मिक है, बल्कि राजनीतिक और आर्थिक भी है।",
 zh_title: "yǐn yòng ： zhèng zhì jī dū",
 zh_content: "wǒ xiǎng shuō ， yē sū de quán wēi bù jǐn shì jīng shén shàng de ， ér qiě shì zhèng zhì shàng hé jīng jì shàng de 。"
tags: ["jesus_christ", "authority", "political", "spiritual", "economical"]
ptopic: "[[topic-POLITICAL-SCIENCE]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.POLITICAL_CHRIST",
    alias: "Quote: Quote: POLITICAL CHRIST",
    parent: "topic.POLITICAL-SCIENCE",
    tags: ["jesus_christ", "authority", "political", "spiritual", "economical"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.POLITICAL_CHRIST",
    ctype: "QUOTE",
    en_title: "Quote: POLITICAL CHRIST",
    en_content: "I state that not only is Jesus' Authority spiritual, but political and economic as well.",
 es_title: "Cita: CRISTO POLÍTICO",
 es_content: "Afirmo que la Autoridad de Jesús no sólo es espiritual, sino también política y económica.",
 fr_title: "Citation : CHRIST POLITIQUE",
 fr_content: "Je déclare que l'autorité de Jésus est non seulement spirituelle, mais aussi politique et économique.",
 hi_title: "उद्धरण: राजनीतिक मसीह",
 hi_content: "मैं कहता हूं कि यीशु का अधिकार न केवल आध्यात्मिक है, बल्कि राजनीतिक और आर्थिक भी है।",
 zh_title: "yǐn yòng ： zhèng zhì jī dū",
 zh_content: "wǒ xiǎng shuō ， yē sū de quán wēi bù jǐn shì jīng shén shàng de ， ér qiě shì zhèng zhì shàng hé jīng jì shàng de 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.POLITICAL_CHRIST"})
MATCH (c:CONTENT {name: "content.POLITICAL_CHRIST"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.POLITICAL_CHRIST"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.POLITICAL-SCIENCE"})
MATCH (child:QUOTE {name: "quote.POLITICAL_CHRIST"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.POLITICAL-SCIENCE->POLITICAL_CHRIST"}]->(child);

```
