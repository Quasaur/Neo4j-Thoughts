---
type: QUOTE
name: "quote.CHRIST IS ENOUGH"
alias: "Quote: Christ is Enough"
parent: "topic.GRACE"
en_content: "I say to you again in the Name of The Father, Son and Holy Spirit and in the Presence of Heaven, Earth and all Creation: JESUS CHRIST IS ENOUGH to completely deliver any soul from damnation to Divine Perfection.",
 es_title: "Cita: CRISTO ES SUFICIENTE",
 es_content: "Les digo nuevamente en el Nombre del Padre, del Hijo y del Espíritu Santo y en la Presencia del Cielo, de la Tierra y de toda la Creación: JESUCRISTO ES BASTANTE para liberar completamente a cualquier alma de la condenación a la Perfección Divina.",
 fr_title: "Citation : CHRIST SUFFIT",
 fr_content: "Je vous le dis encore au Nom du Père, du Fils et du Saint-Esprit et en Présence du Ciel, de la Terre et de toute la Création : JÉSUS-CHRIST SUFFIT pour délivrer complètement toute âme de la damnation à la Perfection Divine.",
 hi_title: "उद्धरण: मसीह ही पर्याप्त है",
 hi_content: "मैं आपको पिता, पुत्र और पवित्र आत्मा के नाम पर और स्वर्ग, पृथ्वी और सारी सृष्टि की उपस्थिति में फिर से कहता हूं: यीशु मसीह किसी भी आत्मा को पूरी तरह से विनाश से दिव्य पूर्णता तक पहुंचाने के लिए पर्याप्त हैं।",
 zh_title: "yǐn yòng ： jī dū jiù zú gòu le",
 zh_content: "wǒ yǐ shèng fù 、 shèng zi hé shèng líng de míng yì ， bìng zài tiān 、 dì hé suǒ yǒu zào wù de miàn qián zài cì duì nǐ men shuō ： yē sū jī dū zú yǐ jiāng rèn hé líng hún cóng zǔ zhòu zhōng wán quán zhěng jiù dào shén shèng de wán měi 。"
tags: ["jesus_christ", "sufficient", "enough", "salvation", "redemption"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHRIST IS ENOUGH",
    alias: "Quote: Christ is Enough",
    parent: "topic.GRACE",
    tags: ["jesus_christ", "sufficient", "enough", "salvation", "redemption"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHRIST IS ENOUGH",
    ctype: "QUOTE",
    en_title: "Christ is Enough",
    en_content: "I say to you again in the Name of The Father, Son and Holy Spirit and in the Presence of Heaven, Earth and all Creation: JESUS CHRIST IS ENOUGH to completely deliver any soul from damnation to Divine Perfection.",
 es_title: "Cita: CRISTO ES SUFICIENTE",
 es_content: "Les digo nuevamente en el Nombre del Padre, del Hijo y del Espíritu Santo y en la Presencia del Cielo, de la Tierra y de toda la Creación: JESUCRISTO ES BASTANTE para liberar completamente a cualquier alma de la condenación a la Perfección Divina.",
 fr_title: "Citation : CHRIST SUFFIT",
 fr_content: "Je vous le dis encore au Nom du Père, du Fils et du Saint-Esprit et en Présence du Ciel, de la Terre et de toute la Création : JÉSUS-CHRIST SUFFIT pour délivrer complètement toute âme de la damnation à la Perfection Divine.",
 hi_title: "उद्धरण: मसीह ही पर्याप्त है",
 hi_content: "मैं आपको पिता, पुत्र और पवित्र आत्मा के नाम पर और स्वर्ग, पृथ्वी और सारी सृष्टि की उपस्थिति में फिर से कहता हूं: यीशु मसीह किसी भी आत्मा को पूरी तरह से विनाश से दिव्य पूर्णता तक पहुंचाने के लिए पर्याप्त हैं।",
 zh_title: "yǐn yòng ： jī dū jiù zú gòu le",
 zh_content: "wǒ yǐ shèng fù 、 shèng zi hé shèng líng de míng yì ， bìng zài tiān 、 dì hé suǒ yǒu zào wù de miàn qián zài cì duì nǐ men shuō ： yē sū jī dū zú yǐ jiāng rèn hé líng hún cóng zǔ zhòu zhōng wán quán zhěng jiù dào shén shèng de wán měi 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.CHRIST IS ENOUGH"})
MATCH (c:CONTENT {name: "content.CHRIST IS ENOUGH"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHRIST IS ENOUGH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.CHRIST IS ENOUGH"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->CHRIST IS ENOUGH"}]->(child);

```
