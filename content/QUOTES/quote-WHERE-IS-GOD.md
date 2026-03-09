---
type: QUOTE
name: "quote.WHERE IS GOD?"
alias: "Quote: Where is God?"
parent: "topic.DIVINE-SOVEREIGNTY"
en_content: "GOD is the eight-billion-ton Leviathan in the room...yet you cannot see, hear, smell, taste, touch or perceive Him. Spiritists and other occult adepts with years of experience in the spirit realm seriously doubt His Existence because they've never encountered Him, though He fills all things ([Jeremiah 23:24](https://www.biblegateway.com/passage/?search=Jeremiah+23%3A24&version=ESV))...WHY is that? It is because they, like you and i, are EVIL and therefore enemies of GOD. And like you and i, they are DEAD to Him and His Transcendently HOLY Nature.",
 es_title: "Cita: ¿DÓNDE ESTÁ DIOS?",
 es_content: "DIOS es el Leviatán de ocho mil millones de toneladas en la habitación... sin embargo, no puedes verlo, oírlo, olerlo, saborearlo, tocarlo ni percibirlo. Los espiritistas y otros adeptos ocultistas con años de experiencia en el reino espiritual dudan seriamente de Su Existencia porque nunca lo han encontrado, aunque Él llena todas las cosas ([Jeremías 23:24](https://www.biblegateway.com/passage/?search=Jeremiah+23%3A24&version=ESV))...¿POR QUÉ? Es porque ellos, como tú y yo, somos MALVADOS y por lo tanto enemigos de DIOS. Y como tú y yo, están MUERTOS para Él y Su Naturaleza Trascendente y SANTA.",
 fr_title: "Citation : OÙ EST DIEU ?",
 fr_content: "DIEU est le Léviathan de huit milliards de tonnes dans la pièce... pourtant vous ne pouvez pas le voir, l'entendre, le sentir, le goûter, le toucher ou le percevoir. Les spirites et autres adeptes occultes avec des années d'expérience dans le domaine spirituel doutent sérieusement de son existence parce qu'ils ne l'ont jamais rencontré, bien qu'il remplisse toutes choses ([Jérémie 23 :24](https://www.biblegateway.com/passage/?search=Jeremiah+23%3A24&version=ESV))... POURQUOI est-ce ? C'est parce qu'eux, comme vous et moi, sont MAL et donc ennemis de DIEU. Et comme vous et moi, ils sont MORTS pour Lui et pour Sa Nature Transcendantement SAINTE.",
 hi_title: "उद्धरण: भगवान कहाँ है?",
 hi_content: "भगवान कमरे में आठ अरब टन का लेविथान है...फिर भी आप उसे देख, सुन, सूंघ, चख, स्पर्श या अनुभव नहीं कर सकते। आत्मिक क्षेत्र में वर्षों के अनुभव वाले अध्यात्मवादी और अन्य गुप्त विशेषज्ञ उसके अस्तित्व पर गंभीरता से संदेह करते हैं क्योंकि उन्होंने कभी उसका सामना नहीं किया है, हालांकि वह सभी चीजों को भरता है ([यिर्मयाह 23:24](https://www.biblegateway.com/passage/?search=Jermediah+23%3A24&version=ESV))...ऐसा क्यों है? ऐसा इसलिए है क्योंकि वे, आपकी और मेरी तरह, दुष्ट हैं और इसलिए भगवान के दुश्मन हैं। और आपकी और मेरी तरह, वे भी उसके और उसकी उत्कृष्ट पवित्र प्रकृति के प्रति मर चुके हैं।",
 zh_title: "yǐn yòng :  shàng dì zài nǎ lǐ ？",
 zh_content: "shàng dì shì fáng jiān lǐ bā shí yì dūn zhòng de lì wéi tǎn …… dàn nǐ kàn bú dào 、 tīng bú dào 、 wén bú dào 、 cháng bú dào 、 mō bú dào huò gǎn zhī bú dào tā 。 tōng líng zhě hé qí tā zài líng jiè yōng yǒu duō nián jīng yàn de shén mì zhuān jiā yán zhòng huái yí tā de cún zài ， yīn wèi tā men cóng wèi yù dào guò tā ， jǐn guǎn tā chōng mǎn le wàn wù （[ yé lì mǐ shū  23:24](https://www.biblegateway.com/passage/?search=Jeremiah+23%3A24&version=ESV)）... zhè shì wèi shén me ？ zhè shì yīn wèi tā men ， jiù xiàng nǐ wǒ yī yàng ， shì xié è de ， yīn cǐ shì shàng dì de dí rén 。 jiù xiàng nǐ wǒ yī yàng ， tā men duì tā hé tā chāo rán de shén shèng běn xìng lái shuō shì sǐ de 。"
tags: ["unperceived", "spiritual_death", "separation", "evil", "no_fellowship"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 4
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.WHERE IS GOD?",
    alias: "Quote: Where is God?",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["unperceived", "spiritual_death", "separation", "evil", "no_fellowship"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.WHERE IS GOD?",
    ctype: "QUOTE",
    en_title: "Where is God?",
    en_content: "GOD is the eight-billion-ton Leviathan in the room...yet you cannot see, hear, smell, taste, touch or perceive Him. Spiritists and other occult adepts with years of experience in the spirit realm seriously doubt His Existence because they've never encountered Him, though He fills all things ([Jeremiah 23:24](https://www.biblegateway.com/passage/?search=Jeremiah+23%3A24&version=ESV))...WHY is that? It is because they, like you and i, are EVIL and therefore enemies of GOD. And like you and i, they are DEAD to Him and His Transcendently HOLY Nature.",
 es_title: "Cita: ¿DÓNDE ESTÁ DIOS?",
 es_content: "DIOS es el Leviatán de ocho mil millones de toneladas en la habitación... sin embargo, no puedes verlo, oírlo, olerlo, saborearlo, tocarlo ni percibirlo. Los espiritistas y otros adeptos ocultistas con años de experiencia en el reino espiritual dudan seriamente de Su Existencia porque nunca lo han encontrado, aunque Él llena todas las cosas ([Jeremías 23:24](https://www.biblegateway.com/passage/?search=Jeremiah+23%3A24&version=ESV))...¿POR QUÉ? Es porque ellos, como tú y yo, somos MALVADOS y por lo tanto enemigos de DIOS. Y como tú y yo, están MUERTOS para Él y Su Naturaleza Trascendente y SANTA.",
 fr_title: "Citation : OÙ EST DIEU ?",
 fr_content: "DIEU est le Léviathan de huit milliards de tonnes dans la pièce... pourtant vous ne pouvez pas le voir, l'entendre, le sentir, le goûter, le toucher ou le percevoir. Les spirites et autres adeptes occultes avec des années d'expérience dans le domaine spirituel doutent sérieusement de son existence parce qu'ils ne l'ont jamais rencontré, bien qu'il remplisse toutes choses ([Jérémie 23 :24](https://www.biblegateway.com/passage/?search=Jeremiah+23%3A24&version=ESV))... POURQUOI est-ce ? C'est parce qu'eux, comme vous et moi, sont MAL et donc ennemis de DIEU. Et comme vous et moi, ils sont MORTS pour Lui et pour Sa Nature Transcendantement SAINTE.",
 hi_title: "उद्धरण: भगवान कहाँ है?",
 hi_content: "भगवान कमरे में आठ अरब टन का लेविथान है...फिर भी आप उसे देख, सुन, सूंघ, चख, स्पर्श या अनुभव नहीं कर सकते। आत्मिक क्षेत्र में वर्षों के अनुभव वाले अध्यात्मवादी और अन्य गुप्त विशेषज्ञ उसके अस्तित्व पर गंभीरता से संदेह करते हैं क्योंकि उन्होंने कभी उसका सामना नहीं किया है, हालांकि वह सभी चीजों को भरता है ([यिर्मयाह 23:24](https://www.biblegateway.com/passage/?search=Jermediah+23%3A24&version=ESV))...ऐसा क्यों है? ऐसा इसलिए है क्योंकि वे, आपकी और मेरी तरह, दुष्ट हैं और इसलिए भगवान के दुश्मन हैं। और आपकी और मेरी तरह, वे भी उसके और उसकी उत्कृष्ट पवित्र प्रकृति के प्रति मर चुके हैं।",
 zh_title: "yǐn yòng :  shàng dì zài nǎ lǐ ？",
 zh_content: "shàng dì shì fáng jiān lǐ bā shí yì dūn zhòng de lì wéi tǎn …… dàn nǐ kàn bú dào 、 tīng bú dào 、 wén bú dào 、 cháng bú dào 、 mō bú dào huò gǎn zhī bú dào tā 。 tōng líng zhě hé qí tā zài líng jiè yōng yǒu duō nián jīng yàn de shén mì zhuān jiā yán zhòng huái yí tā de cún zài ， yīn wèi tā men cóng wèi yù dào guò tā ， jǐn guǎn tā chōng mǎn le wàn wù （[ yé lì mǐ shū  23:24](https://www.biblegateway.com/passage/?search=Jeremiah+23%3A24&version=ESV)）... zhè shì wèi shén me ？ zhè shì yīn wèi tā men ， jiù xiàng nǐ wǒ yī yàng ， shì xié è de ， yīn cǐ shì shàng dì de dí rén 。 jiù xiàng nǐ wǒ yī yàng ， tā men duì tā hé tā chāo rán de shén shèng běn xìng lái shuō shì sǐ de 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.WHERE IS GOD?"})
MATCH (c:CONTENT {name: "content.WHERE IS GOD?"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.WHERE IS GOD?"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MATCH (child:QUOTE {name: "quote.WHERE IS GOD?"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->WHERE IS GOD?"}]->(child);

```
