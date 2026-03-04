---
type: QUOTE
name: "quote.PERFORMANCE"
alias: "Quote: Performance"
parent: "topic.RELIGION"
en_content: "Doubt: As long as ANY PART of your Salvation is dependent upon your performance rather than Christ’s Righteousness, you can NEVER be assured of your Eternal Salvation nor of your name’s place in the Lamb’s Book of LIFE.",
 es_title: "Cita: RENDIMIENTO",
 es_content: "Duda: Mientras CUALQUIER PARTE de tu Salvación dependa de tu desempeño y no de la Justicia de Cristo, NUNCA podrás estar seguro de tu Salvación Eterna ni del lugar de tu nombre en el Libro de la VIDA del Cordero.",
 fr_title: "Citation : PERFORMANCE",
 fr_content: "Doute : Tant que TOUTE PARTIE de votre salut dépend de votre performance plutôt que de la justice du Christ, vous ne pouvez JAMAIS être assuré de votre salut éternel ni de la place de votre nom dans le Livre de VIE de l’Agneau.",
 hi_title: "उद्धरण: प्रदर्शन",
 hi_content: "संदेह: जब तक आपके उद्धार का कोई भी हिस्सा मसीह की धार्मिकता के बजाय आपके प्रदर्शन पर निर्भर है, तब तक आप कभी भी अपने शाश्वत उद्धार के बारे में आश्वस्त नहीं हो सकते हैं और न ही मेम्ने के जीवन की पुस्तक में आपके नाम के स्थान के बारे में आश्वस्त हो सकते हैं।",
 zh_title: "yǐn yòng ： xìng néng",
 zh_content: "huái yí ： zhǐ yào nǐ de jiù ēn de rèn hé bù fèn qǔ jué yú nǐ de biǎo xiàn ér bú shì jī dū de yì ， nǐ jiù yǒng yuǎn wú fǎ bǎo zhèng nǐ de yǒng héng jiù ēn ， yě wú fǎ bǎo zhèng nǐ de míng zì zài gāo yáng shēng mìng cè shàng de wèi zhì 。"
tags: ["doubt", "performance", "christ", "righteousness", "assurance"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.PERFORMANCE",
    alias: "Quote: Performance",
    parent: "topic.RELIGION",
    tags: ["doubt", "performance", "christ", "righteousness", "assurance"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PERFORMANCE",
    ctype: "QUOTE",
    en_title: "Performance",
    en_content: "Doubt: As long as ANY PART of your Salvation is dependent upon your performance rather than Christ’s Righteousness, you can NEVER be assured of your Eternal Salvation nor of your name’s place in the Lamb’s Book of LIFE.",
 es_title: "Cita: RENDIMIENTO",
 es_content: "Duda: Mientras CUALQUIER PARTE de tu Salvación dependa de tu desempeño y no de la Justicia de Cristo, NUNCA podrás estar seguro de tu Salvación Eterna ni del lugar de tu nombre en el Libro de la VIDA del Cordero.",
 fr_title: "Citation : PERFORMANCE",
 fr_content: "Doute : Tant que TOUTE PARTIE de votre salut dépend de votre performance plutôt que de la justice du Christ, vous ne pouvez JAMAIS être assuré de votre salut éternel ni de la place de votre nom dans le Livre de VIE de l’Agneau.",
 hi_title: "उद्धरण: प्रदर्शन",
 hi_content: "संदेह: जब तक आपके उद्धार का कोई भी हिस्सा मसीह की धार्मिकता के बजाय आपके प्रदर्शन पर निर्भर है, तब तक आप कभी भी अपने शाश्वत उद्धार के बारे में आश्वस्त नहीं हो सकते हैं और न ही मेम्ने के जीवन की पुस्तक में आपके नाम के स्थान के बारे में आश्वस्त हो सकते हैं।",
 zh_title: "yǐn yòng ： xìng néng",
 zh_content: "huái yí ： zhǐ yào nǐ de jiù ēn de rèn hé bù fèn qǔ jué yú nǐ de biǎo xiàn ér bú shì jī dū de yì ， nǐ jiù yǒng yuǎn wú fǎ bǎo zhèng nǐ de yǒng héng jiù ēn ， yě wú fǎ bǎo zhèng nǐ de míng zì zài gāo yáng shēng mìng cè shàng de wèi zhì 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.PERFORMANCE"})
MATCH (c:CONTENT {name: "content.PERFORMANCE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.PERFORMANCE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:QUOTE {name: "quote.PERFORMANCE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->PERFORMANCE"}]->(child);

```
