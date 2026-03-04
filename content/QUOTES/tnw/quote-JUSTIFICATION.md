---
type: QUOTE
name: "quote.JUSTIFICATION"
alias: "Quote: Justification"
parent: "topic.GRACE"
en_content: "Oh My GOD! GOD is justifying the ungodly: that is, He is DECLARING THE UNGODLY LEGALLY JUST for Christ's Sake!! This has nothing to do with feelings, but WHAT YOU BELIEVE IN YOUR HEART!!! If you believe in your heart that what was done to Christ in the garden, in the Sanhedrin, before Herod, before Pilate, in the Praetorium and on the Cross was done for YOU, GOD considers you as just as Christ is EVEN THOUGH YOU ARE NOT!!!",
 es_title: "Cita: JUSTIFICACIÓN",
 es_content: "¡Ay dios mío! ¡¡DIOS está justificando a los impíos: es decir, Él está DECLARANDO A LOS IMPÍOS LEGALMENTE JUSTOS por amor de Cristo!! Esto no tiene que ver con sentimientos, sino con LO QUE CREES EN TU CORAZÓN!!! Si crees en tu corazón que lo que le fue hecho a Cristo en el huerto, en el Sanedrín, ante Herodes, ante Pilato, en el Pretorio y en la Cruz, fue hecho por TI, DIOS te considera tan justo como Cristo AUNQUE NO LO SEAS!!!",
 fr_title: "Citation : JUSTIFICATION",
 fr_content: "Oh mon Dieu! DIEU justifie les impies : c'est-à-dire qu'Il DÉCLARE LES IMPIES LÉGALEMENT JUSTE pour l'amour du Christ !! Cela n'a rien à voir avec les sentiments, mais CE QUE VOUS CROYEZ DANS VOTRE COEUR !!! Si vous croyez dans votre cœur que ce qui a été fait au Christ au jardin, au Sanhédrin, devant Hérode, devant Pilate, au Prétoire et sur la Croix a été fait pour VOUS, DIEU vous considère comme le Christ, MÊME SI VOUS NE L'ÊTES PAS !!!",
 hi_title: "उद्धरण: औचित्य",
 hi_content: "अरे बाप रे! परमेश्वर अधर्मी को न्यायोचित ठहरा रहा है: अर्थात्, वह केवल मसीह के लिए अधर्मी को कानूनी रूप से घोषित कर रहा है!! इसका भावनाओं से कोई लेना-देना नहीं है, लेकिन आप अपने दिल में क्या मानते हैं!!! यदि आप अपने दिल में विश्वास करते हैं कि बगीचे में, महासभा में, हेरोदेस से पहले, पीलातुस से पहले, प्रेटोरियम में और क्रूस पर जो मसीह के साथ किया गया था वह आपके लिए किया गया था, भगवान आपको मसीह के समान ही मानते हैं भले ही आप नहीं हैं!!!",
 zh_title: "yǐn yòng ： lǐ yóu",
 zh_content: "wǒ de tiān a ！ shén zhèng zài chēng bù jìng qián de rén wéi yì ： yě jiù shì shuō ， tā zhǐ shì wèi le jī dū de yuán gù ér xuān bù bù jìng qián de rén hé fǎ ！ zhè yǔ gǎn jué wú guān ， ér shì nǐ nèi xīn xiāng xìn shén me ！！！ rú guǒ nǐ xīn lǐ xiāng xìn ， zài huā yuán lǐ 、 zài gōng huì lǐ 、 zài xī lǜ miàn qián 、 zài bǐ lā duō miàn qián 、 zài zǒng dū fǔ lǐ hé zài shí zì jià shàng duì jī dū suǒ zuò de yī qiè dōu shì wèi nǐ zuò de ， jí shǐ nǐ bú shì ， shàng dì yě huì rèn wéi nǐ hé jī dū yī yàng ！"
tags: ["just", "legal", "grace", "jesus_christ", "adquited"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.JUSTIFICATION",
    alias: "Quote: Justification",
    parent: "topic.GRACE",
    tags: ["just", "legal", "grace", "jesus_christ", "adquited"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.JUSTIFICATION",
    ctype: "QUOTE",
    en_title: "Justification",
    en_content: "Oh My GOD! GOD is justifying the ungodly: that is, He is DECLARING THE UNGODLY LEGALLY JUST for Christ's Sake!! This has nothing to do with feelings, but WHAT YOU BELIEVE IN YOUR HEART!!! If you believe in your heart that what was done to Christ in the garden, in the Sanhedrin, before Herod, before Pilate, in the Praetorium and on the Cross was done for YOU, GOD considers you as just as Christ is EVEN THOUGH YOU ARE NOT!!!",
 es_title: "Cita: JUSTIFICACIÓN",
 es_content: "¡Ay dios mío! ¡¡DIOS está justificando a los impíos: es decir, Él está DECLARANDO A LOS IMPÍOS LEGALMENTE JUSTOS por amor de Cristo!! Esto no tiene que ver con sentimientos, sino con LO QUE CREES EN TU CORAZÓN!!! Si crees en tu corazón que lo que le fue hecho a Cristo en el huerto, en el Sanedrín, ante Herodes, ante Pilato, en el Pretorio y en la Cruz, fue hecho por TI, DIOS te considera tan justo como Cristo AUNQUE NO LO SEAS!!!",
 fr_title: "Citation : JUSTIFICATION",
 fr_content: "Oh mon Dieu! DIEU justifie les impies : c'est-à-dire qu'Il DÉCLARE LES IMPIES LÉGALEMENT JUSTE pour l'amour du Christ !! Cela n'a rien à voir avec les sentiments, mais CE QUE VOUS CROYEZ DANS VOTRE COEUR !!! Si vous croyez dans votre cœur que ce qui a été fait au Christ au jardin, au Sanhédrin, devant Hérode, devant Pilate, au Prétoire et sur la Croix a été fait pour VOUS, DIEU vous considère comme le Christ, MÊME SI VOUS NE L'ÊTES PAS !!!",
 hi_title: "उद्धरण: औचित्य",
 hi_content: "अरे बाप रे! परमेश्वर अधर्मी को न्यायोचित ठहरा रहा है: अर्थात्, वह केवल मसीह के लिए अधर्मी को कानूनी रूप से घोषित कर रहा है!! इसका भावनाओं से कोई लेना-देना नहीं है, लेकिन आप अपने दिल में क्या मानते हैं!!! यदि आप अपने दिल में विश्वास करते हैं कि बगीचे में, महासभा में, हेरोदेस से पहले, पीलातुस से पहले, प्रेटोरियम में और क्रूस पर जो मसीह के साथ किया गया था वह आपके लिए किया गया था, भगवान आपको मसीह के समान ही मानते हैं भले ही आप नहीं हैं!!!",
 zh_title: "yǐn yòng ： lǐ yóu",
 zh_content: "wǒ de tiān a ！ shén zhèng zài chēng bù jìng qián de rén wéi yì ： yě jiù shì shuō ， tā zhǐ shì wèi le jī dū de yuán gù ér xuān bù bù jìng qián de rén hé fǎ ！ zhè yǔ gǎn jué wú guān ， ér shì nǐ nèi xīn xiāng xìn shén me ！！！ rú guǒ nǐ xīn lǐ xiāng xìn ， zài huā yuán lǐ 、 zài gōng huì lǐ 、 zài xī lǜ miàn qián 、 zài bǐ lā duō miàn qián 、 zài zǒng dū fǔ lǐ hé zài shí zì jià shàng duì jī dū suǒ zuò de yī qiè dōu shì wèi nǐ zuò de ， jí shǐ nǐ bú shì ， shàng dì yě huì rèn wéi nǐ hé jī dū yī yàng ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.JUSTIFICATION"})
MATCH (c:CONTENT {name: "content.JUSTIFICATION"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.JUSTIFICATION"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.JUSTIFICATION"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->JUSTIFICATION"}]->(child);

```
