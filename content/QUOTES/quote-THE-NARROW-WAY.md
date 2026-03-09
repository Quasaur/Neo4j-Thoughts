---
type: QUOTE
name: "quote.THE NARROW WAY"
alias: "Quote: The Narrow Way"
parent: "topic.THE-GOSPEL"
source: "'The Narrow Way'"
en_content: "As the only means to peace with our Creator, the Narrow Way (the Gospel) must be communicated with clarity and simplicity. Declared properly, the Narrow Way will always push me into a corner and compel me to decide against my self and for GOD. The Objective of Salvation is not to get GOD on my side, but to get me to take the side of GOD against my self!",
 es_title: "Cita: EL CAMINO ESTRECHO",
 es_content: "Como único medio para la paz con nuestro Creador, el Camino Estrecho (el Evangelio) debe comunicarse con claridad y sencillez. Declarado correctamente, el Camino Estrecho siempre me arrinconará y me obligará a decidir en contra de mí mismo y por DIOS. ¡El Objetivo de la Salvación no es poner a DIOS de mi lado, sino hacer que yo me ponga del lado de DIOS contra mí mismo!",
 fr_title: "Citation : LE CHEMIN ÉTROIT",
 fr_content: "En tant que seul moyen de parvenir à la paix avec notre Créateur, le Chemin Étroit (l’Évangile) doit être communiqué avec clarté et simplicité. Déclarée correctement, la Voie Étroite me poussera toujours dans un coin et m'obligera à décider contre moi-même et pour DIEU. L’objectif du salut n’est pas d’avoir DIEU de mon côté, mais de m’amener à prendre le parti de DIEU contre moi-même !",
 hi_title: "उद्धरण: संकीर्ण रास्ता",
 hi_content: "हमारे निर्माता के साथ शांति के एकमात्र साधन के रूप में, संकीर्ण मार्ग (सुसमाचार) को स्पष्टता और सरलता के साथ संप्रेषित किया जाना चाहिए। उचित रूप से घोषित, संकीर्ण मार्ग मुझे हमेशा एक कोने में धकेल देगा और मुझे अपने स्वयं के खिलाफ और भगवान के लिए निर्णय लेने के लिए मजबूर करेगा। मुक्ति का उद्देश्य ईश्वर को अपने पक्ष में करना नहीं है, बल्कि मुझे अपने विरुद्ध ईश्वर का पक्ष लेने के लिए प्रेरित करना है!",
 zh_title: "yǐn yòng ： xiá zhǎi de dào lù",
 zh_content: "zuò wéi yǔ wǒ men de zào wù zhǔ hé píng xiāng chǔ de wéi yī tú jìng ， zhǎi lù （ fú yīn ） bì xū qīng xī jiǎn dān dì chuán dá 。 rú guǒ shēng míng dé dàng ， zhǎi lù zǒng shì huì bǎ wǒ bī dào qiáng jiǎo ， pò shǐ wǒ zuò chū fǎn duì zì wǒ 、 zhī chí shàng dì de jué dìng 。 jiù shú de mù dì bú shì ràng shén zhàn zài wǒ zhè yī biān ， ér shì ràng wǒ zhàn zài shén yī biān fǎn duì wǒ zì jǐ ！"
tags: ["god", "peace", "reconciliation", "self_denial", "submission"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE NARROW WAY",
    alias: "Quote: The Narrow Way",
    parent: "topic.THE-GOSPEL",
    tags: ["god", "peace", "reconciliation", "self_denial", "submission"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE NARROW WAY",
    ctype: "QUOTE",
    en_title: "The Narrow Way",
    en_content: "As the only means to peace with our Creator, the Narrow Way (the Gospel) must be communicated with clarity and simplicity. Declared properly, the Narrow Way will always push me into a corner and compel me to decide against my self and for GOD. The Objective of Salvation is not to get GOD on my side, but to get me to take the side of GOD against my self!",
 es_title: "Cita: EL CAMINO ESTRECHO",
 es_content: "Como único medio para la paz con nuestro Creador, el Camino Estrecho (el Evangelio) debe comunicarse con claridad y sencillez. Declarado correctamente, el Camino Estrecho siempre me arrinconará y me obligará a decidir en contra de mí mismo y por DIOS. ¡El Objetivo de la Salvación no es poner a DIOS de mi lado, sino hacer que yo me ponga del lado de DIOS contra mí mismo!",
 fr_title: "Citation : LE CHEMIN ÉTROIT",
 fr_content: "En tant que seul moyen de parvenir à la paix avec notre Créateur, le Chemin Étroit (l’Évangile) doit être communiqué avec clarté et simplicité. Déclarée correctement, la Voie Étroite me poussera toujours dans un coin et m'obligera à décider contre moi-même et pour DIEU. L’objectif du salut n’est pas d’avoir DIEU de mon côté, mais de m’amener à prendre le parti de DIEU contre moi-même !",
 hi_title: "उद्धरण: संकीर्ण रास्ता",
 hi_content: "हमारे निर्माता के साथ शांति के एकमात्र साधन के रूप में, संकीर्ण मार्ग (सुसमाचार) को स्पष्टता और सरलता के साथ संप्रेषित किया जाना चाहिए। उचित रूप से घोषित, संकीर्ण मार्ग मुझे हमेशा एक कोने में धकेल देगा और मुझे अपने स्वयं के खिलाफ और भगवान के लिए निर्णय लेने के लिए मजबूर करेगा। मुक्ति का उद्देश्य ईश्वर को अपने पक्ष में करना नहीं है, बल्कि मुझे अपने विरुद्ध ईश्वर का पक्ष लेने के लिए प्रेरित करना है!",
 zh_title: "yǐn yòng ： xiá zhǎi de dào lù",
 zh_content: "zuò wéi yǔ wǒ men de zào wù zhǔ hé píng xiāng chǔ de wéi yī tú jìng ， zhǎi lù （ fú yīn ） bì xū qīng xī jiǎn dān dì chuán dá 。 rú guǒ shēng míng dé dàng ， zhǎi lù zǒng shì huì bǎ wǒ bī dào qiáng jiǎo ， pò shǐ wǒ zuò chū fǎn duì zì wǒ 、 zhī chí shàng dì de jué dìng 。 jiù shú de mù dì bú shì ràng shén zhàn zài wǒ zhè yī biān ， ér shì ràng wǒ zhàn zài shén yī biān fǎn duì wǒ zì jǐ ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE NARROW WAY"})
MATCH (c:CONTENT {name: "content.THE NARROW WAY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE NARROW WAY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MATCH (child:QUOTE {name: "quote.THE NARROW WAY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->THE NARROW WAY"}]->(child);

```
