---
type: QUOTE
name: "quote.HUMILITY"
alias: "Quote: Humility"
parent: "topic.HUMILITY"
en_content: "A realistic view of ourselves in the Light of the Holy Scriptures and in the Presence of Almighty GOD is what we call HUMILITY; and without this humility Salvation is simply impossible.",
 es_title: "Cita: HUMILDAD",
 es_content: "Una visión realista de nosotros mismos a la Luz de las Sagradas Escrituras y en la Presencia de DIOS Todopoderoso es lo que llamamos HUMILDAD; y sin esta humildad la Salvación es simplemente imposible.",
 fr_title: "Citation : HUMILITÉ",
 fr_content: "Une vision réaliste de nous-mêmes à la Lumière des Saintes Écritures et en Présence de DIEU Tout-Puissant est ce que nous appelons l’HUMILITÉ ; et sans cette humilité, le salut est tout simplement impossible.",
 hi_title: "उद्धरण: विनम्रता",
 hi_content: "पवित्र धर्मग्रंथों के प्रकाश में और सर्वशक्तिमान ईश्वर की उपस्थिति में अपने बारे में एक यथार्थवादी दृष्टिकोण को हम विनम्रता कहते हैं; और इस विनम्रता के बिना मुक्ति बिल्कुल असंभव है।",
 zh_title: "yǐn yòng ： qiān xū",
 zh_content: "zài shèng jīng de guāng zhào xià hé zài quán néng shàng dì miàn qián duì zì jǐ de xiàn shí kàn fǎ jiù shì wǒ men suǒ shuō de qiān bēi 。 méi yǒu zhè zhǒng qiān bēi ， jiù shú gēn běn bù kě néng 。"
tags: ["self_image", "bible", "god", "reservedness", "salvation"]
ptopic: "[[topic-HUMILITY]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.HUMILITY",
    alias: "Quote: Humility",
    parent: "topic.HUMILITY",
    tags: ["self_image", "bible", "god", "reservedness", "salvation"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.HUMILITY",
    ctype: "QUOTE",
    en_title: "Humility",
    en_content: "A realistic view of ourselves in the Light of the Holy Scriptures and in the Presence of Almighty GOD is what we call HUMILITY; and without this humility Salvation is simply impossible.",
 es_title: "Cita: HUMILDAD",
 es_content: "Una visión realista de nosotros mismos a la Luz de las Sagradas Escrituras y en la Presencia de DIOS Todopoderoso es lo que llamamos HUMILDAD; y sin esta humildad la Salvación es simplemente imposible.",
 fr_title: "Citation : HUMILITÉ",
 fr_content: "Une vision réaliste de nous-mêmes à la Lumière des Saintes Écritures et en Présence de DIEU Tout-Puissant est ce que nous appelons l’HUMILITÉ ; et sans cette humilité, le salut est tout simplement impossible.",
 hi_title: "उद्धरण: विनम्रता",
 hi_content: "पवित्र धर्मग्रंथों के प्रकाश में और सर्वशक्तिमान ईश्वर की उपस्थिति में अपने बारे में एक यथार्थवादी दृष्टिकोण को हम विनम्रता कहते हैं; और इस विनम्रता के बिना मुक्ति बिल्कुल असंभव है।",
 zh_title: "yǐn yòng ： qiān xū",
 zh_content: "zài shèng jīng de guāng zhào xià hé zài quán néng shàng dì miàn qián duì zì jǐ de xiàn shí kàn fǎ jiù shì wǒ men suǒ shuō de qiān bēi 。 méi yǒu zhè zhǒng qiān bēi ， jiù shú gēn běn bù kě néng 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.HUMILITY"})
MATCH (c:CONTENT {name: "content.HUMILITY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.HUMILITY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.HUMILITY"})
MATCH (child:QUOTE {name: "quote.HUMILITY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.HUMILITY->HUMILITY"}]->(child);

```
