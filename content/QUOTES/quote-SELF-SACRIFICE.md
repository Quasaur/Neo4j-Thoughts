---
type: QUOTE
name: "quote.SELF-SACRIFICE"
alias: "Quote: Self-sacrifice"
parent: "topic.HUMILITY"
source: "'The Narrow Way'"
en_content: "Did i drift off topic, Dear Reader? Not at all; the spirit of worship, obedience and self-sacrifice for the Glory of GOD is the product of True, Divinely-given Faith that exists in the heart, and not just the mind. GOD gave up That which was EVERYTHING to Him to love you; and if you truly desire to be filled with His Holy Spirit, That Selfsame Member of the Eternal GODHEAD will inspire you to the same level of self-sacrificial love we see in Christ Himself.",
 es_title: "Cita: AUTOSACRIFICIO",
 es_content: "¿Me desvié del tema, querido lector? De nada; El espíritu de adoración, obediencia y autosacrificio para la Gloria de DIOS es el producto de la Fe Verdadera y Divina que existe en el corazón, y no solo en la mente. DIOS entregó Aquello que era TODO para Él para amarte; y si realmente deseas ser lleno de Su Espíritu Santo, Ese Mismo Miembro de la DIOS Eterna te inspirará al mismo nivel de amor abnegado que vemos en Cristo mismo.",
 fr_title: "Citation : SACRIFICE DE SOI",
 fr_content: "Ai-je dérivé du sujet, cher lecteur ? Pas du tout; l'esprit d'adoration, d'obéissance et d'abnégation pour la gloire de DIEU est le produit de la vraie foi divinement donnée qui existe dans le cœur, et pas seulement dans l'esprit. DIEU a abandonné Ce qui était TOUT pour Lui pour t'aimer ; et si vous désirez vraiment être rempli de Son Saint-Esprit, ce même membre de la DIVINITÉ Éternelle vous inspirera le même niveau d’amour sacrificiel que nous voyons en Christ lui-même.",
 hi_title: "उद्धरण: आत्म-बलिदान",
 hi_content: "क्या मैं विषय से भटक गया, प्रिय पाठक? बिल्कुल नहीं; ईश्वर की महिमा के लिए पूजा, आज्ञाकारिता और आत्म-बलिदान की भावना सच्चे, दैवीय प्रदत्त विश्वास का उत्पाद है जो हृदय में मौजूद है, न कि केवल दिमाग में। परमेश्वर ने आपसे प्रेम करने के लिए वह सब कुछ त्याग दिया जो उसके लिए सब कुछ था; और यदि आप वास्तव में उनकी पवित्र आत्मा से परिपूर्ण होने की इच्छा रखते हैं, तो शाश्वत ईश्वर का वही सदस्य आपको उसी स्तर के आत्म-बलिदान प्रेम के लिए प्रेरित करेगा जो हम स्वयं मसीह में देखते हैं।",
 zh_title: "yǐn yòng ： zì wǒ xī shēng",
 zh_content: "qīn ài de dú zhě ， wǒ shì bú shì piān lí le zhǔ tí ？ yì diǎn yě bù ; wèi le shàng dì de róng yào ér chóng bài 、 fú cóng hé zì wǒ xī shēng de jīng shén shì cún zài yú nèi xīn ér bù jǐn jǐn shì tóu nǎo zhōng de zhēn shí de 、 shén shèng de xìn yǎng de chǎn wù 。 shén wèi le ài nǐ ér fàng qì le tā de yī qiè ； rú guǒ nǐ zhēn de kě wàng bèi tā de shèng líng chōng mǎn ， nà yǒng héng shén xìng de tóng yī gè chéng yuán jiāng jī lì nǐ dá dào wǒ men zài jī dū shēn shàng kàn dào de tóng yàng shuǐ píng de zì wǒ xī shēng zhī ài 。"
tags: ["self_sacrifice", "submission", "offering", "love", "christfirst"]
ptopic: "[[topic-HUMILITY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SELF-SACRIFICE",
    alias: "Quote: Self-sacrifice",
    parent: "topic.HUMILITY",
    tags: ["self_sacrifice", "submission", "offering", "love", "christfirst"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SELF-SACRIFICE",
    ctype: "QUOTE",
    en_title: "Self-sacrifice",
    en_content: "Did i drift off topic, Dear Reader? Not at all; the spirit of worship, obedience and self-sacrifice for the Glory of GOD is the product of True, Divinely-given Faith that exists in the heart, and not just the mind. GOD gave up That which was EVERYTHING to Him to love you; and if you truly desire to be filled with His Holy Spirit, That Selfsame Member of the Eternal GODHEAD will inspire you to the same level of self-sacrificial love we see in Christ Himself.",
 es_title: "Cita: AUTOSACRIFICIO",
 es_content: "¿Me desvié del tema, querido lector? De nada; El espíritu de adoración, obediencia y autosacrificio para la Gloria de DIOS es el producto de la Fe Verdadera y Divina que existe en el corazón, y no solo en la mente. DIOS entregó Aquello que era TODO para Él para amarte; y si realmente deseas ser lleno de Su Espíritu Santo, Ese Mismo Miembro de la DIOS Eterna te inspirará al mismo nivel de amor abnegado que vemos en Cristo mismo.",
 fr_title: "Citation : SACRIFICE DE SOI",
 fr_content: "Ai-je dérivé du sujet, cher lecteur ? Pas du tout; l'esprit d'adoration, d'obéissance et d'abnégation pour la gloire de DIEU est le produit de la vraie foi divinement donnée qui existe dans le cœur, et pas seulement dans l'esprit. DIEU a abandonné Ce qui était TOUT pour Lui pour t'aimer ; et si vous désirez vraiment être rempli de Son Saint-Esprit, ce même membre de la DIVINITÉ Éternelle vous inspirera le même niveau d’amour sacrificiel que nous voyons en Christ lui-même.",
 hi_title: "उद्धरण: आत्म-बलिदान",
 hi_content: "क्या मैं विषय से भटक गया, प्रिय पाठक? बिल्कुल नहीं; ईश्वर की महिमा के लिए पूजा, आज्ञाकारिता और आत्म-बलिदान की भावना सच्चे, दैवीय प्रदत्त विश्वास का उत्पाद है जो हृदय में मौजूद है, न कि केवल दिमाग में। परमेश्वर ने आपसे प्रेम करने के लिए वह सब कुछ त्याग दिया जो उसके लिए सब कुछ था; और यदि आप वास्तव में उनकी पवित्र आत्मा से परिपूर्ण होने की इच्छा रखते हैं, तो शाश्वत ईश्वर का वही सदस्य आपको उसी स्तर के आत्म-बलिदान प्रेम के लिए प्रेरित करेगा जो हम स्वयं मसीह में देखते हैं।",
 zh_title: "yǐn yòng ： zì wǒ xī shēng",
 zh_content: "qīn ài de dú zhě ， wǒ shì bú shì piān lí le zhǔ tí ？ yì diǎn yě bù ; wèi le shàng dì de róng yào ér chóng bài 、 fú cóng hé zì wǒ xī shēng de jīng shén shì cún zài yú nèi xīn ér bù jǐn jǐn shì tóu nǎo zhōng de zhēn shí de 、 shén shèng de xìn yǎng de chǎn wù 。 shén wèi le ài nǐ ér fàng qì le tā de yī qiè ； rú guǒ nǐ zhēn de kě wàng bèi tā de shèng líng chōng mǎn ， nà yǒng héng shén xìng de tóng yī gè chéng yuán jiāng jī lì nǐ dá dào wǒ men zài jī dū shēn shàng kàn dào de tóng yàng shuǐ píng de zì wǒ xī shēng zhī ài 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.SELF-SACRIFICE"})
MATCH (c:CONTENT {name: "content.SELF-SACRIFICE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SELF-SACRIFICE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.HUMILITY"})
MATCH (child:QUOTE {name: "quote.SELF-SACRIFICE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.HUMILITY->SELF-SACRIFICE"}]->(child);

```
