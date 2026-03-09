---
type: QUOTE
name: "quote.CESSATION OF LABOR"
alias: "Quote: Cessation of Labor"
parent: "topic.GRACE"
source: "'The Traveler's Oasis, Book Two'"
en_content: "Upon entering by faith into Christ Jesus, the soul CEASES FROM ITS OWN LABOR, just as God did fro His. There is Peace; endless, refreshing, soothing, loving, empowering PEACE.",
 es_title: "Cita: CESE DEL TRABAJO",
 es_content: "Al entrar por la fe en Cristo Jesús, el alma CESA DE SU PROPIO TRABAJO, así como Dios lo hizo con el suyo. Hay Paz; PAZ infinita, refrescante, calmante, amorosa y empoderadora.",
 fr_title: "Citation : CESSATION DU TRAVAIL",
 fr_content: "En entrant par la foi en Jésus-Christ, l'âme CESSE DE SON PROPRE TRAVAIL, tout comme Dieu l'a fait pour le Sien. Il y a la Paix ; une PAIX sans fin, rafraîchissante, apaisante, aimante et stimulante.",
 hi_title: "उद्धरण: श्रम की समाप्ति",
 hi_content: "मसीह यीशु में विश्वास के द्वारा प्रवेश करने पर, आत्मा अपने श्रम से मुक्त हो जाती है, ठीक वैसे ही जैसे भगवान ने अपने काम से किया था। वहाँ शांति है; अंतहीन, ताज़ा, सुखदायक, प्रेमपूर्ण, सशक्त शांति।",
 zh_title: "yǐn yòng ： tíng zhǐ láo dòng",
 zh_content: "yí dàn píng zhe xìn xīn jìn rù jī dū yē sū ， líng hún jiù tíng zhǐ le zì jǐ de láo dòng ， jiù xiàng shén tíng zhǐ le tā de láo dòng yī yàng 。 yǒu hé píng ； wú jìn de 、 qīng shuǎng de 、 shū huǎn de 、 chōng mǎn ài de 、 fù yǔ hé píng de lì liàng 。"
tags: ["inchrist", "byfaith", "soul", "rest", "peace"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CESSATION OF LABOR",
    alias: "Quote: Cessation of Labor",
    parent: "topic.GRACE",
    tags: ["inchrist", "byfaith", "soul", "rest", "peace"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CESSATION OF LABOR",
    ctype: "QUOTE",
    en_title: "Cessation of Labor",
    en_content: "Upon entering by faith into Christ Jesus, the soul CEASES FROM ITS OWN LABOR, just as God did fro His. There is Peace; endless, refreshing, soothing, loving, empowering PEACE.",
 es_title: "Cita: CESE DEL TRABAJO",
 es_content: "Al entrar por la fe en Cristo Jesús, el alma CESA DE SU PROPIO TRABAJO, así como Dios lo hizo con el suyo. Hay Paz; PAZ infinita, refrescante, calmante, amorosa y empoderadora.",
 fr_title: "Citation : CESSATION DU TRAVAIL",
 fr_content: "En entrant par la foi en Jésus-Christ, l'âme CESSE DE SON PROPRE TRAVAIL, tout comme Dieu l'a fait pour le Sien. Il y a la Paix ; une PAIX sans fin, rafraîchissante, apaisante, aimante et stimulante.",
 hi_title: "उद्धरण: श्रम की समाप्ति",
 hi_content: "मसीह यीशु में विश्वास के द्वारा प्रवेश करने पर, आत्मा अपने श्रम से मुक्त हो जाती है, ठीक वैसे ही जैसे भगवान ने अपने काम से किया था। वहाँ शांति है; अंतहीन, ताज़ा, सुखदायक, प्रेमपूर्ण, सशक्त शांति।",
 zh_title: "yǐn yòng ： tíng zhǐ láo dòng",
 zh_content: "yí dàn píng zhe xìn xīn jìn rù jī dū yē sū ， líng hún jiù tíng zhǐ le zì jǐ de láo dòng ， jiù xiàng shén tíng zhǐ le tā de láo dòng yī yàng 。 yǒu hé píng ； wú jìn de 、 qīng shuǎng de 、 shū huǎn de 、 chōng mǎn ài de 、 fù yǔ hé píng de lì liàng 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.CESSATION OF LABOR"})
MATCH (c:CONTENT {name: "content.CESSATION OF LABOR"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CESSATION OF LABOR"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.CESSATION OF LABOR"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->CESSATION OF LABOR"}]->(child);

```
