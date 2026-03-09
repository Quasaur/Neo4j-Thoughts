---
type: QUOTE
name: "quote.CHILD OF SATAN"
alias: "Quote: Child of Satan"
parent: "topic.EVIL"
source: "'The Narrow Way'"
en_content: "It is impossible to be a sinner and not harbor in your heart some lie that you cling to as truth. Do you even now yet see yourself as a 'good person' who could 'benefit' from having an 'advisor' such as Jesus at your side? Or are you willing to admit that you're a child of the Devil, by your very nature damned for Wrath and in DESPERATE NEED of the Only-Begotten Son of GOD's Mercy, Forgiveness and Saving Grace?"
 es_title: "Cita: HIJO DE SATANÁS"
 es_content: "Es imposible ser pecador y no albergar en tu corazón alguna mentira a la que te aferras como verdad. ¿Se ve todavía ahora como una \"buena persona\" que podría \"beneficiarse\" de tener a su lado un \"consejero\" como Jesús? ¿O estás dispuesto a admitir que eres un hijo del Diablo, por tu propia naturaleza condenado por la ira y con una NECESIDAD DESESPERADA del Hijo Unigénito de la Misericordia, el Perdón y la Gracia Salvadora de DIOS?"
 fr_title: "Citation : ENFANT DE SATAN"
 fr_content: "Il est impossible d’être pécheur et de ne pas abriter dans son cœur un mensonge auquel on s’accroche comme étant la vérité. Vous considérez-vous encore maintenant comme une « bonne personne » qui pourrait « bénéficier » d’avoir un « conseiller » tel que Jésus à vos côtés ? Ou êtes-vous prêt à admettre que vous êtes un enfant du Diable, par nature damné par la colère et dans un BESOIN DÉSPÉRÉ de la miséricorde, du pardon et de la grâce salvatrice du Fils unique de DIEU ?"
 hi_title: "उद्धरण: शैतान की संतान"
 hi_content: "यह असंभव है कि आप पापी हों और अपने हृदय में कोई ऐसा झूठ न पालें जिसे आप सत्य मानकर चिपके रहें। क्या आप अब भी स्वयं को एक 'अच्छे व्यक्ति' के रूप में देखते हैं जो आपके साथ यीशु जैसे 'सलाहकार' होने से 'लाभ' प्राप्त कर सकता है? या क्या आप यह स्वीकार करने को तैयार हैं कि आप शैतान की संतान हैं, अपने स्वभाव से ही क्रोध के लिए अभिशप्त हैं और आपको भगवान की दया, क्षमा और बचाने वाले अनुग्रह के एकलौते पुत्र की सख्त जरूरत है?"
 zh_title: "yǐn yòng ： sā dàn zhī zi"
 zh_content: "zuò wéi yí gè zuì rén ， nǐ bù kě néng bù zài xīn lǐ cáng zhe yī xiē nǐ jiān chí rèn wéi zhēn lǐ de huǎng yán 。 nǐ xiàn zài shì fǒu hái rèn wéi zì jǐ shì yí gè “ hǎo rén ”， kě yǐ cóng xiàng yē sū zhè yàng de “ gù wèn ” zài nǐ shēn biān “ shòu yì ”？ huò zhě nǐ yuàn yì chéng rèn nǐ shì mó guǐ de hái zi ， nǐ de běn xìng yīn fèn nù ér shòu dào zǔ zhòu ， bìng qiě pò qiè xū yào shàng dì dú shēng zi de lián mǐn 、 kuān shù hé zhěng jiù ēn diǎn ？"
tags: ["evil", "wicked", "reprobate", "hopeless", "jesus_christ"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHILD OF SATAN",
    alias: "Quote: Child of Satan",
    parent: "topic.EVIL",
    tags: ["evil", "wicked", "reprobate", "hopeless", "jesus_christ"],
    source: "'The Narrow Way'",
    booklink: "()",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHILD OF SATAN",
    ctype: "QUOTE",
    en_title: "Child of Satan",
    en_content: "It is impossible to be a sinner and not harbor in your heart some lie that you cling to as truth. Do you even now yet see yourself as a 'good person' who could 'benefit' from having an 'advisor' such as Jesus at your side? Or are you willing to admit that you're a child of the Devil, by your very nature damned for Wrath and in DESPERATE NEED of the Only-Begotten Son of GOD's Mercy, Forgiveness and Saving Grace?",
 es_title: "Cita: HIJO DE SATANÁS",
 es_content: "Es imposible ser pecador y no albergar en tu corazón alguna mentira a la que te aferras como verdad. ¿Se ve todavía ahora como una \"buena persona\" que podría \"beneficiarse\" de tener a su lado un \"consejero\" como Jesús? ¿O estás dispuesto a admitir que eres un hijo del Diablo, por tu propia naturaleza condenado por la ira y con una NECESIDAD DESESPERADA del Hijo Unigénito de la Misericordia, el Perdón y la Gracia Salvadora de DIOS?",
 fr_title: "Citation : ENFANT DE SATAN",
 fr_content: "Il est impossible d’être pécheur et de ne pas abriter dans son cœur un mensonge auquel on s’accroche comme étant la vérité. Vous considérez-vous encore maintenant comme une « bonne personne » qui pourrait « bénéficier » d’avoir un « conseiller » tel que Jésus à vos côtés ? Ou êtes-vous prêt à admettre que vous êtes un enfant du Diable, par nature damné par la colère et dans un BESOIN DÉSPÉRÉ de la miséricorde, du pardon et de la grâce salvatrice du Fils unique de DIEU ?",
 hi_title: "उद्धरण: शैतान की संतान",
 hi_content: "यह असंभव है कि आप पापी हों और अपने हृदय में कोई ऐसा झूठ न पालें जिसे आप सत्य मानकर चिपके रहें। क्या आप अब भी स्वयं को एक 'अच्छे व्यक्ति' के रूप में देखते हैं जो आपके साथ यीशु जैसे 'सलाहकार' होने से 'लाभ' प्राप्त कर सकता है? या क्या आप यह स्वीकार करने को तैयार हैं कि आप शैतान की संतान हैं, अपने स्वभाव से ही क्रोध के लिए अभिशप्त हैं और आपको भगवान की दया, क्षमा और बचाने वाले अनुग्रह के एकलौते पुत्र की सख्त जरूरत है?",
 zh_title: "yǐn yòng ： sā dàn zhī zi",
 zh_content: "zuò wéi yí gè zuì rén ， nǐ bù kě néng bù zài xīn lǐ cáng zhe yī xiē nǐ jiān chí rèn wéi zhēn lǐ de huǎng yán 。 nǐ xiàn zài shì fǒu hái rèn wéi zì jǐ shì yí gè “ hǎo rén ”， kě yǐ cóng xiàng yē sū zhè yàng de “ gù wèn ” zài nǐ shēn biān “ shòu yì ”？ huò zhě nǐ yuàn yì chéng rèn nǐ shì mó guǐ de hái zi ， nǐ de běn xìng yīn fèn nù ér shòu dào zǔ zhòu ， bìng qiě pò qiè xū yào shàng dì dú shēng zi de lián mǐn 、 kuān shù hé zhěng jiù ēn diǎn ？"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.CHILD OF SATAN"})
MATCH (c:CONTENT {name: "content.CHILD OF SATAN"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHILD OF SATAN"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:QUOTE {name: "quote.CHILD OF SATAN"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->CHILD OF SATAN"}]->(child);
```