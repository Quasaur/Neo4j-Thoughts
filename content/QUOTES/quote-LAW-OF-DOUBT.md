---
type: QUOTE
name: "quote.LAW OF DOUBT"
alias: "Quote: Law of Doubt"
parent: "topic.RELIGION"
source: "The Narrow Way"
en_content: "As stated in my book 'IMMUNITY to the Lake of Fire: a No-Nonsense Guide' religion has declared the doctrine of Full Assurance (Once Saved, Always Saved) to not only be a heresy, but an unforgivable sin (Council of Trent, Sixth Session, Chapter XVI, Canons on Justification). That is to say: Doubt itself, the sworn enemy of Faith (Matthew 14:31; James 1:5-8), is adopted by institutionalized religion as both critical and necessary. Gadzooks! What am i missing here? How can i walk with Jesus in full assurance of Faith if He can't even guarantee the completion of the Good Work our Heavenly Father began in me?"
tags: ["doubt", "faiithless", "promise", "gospel", "full_assurance"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.LAW OF DOUBT",
    alias: "Quote: Law of Doubt",
    parent: "topic.RELIGION",
    tags: ["doubt", "faiithless", "promise", "gospel", "full_assurance"],
    source: "The Narrow Way",
    booklink: "https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.LAW OF DOUBT",
    ctype: "QUOTE",
    en_title: "Quote: Law of Doubt",
    en_content: "As stated in my book 'IMMUNITY to the Lake of Fire: a No-Nonsense Guide' religion has declared the doctrine of Full Assurance (Once Saved, Always Saved) to not only be a heresy, but an unforgivable sin (Council of Trent, Sixth Session, Chapter XVI, Canons on Justification). That is to say: Doubt itself, the sworn enemy of Faith (Matthew 14:31; James 1:5-8), is adopted by institutionalized religion as both critical and necessary. Gadzooks! What am i missing here? How can i walk with Jesus in full assurance of Faith if He can't even guarantee the completion of the Good Work our Heavenly Father began in me?",
 es_title: "Cita: Ley de la duda",
 es_content: "Como se indica en mi libro 'INMUNIDAD al Lago de Fuego: una guía sensata', la religión ha declarado que la doctrina de la Plena Seguridad (Una vez salvo, siempre salvo) no sólo es una herejía, sino también un pecado imperdonable (Concilio de Trento, Sexta Sesión, Capítulo XVI, Cánones sobre la Justificación). Es decir: la duda misma, el enemigo jurado de la fe (Mateo 14:31; Santiago 1:5-8), es adoptada por la religión institucionalizada como crítica y necesaria. ¡Gadzooks! ¿Qué me falta aquí? ¿Cómo puedo caminar con Jesús en plena seguridad de Fe si Él ni siquiera puede garantizar la finalización de la Buena Obra que nuestro Padre Celestial comenzó en mí?",
 fr_title: "Citation : Loi du doute",
 fr_content: "Comme indiqué dans mon livre « IMMUNITÉ à l'étang de feu : un guide sans fioritures », la religion a déclaré que la doctrine de la pleine assurance (une fois sauvée, toujours sauvée) est non seulement une hérésie, mais aussi un péché impardonnable (Concile de Trente, sixième session, chapitre XVI, Canons sur la justification). Autrement dit : le doute lui-même, l’ennemi juré de la foi (Matthieu 14 :31 ; Jacques 1 :5-8), est adopté par la religion institutionnalisée comme à la fois critique et nécessaire. Des gadzooks ! Qu'est-ce qui me manque ici ? Comment puis-je marcher avec Jésus avec la pleine assurance de la foi s'il ne peut même pas garantir l'achèvement de la bonne œuvre que notre Père céleste a commencé en moi ?",
 hi_title: "उद्धरण: संदेह का नियम",
 hi_content: "जैसा कि मेरी पुस्तक 'इम्युनिटी टू द लेक ऑफ फायर: ए नो-नॉनसेंस गाइड' में कहा गया है, धर्म ने पूर्ण आश्वासन (एक बार बचाया, हमेशा बचाया) के सिद्धांत को न केवल एक विधर्म घोषित किया है, बल्कि एक अक्षम्य पाप भी घोषित किया है (ट्रेंट काउंसिल, छठा सत्र, अध्याय XVI, औचित्य पर सिद्धांत)। कहने का तात्पर्य यह है: संदेह, जो विश्वास का कट्टर शत्रु है (मैथ्यू 14:31; जेम्स 1:5-8), को संस्थागत धर्म द्वारा महत्वपूर्ण और आवश्यक दोनों के रूप में अपनाया जाता है। गैडज़ुक्स! मुझे यहां क्या समझ नहीं आ रहा है? मैं विश्वास के पूर्ण आश्वासन के साथ यीशु के साथ कैसे चल सकता हूँ यदि वह उस अच्छे कार्य के पूरा होने की गारंटी भी नहीं दे सकता जो हमारे स्वर्गीय पिता ने मुझमें शुरू किया था?",
 zh_title: "yǐn yòng ：huái yí fǎ zé",
 zh_content: "zhèng rú wǒ zài < huǒ hú miǎn yì : yī běn zhèng jīng zhǐ nán > yī shū zhōng suǒ shù , zōng jiào xuān chēng wán quán bǎo zhèng （ yí dàn dé jiù , yǒng yuǎn dé jiù ） de jiào yì bù jǐn shì yì duān , ér qiě shì bù kě ráo shù de zuì （ tè lún tè dà gōng huì yì , dì liù cì huì yì , dì shí liù zhāng , chēng yì xìn tiáo ）. yě jiù shì shuō : huái yí běn shēn , xìn yǎng de sǐ dí （ mǎ tài fú yīn 14:31; yǎ gè shū 1:5-8）, bèi zhì dù huà de zōng jiào shì wèi guān jiàn hé bì yào de . dāi zi ! wǒ zài zhè lǐ quē shǎo shén me ? rú guǒ yē sū shèn zhì bù néng bǎo zhèng wǒ men tiān fù zài wǒ shēn shàng kāi shǐ de shàn gōng dé yǐ wán chéng , wǒ zěn me néng huái zhe wán quán de xìn xīn yǔ yē sū tóng háng ne ?"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.LAW OF DOUBT"})
MATCH (c:CONTENT {name: "content.LAW OF DOUBT"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.LAW OF DOUBT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:QUOTE {name: "quote.LAW OF DOUBT"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->LAW OF DOUBT"}]->(child);

```
