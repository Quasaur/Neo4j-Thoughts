---
type: QUOTE
name: "quote.NORMAL-REALITY"
alias: "Quote: Normal-reality"
parent: "topic.TRUTH"
en_content: "Other things happened, but what i most strongly desire to convey to you is that the lives we experience in this world are NOT as real as Eternity. We live in a temporary sub-reality that is the result of humanity being disconnected from our Great and Precious Heavenly Father. The experience i was granted is NORMAL REALITY...the environment we were MEANT to be born into and live our lives in!!!",
 es_title: "Cita: REALIDAD NORMAL",
 es_content: "Sucedieron otras cosas, pero lo que más deseo transmitirles es que las vidas que experimentamos en este mundo NO son tan reales como la Eternidad. Vivimos en una subrealidad temporal que es el resultado de la desconexión de la humanidad de nuestro Gran y Precioso Padre Celestial. La experiencia que me concedieron es REALIDAD NORMAL... ¡¡¡el entorno en el que debíamos nacer y vivir nuestras vidas!!!",
 fr_title: "Citation : RÉALITÉ NORMALE",
 fr_content: "D’autres choses se sont produites, mais ce que je désire le plus vous transmettre, c’est que les vies que nous vivons dans ce monde ne sont PAS aussi réelles que l’éternité. Nous vivons dans une sous-réalité temporaire qui est le résultat de la déconnexion de l’humanité de notre Grand et Précieux Père Céleste. L'expérience qui m'a été accordée est une RÉALITÉ NORMALE... l'environnement dans lequel nous étions censés naître et vivre notre vie !!!",
 hi_title: "उद्धरण: सामान्य-वास्तविकता",
 hi_content: "अन्य चीजें हुईं, लेकिन जो बात मैं आपको बताना चाहता हूं वह यह है कि इस दुनिया में हम जिन जीवनों का अनुभव करते हैं, वे अनंत काल की तरह वास्तविक नहीं हैं। हम एक अस्थायी उप-वास्तविकता में रहते हैं जो मानवता के हमारे महान और अनमोल स्वर्गीय पिता से अलग होने का परिणाम है। मुझे जो अनुभव दिया गया वह सामान्य वास्तविकता है... हमें जिस वातावरण में जन्म लेना था और उसमें अपना जीवन जीना था!!!",
 zh_title: "yǐn yòng ： zhèng cháng xiàn shí",
 zh_content: "qí tā shì qíng yě fā shēng le ， dàn wǒ zuì qiáng liè dì xiǎng xiàng nǐ men chuán dá de shì ， wǒ men zài zhè ge shì jiè shàng jīng lì de shēng huó bìng bù xiàng yǒng héng nà yàng zhēn shí 。 wǒ men shēng huó zài yí gè zàn shí de cì xiàn shí zhōng ， zhè shì rén lèi yǔ wǒ men wěi dà ér bǎo guì de tiān fù tuō jié de jié guǒ 。 The experience i was granted is NORMAL REALITY...the environment we were MEANT to be born into and live our lives in!!!"
tags: ["eternity", "godhead", "reality", "normal", "glory"]
ptopic: "[[topic-TRUTH]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NORMAL-REALITY",
    alias: "Quote: Normal-reality",
    parent: "topic.TRUTH",
    tags: ["eternity", "godhead", "reality", "normal", "glory"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NORMAL-REALITY",
    ctype: "QUOTE",
    en_title: "Normal-reality",
    en_content: "Other things happened, but what i most strongly desire to convey to you is that the lives we experience in this world are NOT as real as Eternity. We live in a temporary sub-reality that is the result of humanity being disconnected from our Great and Precious Heavenly Father. The experience i was granted is NORMAL REALITY...the environment we were MEANT to be born into and live our lives in!!!",
 es_title: "Cita: REALIDAD NORMAL",
 es_content: "Sucedieron otras cosas, pero lo que más deseo transmitirles es que las vidas que experimentamos en este mundo NO son tan reales como la Eternidad. Vivimos en una subrealidad temporal que es el resultado de la desconexión de la humanidad de nuestro Gran y Precioso Padre Celestial. La experiencia que me concedieron es REALIDAD NORMAL... ¡¡¡el entorno en el que debíamos nacer y vivir nuestras vidas!!!",
 fr_title: "Citation : RÉALITÉ NORMALE",
 fr_content: "D’autres choses se sont produites, mais ce que je désire le plus vous transmettre, c’est que les vies que nous vivons dans ce monde ne sont PAS aussi réelles que l’éternité. Nous vivons dans une sous-réalité temporaire qui est le résultat de la déconnexion de l’humanité de notre Grand et Précieux Père Céleste. L'expérience qui m'a été accordée est une RÉALITÉ NORMALE... l'environnement dans lequel nous étions censés naître et vivre notre vie !!!",
 hi_title: "उद्धरण: सामान्य-वास्तविकता",
 hi_content: "अन्य चीजें हुईं, लेकिन जो बात मैं आपको बताना चाहता हूं वह यह है कि इस दुनिया में हम जिन जीवनों का अनुभव करते हैं, वे अनंत काल की तरह वास्तविक नहीं हैं। हम एक अस्थायी उप-वास्तविकता में रहते हैं जो मानवता के हमारे महान और अनमोल स्वर्गीय पिता से अलग होने का परिणाम है। मुझे जो अनुभव दिया गया वह सामान्य वास्तविकता है... हमें जिस वातावरण में जन्म लेना था और उसमें अपना जीवन जीना था!!!",
 zh_title: "yǐn yòng ： zhèng cháng xiàn shí",
 zh_content: "qí tā shì qíng yě fā shēng le ， dàn wǒ zuì qiáng liè dì xiǎng xiàng nǐ men chuán dá de shì ， wǒ men zài zhè ge shì jiè shàng jīng lì de shēng huó bìng bù xiàng yǒng héng nà yàng zhēn shí 。 wǒ men shēng huó zài yí gè zàn shí de cì xiàn shí zhōng ， zhè shì rén lèi yǔ wǒ men wěi dà ér bǎo guì de tiān fù tuō jié de jié guǒ 。 The experience i was granted is NORMAL REALITY...the environment we were MEANT to be born into and live our lives in!!!"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.NORMAL-REALITY"})
MATCH (c:CONTENT {name: "content.NORMAL-REALITY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NORMAL-REALITY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:QUOTE {name: "quote.NORMAL-REALITY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.TRUTH->NORMAL-REALITY"}]->(child);

```
