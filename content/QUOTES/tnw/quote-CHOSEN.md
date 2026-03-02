---
type: QUOTE
name: "quote.CHOSEN"
alias: "Quote: Quote: CHOSEN"
parent: "topic.DIVINE-SOVEREIGNTY"
en_content: "Contrary to popular American religious legend that passes for sound Christian doctrine, the choice that COUNTS towards your ultimate eternal fate and mine is not our decisions but GOD's (John 15:16).",
 es_title: "Cita: ELEGIDO",
 es_content: "Contrariamente a la leyenda religiosa popular estadounidense que pasa por sana doctrina cristiana, la elección que CUENTA para su destino eterno final y el mío no es nuestra decisión sino la de DIOS (Juan 15:16).",
 fr_title: "Citation : CHOISI",
 fr_content: "Contrairement à la légende religieuse américaine populaire qui passe pour une saine doctrine chrétienne, le choix qui COMPTE pour votre destin éternel ultime et le mien n'est pas notre décision mais celle de DIEU (Jean 15 : 16).",
 hi_title: "उद्धरण: चुना गया",
 hi_content: "लोकप्रिय अमेरिकी धार्मिक किंवदंती के विपरीत, जो ठोस ईसाई सिद्धांत से गुजरती है, आपके और मेरे अंतिम शाश्वत भाग्य के लिए जो विकल्प मायने रखता है वह हमारा निर्णय नहीं बल्कि भगवान का है (जॉन 15:16)।",
 zh_title: "yǐn yòng ： xuǎn zé",
 zh_content: "yǔ bèi rèn wéi shì chún zhèng jī dū jiào jiào yì de měi guó liú xíng zōng jiào chuán shuō xiāng fǎn ， duì nǐ wǒ zuì zhōng yǒng héng mìng yùn zhì guān zhòng yào de xuǎn zé bú shì wǒ men de jué dìng ， ér shì shàng dì de jué dìng （ yuē hàn fú yīn 15:16）。"
tags: ["chosen", "god", "sovereignty", "jesus_christ", "eternity"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHOSEN",
    alias: "Quote: Quote: CHOSEN",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["chosen", "god", "sovereignty", "jesus_christ", "eternity"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHOSEN",
    ctype: "QUOTE",
    en_title: "Quote: CHOSEN",
    en_content: "Contrary to popular American religious legend that passes for sound Christian doctrine, the choice that COUNTS towards your ultimate eternal fate and mine is not our decisions but GOD's (John 15:16).",
 es_title: "Cita: ELEGIDO",
 es_content: "Contrariamente a la leyenda religiosa popular estadounidense que pasa por sana doctrina cristiana, la elección que CUENTA para su destino eterno final y el mío no es nuestra decisión sino la de DIOS (Juan 15:16).",
 fr_title: "Citation : CHOISI",
 fr_content: "Contrairement à la légende religieuse américaine populaire qui passe pour une saine doctrine chrétienne, le choix qui COMPTE pour votre destin éternel ultime et le mien n'est pas notre décision mais celle de DIEU (Jean 15 : 16).",
 hi_title: "उद्धरण: चुना गया",
 hi_content: "लोकप्रिय अमेरिकी धार्मिक किंवदंती के विपरीत, जो ठोस ईसाई सिद्धांत से गुजरती है, आपके और मेरे अंतिम शाश्वत भाग्य के लिए जो विकल्प मायने रखता है वह हमारा निर्णय नहीं बल्कि भगवान का है (जॉन 15:16)।",
 zh_title: "yǐn yòng ： xuǎn zé",
 zh_content: "yǔ bèi rèn wéi shì chún zhèng jī dū jiào jiào yì de měi guó liú xíng zōng jiào chuán shuō xiāng fǎn ， duì nǐ wǒ zuì zhōng yǒng héng mìng yùn zhì guān zhòng yào de xuǎn zé bú shì wǒ men de jué dìng ， ér shì shàng dì de jué dìng （ yuē hàn fú yīn 15:16）。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.CHOSEN"})
MATCH (c:CONTENT {name: "content.CHOSEN"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHOSEN"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MATCH (child:QUOTE {name: "quote.CHOSEN"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->CHOSEN"}]->(child);

```
