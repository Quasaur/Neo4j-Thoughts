---
type: QUOTE
name: "quote.THE CHRISTIAN SYSTEM"
alias: "Quote: The Christian System"
parent: "topic.POLITICAL SCIENCE"
source: "The Traveler's Oasis, Book Three"
en_content: "So what is Christianity? Jesus Christ, and all Truth concerning Him IS Christianity. So by saying that Jesus Christ is a political / economic figurehead as well as a spiritual figurehead I am implying that Christianity is a political / economic system as well."
tags: ["christianity", "jesus_christ", "truth", "political", "economic"]
ptopic: "[[topic-POLITICAL-SCIENCE]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE CHRISTIAN SYSTEM",
    alias: "Quote: The Christian System",
    parent: "topic.POLITICAL SCIENCE",
    tags: ["christianity", "jesus_christ", "truth", "political", "economic"],
    source: "The Traveler's Oasis, Book Three",
    booklink: "https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE CHRISTIAN SYSTEM",
    ctype: "QUOTE",
    en_title: "Quote: The Christian System",
    en_content: "So what is Christianity? Jesus Christ, and all Truth concerning Him IS Christianity. So by saying that Jesus Christ is a political / economic figurehead as well as a spiritual figurehead I am implying that Christianity is a political / economic system as well.",
 es_title: "Cita: El sistema cristiano",
 es_content: "Entonces ¿qué es el cristianismo? Jesucristo, y toda verdad acerca de Él ES cristianismo. Entonces, al decir que Jesucristo es una figura política/económica así como una figura espiritual, estoy implicando que el cristianismo es también un sistema político/económico.",
 fr_title: "Citation : Le système chrétien",
 fr_content: "Alors, qu’est-ce que le christianisme ? Jésus-Christ et toute la vérité le concernant EST le christianisme. Ainsi, en disant que Jésus-Christ est une figure de proue politique/économique ainsi qu’une figure de proue spirituelle, j’implique que le christianisme est également un système politique/économique.",
 hi_title: "उद्धरण: ईसाई प्रणाली",
 hi_content: "तो ईसाई धर्म क्या है? यीशु मसीह, और उससे संबंधित सभी सत्य ईसाई धर्म हैं। इसलिए यह कहकर कि ईसा मसीह एक राजनीतिक/आर्थिक व्यक्तित्व के साथ-साथ एक आध्यात्मिक व्यक्तित्व भी हैं, मेरा तात्पर्य यह है कि ईसाई धर्म एक राजनीतिक/आर्थिक प्रणाली भी है।",
 zh_title: "yǐn yòng ：jī dū jiào tǐ xì",
 zh_content: "nà me shén me shì jī dū jiào ne ？ yē sū jī dū yǐ jí guān yú tā de suǒ yǒu zhēn lǐ dōu shì jī dū jiào 。 yīn cǐ ， tōng guò shuō yē sū jī dū shì yí gè zhèng zhì / jīng jì kuǐ lěi yǐ jí jīng shén kuǐ lěi ， wǒ shì zài àn shì jī dū jiào yě shì yí gè zhèng zhì / jīng jì tǐ xì 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE CHRISTIAN SYSTEM"})
MATCH (c:CONTENT {name: "content.THE CHRISTIAN SYSTEM"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE CHRISTIAN SYSTEM"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.POLITICAL SCIENCE"})
MATCH (child:QUOTE {name: "quote.THE CHRISTIAN SYSTEM"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.POLITICAL SCIENCE->THE CHRISTIAN SYSTEM"}]->(child);

```
