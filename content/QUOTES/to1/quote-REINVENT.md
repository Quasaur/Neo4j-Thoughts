---
type: QUOTE
name: "quote.REINVENT"
alias: "Quote: Reinvent"
parent: "topic.GRACE"
en_content: "It would be completely unnecessary (and a waste of time) for me to try to accomplish what God has already done for me",
 es_title: "Cita: REINVENTARSE",
 es_content: "Sería completamente innecesario (y una pérdida de tiempo) para mí intentar lograr lo que Dios ya ha hecho por mí.",
 fr_title: "Citation : RÉINVENTER",
 fr_content: "Il serait totalement inutile (et une perte de temps) pour moi d'essayer d'accomplir ce que Dieu a déjà fait pour moi.",
 hi_title: "उद्धरण: पुनः आविष्कार",
 hi_content: "मेरे लिए यह पूरी तरह से अनावश्यक (और समय की बर्बादी) होगी कि भगवान ने मेरे लिए जो किया है उसे पूरा करने की कोशिश करें",
 zh_title: "yǐn yòng ： zhòng sù",
 zh_content: "duì wǒ lái shuō ， cháng shì wán chéng shàng dì yǐ jīng wèi wǒ suǒ zuò de shì qíng shì wán quán méi yǒu bì yào de （ ér qiě shì làng fèi shí jiān ）"
tags: ["gift", "grace", "accomplish", "effort", "duplicate"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.REINVENT",
    alias: "Quote: Reinvent",
    parent: "topic.GRACE",
    tags: ["gift", "grace", "accomplish", "effort", "duplicate"],
    source: "'The Traveler's Oasis, Book One'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-One-ebook/dp/B00Y43B2OC)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.REINVENT",
    ctype: "QUOTE",
    en_title: "Reinvent",
    en_content: "It would be completely unnecessary (and a waste of time) for me to try to accomplish what God has already done for me",
 es_title: "Cita: REINVENTARSE",
 es_content: "Sería completamente innecesario (y una pérdida de tiempo) para mí intentar lograr lo que Dios ya ha hecho por mí.",
 fr_title: "Citation : RÉINVENTER",
 fr_content: "Il serait totalement inutile (et une perte de temps) pour moi d'essayer d'accomplir ce que Dieu a déjà fait pour moi.",
 hi_title: "उद्धरण: पुनः आविष्कार",
 hi_content: "मेरे लिए यह पूरी तरह से अनावश्यक (और समय की बर्बादी) होगी कि भगवान ने मेरे लिए जो किया है उसे पूरा करने की कोशिश करें",
 zh_title: "yǐn yòng ： zhòng sù",
 zh_content: "duì wǒ lái shuō ， cháng shì wán chéng shàng dì yǐ jīng wèi wǒ suǒ zuò de shì qíng shì wán quán méi yǒu bì yào de （ ér qiě shì làng fèi shí jiān ）"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.REINVENT"})
MATCH (c:CONTENT {name: "content.REINVENT"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.REINVENT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.REINVENT"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->REINVENT"}]->(child);

```
