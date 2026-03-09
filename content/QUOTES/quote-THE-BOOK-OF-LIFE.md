---
type: QUOTE
name: "quote.THE BOOK OF LIFE"
alias: "Quote: The Book of Life"
parent: "topic.DIVINE-SOVEREIGNTY"
en_content: "As long as your name is written in the Lamb’s Book of LIFE, YOU HAVE NOTHING TO WORRY ABOUT WHATSOEVER; the Lake of Fire can do you no harm.",
 es_title: "Cita: EL LIBRO DE LA VIDA",
 es_content: "Mientras tu nombre esté escrito en el Libro de la VIDA del Cordero, NO TIENES NADA DE QUÉ PREOCUPARTE; el Lago de Fuego no puede hacerte daño.",
 fr_title: "Citation : LE LIVRE DE LA VIE",
 fr_content: "Tant que votre nom est écrit dans le Livre de VIE de l’Agneau, VOUS N’AVEZ RIEN À VOUS INQUIÉTER DE QUOI QUE CE SOIT ; le Lac de Feu ne peut vous faire aucun mal.",
 hi_title: "उद्धरण: जीवन की किताब",
 hi_content: "जब तक आपका नाम मेम्ने के जीवन की पुस्तक में लिखा है, आपको किसी भी चीज़ के बारे में चिंता करने की कोई आवश्यकता नहीं है; आग की झील तुम्हें कोई हानि नहीं पहुँचा सकती।",
 zh_title: "yǐn yòng ：《 shēng mìng zhī shū 》",
 zh_content: "zhǐ yào nǐ de míng zì xiě zài gāo yáng de shēng mìng cè shàng ， nǐ jiù wú xū dān xīn rèn hé shì qíng ； huǒ hú bú huì duì nǐ zào chéng shāng hài 。"
tags: ["lamb_of_god", "lake_of_fire", "book_of_life", "immunity", "fearless"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE BOOK OF LIFE",
    alias: "Quote: The Book of Life",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["lamb_of_god", "lake_of_fire", "book_of_life", "immunity", "fearless"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE BOOK OF LIFE",
    ctype: "QUOTE",
    en_title: "The Book of Life",
    en_content: "As long as your name is written in the Lamb’s Book of LIFE, YOU HAVE NOTHING TO WORRY ABOUT WHATSOEVER; the Lake of Fire can do you no harm.",
 es_title: "Cita: EL LIBRO DE LA VIDA",
 es_content: "Mientras tu nombre esté escrito en el Libro de la VIDA del Cordero, NO TIENES NADA DE QUÉ PREOCUPARTE; el Lago de Fuego no puede hacerte daño.",
 fr_title: "Citation : LE LIVRE DE LA VIE",
 fr_content: "Tant que votre nom est écrit dans le Livre de VIE de l’Agneau, VOUS N’AVEZ RIEN À VOUS INQUIÉTER DE QUOI QUE CE SOIT ; le Lac de Feu ne peut vous faire aucun mal.",
 hi_title: "उद्धरण: जीवन की किताब",
 hi_content: "जब तक आपका नाम मेम्ने के जीवन की पुस्तक में लिखा है, आपको किसी भी चीज़ के बारे में चिंता करने की कोई आवश्यकता नहीं है; आग की झील तुम्हें कोई हानि नहीं पहुँचा सकती।",
 zh_title: "yǐn yòng ：《 shēng mìng zhī shū 》",
 zh_content: "zhǐ yào nǐ de míng zì xiě zài gāo yáng de shēng mìng cè shàng ， nǐ jiù wú xū dān xīn rèn hé shì qíng ； huǒ hú bú huì duì nǐ zào chéng shāng hài 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE BOOK OF LIFE"})
MATCH (c:CONTENT {name: "content.THE BOOK OF LIFE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE BOOK OF LIFE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MATCH (child:QUOTE {name: "quote.THE BOOK OF LIFE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->THE BOOK OF LIFE"}]->(child);

```
