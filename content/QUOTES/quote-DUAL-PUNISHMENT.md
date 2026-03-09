---
type: QUOTE
name: "quote.DUAL PUNISHMENT"
alias: "Quote: Dual Punishment"
parent: "topic.JUSTICE"
source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'"
en_content: "It is ILLEGAL for GOD The Father to punish both you and Jesus for the same sin(s)!",
 es_title: "Cita: CASTIGO DOBLE",
 es_content: "¡Es ILEGAL que DIOS Padre castigue tanto a usted como a Jesús por los mismos pecados!",
 fr_title: "Citation : DOUBLE PEINE",
 fr_content: "Il est ILLÉGAL que DIEU Le Père vous punisse, vous et Jésus, pour le(s) même(s) péché(s) !",
 hi_title: "उद्धरण: दोहरी सज़ा",
 hi_content: "परमपिता परमेश्वर द्वारा आपको और यीशु दोनों को एक ही पाप के लिए दंडित करना अवैध है!",
 zh_title: "yǐn yòng ： shuāng chóng chéng fá",
 zh_content: "fù shén yīn tóng yàng de zuì ér chéng fá nǐ hé yē sū shì wéi fǎ de ！"
tags: ["sin", "jesus_christ", "propitiation", "substitute", "sacrifice"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.DUAL PUNISHMENT",
    alias: "Quote: Dual Punishment",
    parent: "topic.JUSTICE",
    tags: ["sin", "jesus_christ", "propitiation", "substitute", "sacrifice"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.DUAL PUNISHMENT",
    ctype: "QUOTE",
    en_title: "Dual Punishment",
    en_content: "It is ILLEGAL for GOD The Father to punish both you and Jesus for the same sin(s)!",
 es_title: "Cita: CASTIGO DOBLE",
 es_content: "¡Es ILEGAL que DIOS Padre castigue tanto a usted como a Jesús por los mismos pecados!",
 fr_title: "Citation : DOUBLE PEINE",
 fr_content: "Il est ILLÉGAL que DIEU Le Père vous punisse, vous et Jésus, pour le(s) même(s) péché(s) !",
 hi_title: "उद्धरण: दोहरी सज़ा",
 hi_content: "परमपिता परमेश्वर द्वारा आपको और यीशु दोनों को एक ही पाप के लिए दंडित करना अवैध है!",
 zh_title: "yǐn yòng ： shuāng chóng chéng fá",
 zh_content: "fù shén yīn tóng yàng de zuì ér chéng fá nǐ hé yē sū shì wéi fǎ de ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.DUAL PUNISHMENT"})
MATCH (c:CONTENT {name: "content.DUAL PUNISHMENT"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.DUAL PUNISHMENT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.JUSTICE"})
MATCH (child:QUOTE {name: "quote.DUAL PUNISHMENT"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.JUSTICE->DUAL PUNISHMENT"}]->(child);

```
