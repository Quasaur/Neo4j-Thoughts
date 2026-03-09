---
type: QUOTE
name: "quote.THE TEN COMMANDMENTS"
alias: "Quote: The Ten Commandments"
parent: "topic.LAW"
en_content: "God places an INESTIMABLE VALUE upon the Ten Commandments; and it deeply concerns me that so many of today's Christians take NO TIME to familiarize themselves with any of the first five books of the Bible which clearly identify the One True God in no uncertain terms.",
 es_title: "Cita: LOS DIEZ MANDAMIENTOS",
 es_content: "Dios pone un VALOR INESTIMABLE a los Diez Mandamientos; y me preocupa profundamente que muchos de los cristianos de hoy NO se tomen TIEMPO para familiarizarse con cualquiera de los primeros cinco libros de la Biblia que identifican claramente al Único Dios Verdadero en términos inequívocos.",
 fr_title: "Citation : LES DIX COMMANDEMENTS",
 fr_content: "Dieu accorde une VALEUR INESTIMABLE aux Dix Commandements ; et cela me préoccupe profondément qu'un si grand nombre de chrétiens d'aujourd'hui ne prennent AUCUN TEMPS pour se familiariser avec l'un des cinq premiers livres de la Bible qui identifient clairement le Seul Vrai Dieu en termes non équivoques.",
 hi_title: "उद्धरण: दस आज्ञाएँ",
 hi_content: "भगवान दस आज्ञाओं को अमूल्य महत्व देते हैं; और यह मुझे गहराई से चिंतित करता है कि आज के बहुत से ईसाइयों को बाइबिल की पहली पांच पुस्तकों में से किसी से परिचित होने में कोई समय नहीं लगता है जो बिना किसी अनिश्चित शब्दों के स्पष्ट रूप से एक सच्चे ईश्वर की पहचान करती है।",
 zh_title: "yǐn yòng ： shí jiè",
 zh_content: "shàng dì fù yǔ shí jiè bù kě gū liáng de jià zhí ； lìng wǒ shēn gǎn dān yōu de shì ， jīn tiān yǒu rú cǐ duō de jī dū tú méi yǒu shí jiān qù shú xī 《 shèng jīng 》 qián wǔ běn shū zhōng de rèn hé yī běn shū ， zhè xiē shū yǐ míng què de shù yǔ qīng chǔ dì shí bié le dú yī de zhēn shén 。"
tags: ["peace", "perfect", "grace", "holiness", "love"]
ptopic: "[[topic-LAW]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE TEN COMMANDMENTS",
    alias: "Quote: The Ten Commandments",
    parent: "topic.LAW",
    tags: ["peace", "perfect", "grace", "holiness", "love"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE TEN COMMANDMENTS",
    ctype: "QUOTE",
    en_title: "The Ten Commandments",
    en_content: "God places an INESTIMABLE VALUE upon the Ten Commandments; and it deeply concerns me that so many of today's Christians take NO TIME to familiarize themselves with any of the first five books of the Bible which clearly identify the One True God in no uncertain terms.",
 es_title: "Cita: LOS DIEZ MANDAMIENTOS",
 es_content: "Dios pone un VALOR INESTIMABLE a los Diez Mandamientos; y me preocupa profundamente que muchos de los cristianos de hoy NO se tomen TIEMPO para familiarizarse con cualquiera de los primeros cinco libros de la Biblia que identifican claramente al Único Dios Verdadero en términos inequívocos.",
 fr_title: "Citation : LES DIX COMMANDEMENTS",
 fr_content: "Dieu accorde une VALEUR INESTIMABLE aux Dix Commandements ; et cela me préoccupe profondément qu'un si grand nombre de chrétiens d'aujourd'hui ne prennent AUCUN TEMPS pour se familiariser avec l'un des cinq premiers livres de la Bible qui identifient clairement le Seul Vrai Dieu en termes non équivoques.",
 hi_title: "उद्धरण: दस आज्ञाएँ",
 hi_content: "भगवान दस आज्ञाओं को अमूल्य महत्व देते हैं; और यह मुझे गहराई से चिंतित करता है कि आज के बहुत से ईसाइयों को बाइबिल की पहली पांच पुस्तकों में से किसी से परिचित होने में कोई समय नहीं लगता है जो बिना किसी अनिश्चित शब्दों के स्पष्ट रूप से एक सच्चे ईश्वर की पहचान करती है।",
 zh_title: "yǐn yòng ： shí jiè",
 zh_content: "shàng dì fù yǔ shí jiè bù kě gū liáng de jià zhí ； lìng wǒ shēn gǎn dān yōu de shì ， jīn tiān yǒu rú cǐ duō de jī dū tú méi yǒu shí jiān qù shú xī 《 shèng jīng 》 qián wǔ běn shū zhōng de rèn hé yī běn shū ， zhè xiē shū yǐ míng què de shù yǔ qīng chǔ dì shí bié le dú yī de zhēn shén 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE TEN COMMANDMENTS"})
MATCH (c:CONTENT {name: "content.THE TEN COMMANDMENTS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE TEN COMMANDMENTS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.LAW"})
MATCH (child:QUOTE {name: "quote.THE TEN COMMANDMENTS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.LAW->THE TEN COMMANDMENTS"}]->(child);

```
