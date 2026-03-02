---
type: QUOTE
name: "quote.THE_CHRISTIAN_SYSTEM"
alias: "Quote: Quote: THE CHRISTIAN SYSTEM"
parent: "topic.POLITICAL-SCIENCE"
en_content: "So what is Christianity? Jesus Christ, and all Truth concerning Him IS Christianity. So by saying that Jesus Christ is a political / economic figurehead as well as a spiritual figurehead I am implying that Christianity is a political / economic system as well.",
 es_title: "Cita: EL SISTEMA CRISTIANO",
 es_content: "Entonces ¿qué es el cristianismo? Jesucristo, y toda verdad acerca de Él ES cristianismo. Entonces, al decir que Jesucristo es una figura política/económica así como una figura espiritual, estoy implicando que el cristianismo es también un sistema político/económico.",
 fr_title: "Citation : LE SYSTÈME CHRÉTIEN",
 fr_content: "Alors, qu’est-ce que le christianisme ? Jésus-Christ et toute la vérité le concernant EST le christianisme. Ainsi, en disant que Jésus-Christ est une figure de proue politique/économique ainsi qu’une figure de proue spirituelle, j’implique que le christianisme est également un système politique/économique.",
 hi_title: "उद्धरण: ईसाई प्रणाली",
 hi_content: "तो ईसाई धर्म क्या है? यीशु मसीह, और उससे संबंधित सभी सत्य ईसाई धर्म हैं। इसलिए यह कहकर कि ईसा मसीह एक राजनीतिक/आर्थिक व्यक्तित्व के साथ-साथ एक आध्यात्मिक व्यक्तित्व भी हैं, मेरा तात्पर्य यह है कि ईसाई धर्म एक राजनीतिक/आर्थिक प्रणाली भी है।",
 zh_title: "yǐn yòng ： jī dū jiào tǐ xì",
 zh_content: "nà me shén me shì jī dū jiào ne ？ yē sū jī dū yǐ jí guān yú tā de suǒ yǒu zhēn lǐ dōu shì jī dū jiào 。 yīn cǐ ， tōng guò shuō yē sū jī dū shì yí gè zhèng zhì / jīng jì kuǐ lěi yǐ jí jīng shén kuǐ lěi ， wǒ shì zài àn shì jī dū jiào yě shì yí gè zhèng zhì / jīng jì tǐ xì 。"
tags: ["christianity", "jesus_christ", "truth", "political", "economic"]
ptopic: "[[topic-POLITICAL-SCIENCE]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_CHRISTIAN_SYSTEM",
    alias: "Quote: Quote: THE CHRISTIAN SYSTEM",
    parent: "topic.POLITICAL-SCIENCE",
    tags: ["christianity", "jesus_christ", "truth", "political", "economic"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_CHRISTIAN_SYSTEM",
    ctype: "QUOTE",
    en_title: "Quote: THE CHRISTIAN SYSTEM",
    en_content: "So what is Christianity? Jesus Christ, and all Truth concerning Him IS Christianity. So by saying that Jesus Christ is a political / economic figurehead as well as a spiritual figurehead I am implying that Christianity is a political / economic system as well.",
 es_title: "Cita: EL SISTEMA CRISTIANO",
 es_content: "Entonces ¿qué es el cristianismo? Jesucristo, y toda verdad acerca de Él ES cristianismo. Entonces, al decir que Jesucristo es una figura política/económica así como una figura espiritual, estoy implicando que el cristianismo es también un sistema político/económico.",
 fr_title: "Citation : LE SYSTÈME CHRÉTIEN",
 fr_content: "Alors, qu’est-ce que le christianisme ? Jésus-Christ et toute la vérité le concernant EST le christianisme. Ainsi, en disant que Jésus-Christ est une figure de proue politique/économique ainsi qu’une figure de proue spirituelle, j’implique que le christianisme est également un système politique/économique.",
 hi_title: "उद्धरण: ईसाई प्रणाली",
 hi_content: "तो ईसाई धर्म क्या है? यीशु मसीह, और उससे संबंधित सभी सत्य ईसाई धर्म हैं। इसलिए यह कहकर कि ईसा मसीह एक राजनीतिक/आर्थिक व्यक्तित्व के साथ-साथ एक आध्यात्मिक व्यक्तित्व भी हैं, मेरा तात्पर्य यह है कि ईसाई धर्म एक राजनीतिक/आर्थिक प्रणाली भी है।",
 zh_title: "yǐn yòng ： jī dū jiào tǐ xì",
 zh_content: "nà me shén me shì jī dū jiào ne ？ yē sū jī dū yǐ jí guān yú tā de suǒ yǒu zhēn lǐ dōu shì jī dū jiào 。 yīn cǐ ， tōng guò shuō yē sū jī dū shì yí gè zhèng zhì / jīng jì kuǐ lěi yǐ jí jīng shén kuǐ lěi ， wǒ shì zài àn shì jī dū jiào yě shì yí gè zhèng zhì / jīng jì tǐ xì 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_CHRISTIAN_SYSTEM"})
MATCH (c:CONTENT {name: "content.THE_CHRISTIAN_SYSTEM"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_CHRISTIAN_SYSTEM"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.POLITICAL-SCIENCE"})
MATCH (child:QUOTE {name: "quote.THE_CHRISTIAN_SYSTEM"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.POLITICAL-SCIENCE->THE_CHRISTIAN_SYSTEM"}]->(child);

```
