---
type: QUOTE
name: "quote.CHRIST_THE_END"
alias: "Quote: Quote: CHRIST THE END"
parent: "topic.LAW"
en_content: "Just as Christ is the 'end' (the COMPLETION of or FULFILLMENT of) the ceremonial law of sacrifices and atonement, He is the 'end' of the Old Covenant (the Ten Commandments) itself.",
 es_title: "Cita: CRISTO FINAL",
 es_content: "Así como Cristo es el 'fin' (la TERMINACIÓN o CUMPLIMIENTO de) la ley ceremonial de los sacrificios y la expiación, Él es el 'fin' del Antiguo Pacto (los Diez Mandamientos) mismo.",
 fr_title: "Citation : CHRIST LA FIN",
 fr_content: "Tout comme Christ est la « fin » (l'achèvement ou l'accomplissement de) la loi cérémonielle des sacrifices et de l'expiation, il est la « fin » de l'Ancienne Alliance (les dix commandements) elle-même.",
 hi_title: "उद्धरण: मसीह अंत है",
 hi_content: "जिस तरह मसीह बलिदान और प्रायश्चित के औपचारिक कानून का 'अंत' (पूर्णता या पूर्णता) है, वह स्वयं पुरानी वाचा (दस आज्ञाओं) का 'अंत' है।",
 zh_title: "yǐn yòng ： jī dū shì zhōng jié",
 zh_content: "zhèng rú jī dū shì xiàn jì hé shú zuì lǐ yí lǜ fǎ de “ zhōng jié ”（ wán chéng huò shí xiàn ） yī yàng ， tā yě shì jiù yuē （ shí jiè ） běn shēn de “ zhōng jié ”。"
tags: ["jesus_christ", "completion", "fulfillment", "ceremoniallaw", "oldcovenant"]
ptopic: "[[topic-LAW]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHRIST_THE_END",
    alias: "Quote: Quote: CHRIST THE END",
    parent: "topic.LAW",
    tags: ["jesus_christ", "completion", "fulfillment", "ceremoniallaw", "oldcovenant"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHRIST_THE_END",
    ctype: "QUOTE",
    en_title: "Quote: CHRIST THE END",
    en_content: "Just as Christ is the 'end' (the COMPLETION of or FULFILLMENT of) the ceremonial law of sacrifices and atonement, He is the 'end' of the Old Covenant (the Ten Commandments) itself.",
 es_title: "Cita: CRISTO FINAL",
 es_content: "Así como Cristo es el 'fin' (la TERMINACIÓN o CUMPLIMIENTO de) la ley ceremonial de los sacrificios y la expiación, Él es el 'fin' del Antiguo Pacto (los Diez Mandamientos) mismo.",
 fr_title: "Citation : CHRIST LA FIN",
 fr_content: "Tout comme Christ est la « fin » (l'achèvement ou l'accomplissement de) la loi cérémonielle des sacrifices et de l'expiation, il est la « fin » de l'Ancienne Alliance (les dix commandements) elle-même.",
 hi_title: "उद्धरण: मसीह अंत है",
 hi_content: "जिस तरह मसीह बलिदान और प्रायश्चित के औपचारिक कानून का 'अंत' (पूर्णता या पूर्णता) है, वह स्वयं पुरानी वाचा (दस आज्ञाओं) का 'अंत' है।",
 zh_title: "yǐn yòng ： jī dū shì zhōng jié",
 zh_content: "zhèng rú jī dū shì xiàn jì hé shú zuì lǐ yí lǜ fǎ de “ zhōng jié ”（ wán chéng huò shí xiàn ） yī yàng ， tā yě shì jiù yuē （ shí jiè ） běn shēn de “ zhōng jié ”。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.CHRIST_THE_END"})
MATCH (c:CONTENT {name: "content.CHRIST_THE_END"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHRIST_THE_END"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.LAW"})
MATCH (child:QUOTE {name: "quote.CHRIST_THE_END"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.LAW->CHRIST_THE_END"}]->(child);

```
