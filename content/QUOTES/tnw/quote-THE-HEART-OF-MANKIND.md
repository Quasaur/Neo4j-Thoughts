---
type: QUOTE
name: "quote.THE_HEART_OF_MANKIND"
alias: "Quote: Quote: The HEART OF MANKIND"
parent: "topic.RELIGION"
en_content: "None of our achievements, advances, contributions, virtuous deeds or good intentions make up for our evil hearts (hearts that believe GOD is not necessary to live a fulfilling life) ...else Christ would not have had to present Himself as a Sacrifice in our stead.",
 es_title: "Cita: El CORAZÓN DE LA HUMANIDAD",
 es_content: "Ninguno de nuestros logros, avances, contribuciones, obras virtuosas o buenas intenciones compensan nuestros corazones malvados (corazones que creen que DIOS no es necesario para vivir una vida plena)...de lo contrario, Cristo no habría tenido que presentarse como un Sacrificio en nuestro lugar.",
 fr_title: "Citation : Le CŒUR DE L'HOMME",
 fr_content: "Aucune de nos réalisations, avancées, contributions, actes vertueux ou bonnes intentions ne compense nos mauvais cœurs (des cœurs qui croient que DIEU n'est pas nécessaire pour vivre une vie épanouie)... sinon Christ n'aurait pas eu à se présenter comme un sacrifice à notre place.",
 hi_title: "उद्धरण: मानवजाति का हृदय",
 hi_content: "हमारी कोई भी उपलब्धि, उन्नति, योगदान, अच्छे कर्म या अच्छे इरादे हमारे बुरे दिलों की भरपाई नहीं करते (वे दिल जो मानते हैं कि भगवान को एक पूर्ण जीवन जीने के लिए आवश्यक नहीं है) ... अन्यथा मसीह को हमारे स्थान पर खुद को बलिदान के रूप में प्रस्तुत नहीं करना पड़ता।",
 zh_title: "yǐn yòng ： rén lèi zhī xīn",
 zh_content: "wǒ men de chéng jiù 、 jìn bù 、 gòng xiàn 、 měi dé xíng wèi huò shàn yì dōu wú fǎ mí bǔ wǒ men xié è de xīn （ xiāng xìn shàng dì bù xū yào guò shàng chōng shí de shēng huó de xīn ）…… fǒu zé jī dū jiù bù bì dài tì wǒ men xī shēng zì jǐ 。"
tags: ["heart", "human", "ungodly", "jesus_christ", "propitiation"]
ptopic: "[[topic-RELIGION]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_HEART_OF_MANKIND",
    alias: "Quote: Quote: The HEART OF MANKIND",
    parent: "topic.RELIGION",
    tags: ["heart", "human", "ungodly", "jesus_christ", "propitiation"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_HEART_OF_MANKIND",
    ctype: "QUOTE",
    en_title: "Quote: The HEART OF MANKIND",
    en_content: "None of our achievements, advances, contributions, virtuous deeds or good intentions make up for our evil hearts (hearts that believe GOD is not necessary to live a fulfilling life) ...else Christ would not have had to present Himself as a Sacrifice in our stead.",
 es_title: "Cita: El CORAZÓN DE LA HUMANIDAD",
 es_content: "Ninguno de nuestros logros, avances, contribuciones, obras virtuosas o buenas intenciones compensan nuestros corazones malvados (corazones que creen que DIOS no es necesario para vivir una vida plena)...de lo contrario, Cristo no habría tenido que presentarse como un Sacrificio en nuestro lugar.",
 fr_title: "Citation : Le CŒUR DE L'HOMME",
 fr_content: "Aucune de nos réalisations, avancées, contributions, actes vertueux ou bonnes intentions ne compense nos mauvais cœurs (des cœurs qui croient que DIEU n'est pas nécessaire pour vivre une vie épanouie)... sinon Christ n'aurait pas eu à se présenter comme un sacrifice à notre place.",
 hi_title: "उद्धरण: मानवजाति का हृदय",
 hi_content: "हमारी कोई भी उपलब्धि, उन्नति, योगदान, अच्छे कर्म या अच्छे इरादे हमारे बुरे दिलों की भरपाई नहीं करते (वे दिल जो मानते हैं कि भगवान को एक पूर्ण जीवन जीने के लिए आवश्यक नहीं है) ... अन्यथा मसीह को हमारे स्थान पर खुद को बलिदान के रूप में प्रस्तुत नहीं करना पड़ता।",
 zh_title: "yǐn yòng ： rén lèi zhī xīn",
 zh_content: "wǒ men de chéng jiù 、 jìn bù 、 gòng xiàn 、 měi dé xíng wèi huò shàn yì dōu wú fǎ mí bǔ wǒ men xié è de xīn （ xiāng xìn shàng dì bù xū yào guò shàng chōng shí de shēng huó de xīn ）…… fǒu zé jī dū jiù bù bì dài tì wǒ men xī shēng zì jǐ 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_HEART_OF_MANKIND"})
MATCH (c:CONTENT {name: "content.THE_HEART_OF_MANKIND"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_HEART_OF_MANKIND"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:QUOTE {name: "quote.THE_HEART_OF_MANKIND"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->THE_HEART_OF_MANKIND"}]->(child);

```
