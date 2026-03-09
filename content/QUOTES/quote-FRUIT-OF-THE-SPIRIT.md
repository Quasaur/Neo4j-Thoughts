---
type: QUOTE
name: "quote.FRUIT OF THE SPIRIT"
alias: "Quote: Fruit of the Spirit"
parent: "topic.GRACE"
en_content: "Notice they're not called the Works of the Spirit but the Fruit of the Spirit. The Apostle is drawing a contrast between the WORKS of the flesh and the FRUIT of the Holy Spirit of GOD...subtle yet critical. 'Works...fruit...what does it matter?' Ahhhh...it does matter, and the difference determines the destiny of billions for Heaven or Hell!"
 es_title: "Cita: FRUTO DEL ESPÍRITU"
 es_content: "Note que no se llaman Obras del Espíritu sino Fruto del Espíritu. El Apóstol está haciendo un contraste entre las OBRAS de la carne y el FRUTO del Espíritu Santo de DIOS... sutil pero crítico. 'Funciona...fruta...¿qué importa?' Ahhhh... ¡sí importa, y la diferencia determina el destino de miles de millones al Cielo o al Infierno!"
 fr_title: "Citation : FRUIT DE L'ESPRIT"
 fr_content: "Remarquez qu’elles ne sont pas appelées les œuvres de l’Esprit mais le fruit de l’Esprit. L'Apôtre établit un contraste entre les ŒUVRES de la chair et le FRUIT du Saint-Esprit de DIEU... subtil mais critique. \"Ça marche... des fruits... qu'importe ?\" Ahhhh... c'est important, et la différence détermine le destin de milliards de personnes au paradis ou en enfer !"
 hi_title: "उद्धरण: आत्मा का फल"
 hi_content: "ध्यान दें कि उन्हें आत्मा का कार्य नहीं बल्कि आत्मा का फल कहा जाता है। प्रेरित शरीर के कार्यों और ईश्वर की पवित्र आत्मा के फल के बीच अंतर बता रहा है...सूक्ष्म फिर भी आलोचनात्मक। 'काम करता है...फल...इससे क्या फर्क पड़ता है?' आह...इससे फर्क पड़ता है, और यही फर्क अरबों लोगों की स्वर्ग या नर्क की नियति तय करता है!"
 zh_title: "yǐn yòng ： shèng líng de guǒ zi"
 zh_content: "qǐng zhù yì ， tā men bù bèi chēng wéi “ shèng líng de gōng zuò ”， ér shì “ shèng líng de guǒ zi ”。 shǐ tú jiāng ròu tǐ de xíng wéi yǔ shàng dì shèng líng de guǒ zi jìn xíng le duì bǐ …… wēi miào dàn zhì guān zhòng yào 。 “ yǒu xiào …… shuǐ guǒ …… yǒu shén me guān xì ？” a …… zhè què shí hěn zhòng yào ， chā yì jué dìng le shù shí yì rén de tiān táng huò dì yù de mìng yùn ！"
tags: ["works", "fruit", "flow", "livingwater", "tree"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FRUIT OF THE SPIRIT",
    alias: "Quote: Fruit of the Spirit",
    parent: "topic.GRACE",
    tags: ["works", "fruit", "flow", "livingwater", "tree"],
    source: "'The Narrow Way'",
    booklink: "()",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FRUIT OF THE SPIRIT",
    ctype: "QUOTE",
    en_title: "Fruit of the Spirit",
    en_content: "Notice they're not called the Works of the Spirit but the Fruit of the Spirit. The Apostle is drawing a contrast between the WORKS of the flesh and the FRUIT of the Holy Spirit of GOD...subtle yet critical. 'Works...fruit...what does it matter?' Ahhhh...it does matter, and the difference determines the destiny of billions for Heaven or Hell!",
 es_title: "Cita: FRUTO DEL ESPÍRITU",
 es_content: "Note que no se llaman Obras del Espíritu sino Fruto del Espíritu. El Apóstol está haciendo un contraste entre las OBRAS de la carne y el FRUTO del Espíritu Santo de DIOS... sutil pero crítico. 'Funciona...fruta...¿qué importa?' Ahhhh... ¡sí importa, y la diferencia determina el destino de miles de millones al Cielo o al Infierno!",
 fr_title: "Citation : FRUIT DE L'ESPRIT",
 fr_content: "Remarquez qu’elles ne sont pas appelées les œuvres de l’Esprit mais le fruit de l’Esprit. L'Apôtre établit un contraste entre les ŒUVRES de la chair et le FRUIT du Saint-Esprit de DIEU... subtil mais critique. \"Ça marche... des fruits... qu'importe ?\" Ahhhh... c'est important, et la différence détermine le destin de milliards de personnes au paradis ou en enfer !",
 hi_title: "उद्धरण: आत्मा का फल",
 hi_content: "ध्यान दें कि उन्हें आत्मा का कार्य नहीं बल्कि आत्मा का फल कहा जाता है। प्रेरित शरीर के कार्यों और ईश्वर की पवित्र आत्मा के फल के बीच अंतर बता रहा है...सूक्ष्म फिर भी आलोचनात्मक। 'काम करता है...फल...इससे क्या फर्क पड़ता है?' आह...इससे फर्क पड़ता है, और यही फर्क अरबों लोगों की स्वर्ग या नर्क की नियति तय करता है!",
 zh_title: "yǐn yòng ： shèng líng de guǒ zi",
 zh_content: "qǐng zhù yì ， tā men bù bèi chēng wéi “ shèng líng de gōng zuò ”， ér shì “ shèng líng de guǒ zi ”。 shǐ tú jiāng ròu tǐ de xíng wéi yǔ shàng dì shèng líng de guǒ zi jìn xíng le duì bǐ …… wēi miào dàn zhì guān zhòng yào 。 “ yǒu xiào …… shuǐ guǒ …… yǒu shén me guān xì ？” a …… zhè què shí hěn zhòng yào ， chā yì jué dìng le shù shí yì rén de tiān táng huò dì yù de mìng yùn ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.FRUIT OF THE SPIRIT"})
MATCH (c:CONTENT {name: "content.FRUIT OF THE SPIRIT"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FRUIT OF THE SPIRIT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.FRUIT OF THE SPIRIT"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->FRUIT OF THE SPIRIT"}]->(child);
```