---
type: QUOTE
name: "quote.EVIL IDENTIFIED"
alias: "Quote: Evil Identified"
parent: "topic.EVIL"
source: "The Narrow Way"
en_content: "Evil is not identified by works alone but by the absence of GOD in the human heart. The most altruistic soul walking the Earth today without Christ Jesus is just as damned as the most prolific serial killer."
tags: ["evil", "ungodly", "without_god", "humanitarian", "dead_works"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.EVIL IDENTIFIED",
    alias: "Quote: Evil Identified",
    parent: "topic.EVIL",
    tags: ["evil", "ungodly", "without_god", "humanitarian", "dead_works"],
    source: "The Narrow Way",
    booklink: "https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.EVIL IDENTIFIED",
    ctype: "QUOTE",
    en_title: "Quote: Evil Identified",
    en_content: "Evil is not identified by works alone but by the absence of GOD in the human heart. The most altruistic soul walking the Earth today without Christ Jesus is just as damned as the most prolific serial killer.",
 es_title: "Cita: Mal identificado",
 es_content: "El mal no se identifica sólo por las obras sino por la ausencia de DIOS en el corazón humano. El alma más altruista que hoy camina por la Tierra sin Cristo Jesús está tan condenada como el asesino en serie más prolífico.",
 fr_title: "Citation : Le mal identifié",
 fr_content: "Le mal ne s'identifie pas seulement aux œuvres mais à l'absence de DIEU dans le cœur humain. L’âme la plus altruiste qui marche sur Terre aujourd’hui sans Jésus-Christ est tout aussi damnée que le tueur en série le plus prolifique.",
 hi_title: "उद्धरण: बुराई की पहचान हो गई",
 hi_content: "बुराई की पहचान केवल कार्यों से नहीं बल्कि मानव हृदय में ईश्वर की अनुपस्थिति से होती है। मसीह यीशु के बिना आज पृथ्वी पर चलने वाली सबसे परोपकारी आत्मा सबसे विपुल सीरियल किलर के समान ही अभिशप्त है।",
 zh_title: "yǐn yòng ：xié è yǐ shí bié",
 zh_content: "xié è bù jǐn jǐn qǔ jué yú xíng wéi ， hái qǔ jué yú rén xīn zhōng méi yǒu shàng dì 。 jīn tiān ， zài méi yǒu jī dū yē sū de qíng kuàng xià ， zài dì qiú shàng háng zǒu de zuì wú sī de líng hún jiù xiàng zuì duō chǎn de lián huán shā shǒu yī yàng shòu dào zǔ zhòu 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.EVIL IDENTIFIED"})
MATCH (c:CONTENT {name: "content.EVIL IDENTIFIED"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.EVIL IDENTIFIED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:QUOTE {name: "quote.EVIL IDENTIFIED"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->EVIL IDENTIFIED"}]->(child);

```
