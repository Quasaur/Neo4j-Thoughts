// Cypher UPDATE queries to add missing translations to PASSAGE CONTENT nodes
// Generated automatically from passage_translations.json
// Total updates: 12

// Update 1/12: passage.FAITHLESSNESS
MATCH (c:CONTENT {name: "content.FAITHLESSNESS"})
SET
    c.es_title = "FIDELIDAD",
    c.es_content = "Porque la infidelidad de los ingenuos los matará, y la complacencia de los necios los destruirá.",
    c.fr_title = "INFIDÉLITÉ",
    c.fr_content = "Car l'infidélité des naïfs les tuera, et la complaisance des insensés les détruira.",
    c.hi_title = "बेवफ़ाई",
    c.hi_content = "क्योंकि भोले-भाले लोगों की निष्ठा उन्हें मार डालेगी, और मूर्खों की शालीनता उन्हें नष्ट कर देगी।",
    c.zh_title = "bù zhōng",
    c.zh_content = "yīn wèi tiān zhēn zhě de bù xìn jiāng shā sǐ tā men ， yú zhě de zì mǎn jiāng huǐ miè tā men 。"
RETURN c.name as updated;

// Update 2/12: passage.FATE_OF_THE_WICKED
MATCH (c:CONTENT {name: "content.FATE_OF_THE_WICKED"})
SET
    c.es_title = "DESTINO DE LOS MALVADOS",
    c.es_content = "Pero los impíos serán eliminados de la tierra, y los traidores serán arrancados de ella.",
    c.fr_title = "LE SORT DES MÉCHANTS",
    c.fr_content = "Mais les méchants seront éliminés du pays, Et les perfides en seront arrachés.",
    c.hi_title = "दुष्टों का भाग्य",
    c.hi_content = "परन्तु दुष्ट लोग देश में से नाश किए जाएंगे, और विश्वासघाती उस में से नाश किए जाएंगे।",
    c.zh_title = "è rén de mìng yùn",
    c.zh_content = "dàn è rén bì cóng dì shàng bèi xiāo miè ， jiān zhà rén bì cóng dì shàng bèi bá chú 。"
RETURN c.name as updated;

// Update 3/12: passage.PROTECTION_FROM_EVIL
MATCH (c:CONTENT {name: "content.PROTECTION_FROM_EVIL"})
SET
    c.es_title = "PROTECCIÓN CONTRA EL MAL",
    c.es_content = "Porque la sabiduría entrará en tu corazón, y el conocimiento será delicia para tu alma; La discreción te guardará, el entendimiento te guardará, para librarte del camino del mal, del que habla cosas perversas;",
    c.fr_title = "PROTECTION CONTRE LE MAL",
    c.fr_content = "Car la sagesse entrera dans ton cœur, et la connaissance sera délicieuse à ton âme ; La discrétion veillera sur toi, L'intelligence te gardera, Pour te délivrer de la voie du mal, De celui qui dit des choses perverses ;",
    c.hi_title = "बुराई से सुरक्षा",
    c.hi_content = "क्योंकि बुद्धि तेरे हृदय में प्रवेश करेगी, और ज्ञान से तेरा मन प्रसन्न होगा; विवेक तेरी रक्षा करेगा, समझ तेरी रक्षा करेगी, और तुझे बुराई के मार्ग से बचाएगा, और टेढ़ी-मेढ़ी बातें बोलनेवाले से बचाएगा;",
    c.zh_title = "bǎo hù miǎn shòu xié è qīn hài",
    c.zh_content = "yīn wèi zhì huì jiāng jìn rù nǐ de nèi xīn ， zhī shí jiàng lìng nǐ de líng hún yú yuè ； míng biàn huì bǎo hù nǐ ， cōng míng huì bǎo hù nǐ ， jiù nǐ tuō lí è dào ， tuō lí shuō guāi huà de rén 。"
RETURN c.name as updated;

// Update 4/12: passage.DISCIPLINE_AND_REBUKE
MATCH (c:CONTENT {name: "content.DISCIPLINE_AND_REBUKE"})
SET
    c.es_title = "DISCIPLINA Y REPRODUCCIÓN",
    c.es_content = "Hijo mío, no rechaces la disciplina de Jehová ni detestes su reprensión; porque Jehová disciplina a quien ama.",
    c.fr_title = "DISCIPLINE ET RÉprimande",
    c.fr_content = "Mon fils, ne rejette pas la discipline de l'Éternel, et ne déteste pas ses réprimandes, car il corrige celui que l'Éternel aime.",
    c.hi_title = "अनुशासन और फटकार",
    c.hi_content = "हे मेरे पुत्र, यहोवा के अनुशासन को अस्वीकार न करना, और न उसकी घुड़की से घृणा करना, क्योंकि जिस से यहोवा प्रेम रखता है, उसी को वह ताड़ना देता है।",
    c.zh_title = "guǎn jiào yǔ chì zé",
    c.zh_content = "wǒ ér ， nǐ bù kě jù jué yē hé huá de guǎn jiào ， yě bù kě yàn wù tā de zé bèi ； yē hé huá suǒ ài de ， tā bì guǎn jiào ；"
RETURN c.name as updated;

// Update 5/12: passage.MAN_OF_VIOLENCE
MATCH (c:CONTENT {name: "content.MAN_OF_VIOLENCE"})
SET
    c.es_title = "HOMBRE DE VIOLENCIA",
    c.es_content = "No envidies a un hombre violento",
    c.fr_title = "HOMME DE VIOLENCE",
    c.fr_content = "N'enviez pas un homme violent",
    c.hi_title = "हिंसा का आदमी",
    c.hi_content = "हिंसा करने वाले व्यक्ति से ईर्ष्या न करें",
    c.zh_title = "bào lì zhī rén",
    c.zh_content = "bú yào jí dù yǒu bào lì qīng xiàng de rén"
RETURN c.name as updated;

// Update 6/12: passage.NEIGHBORS
MATCH (c:CONTENT {name: "content.NEIGHBORS"})
SET
    c.es_title = "VECINOS",
    c.es_content = "No planees el mal contra tu prójimo,",
    c.fr_title = "VOISINS",
    c.fr_content = "Ne planifie pas de mal contre ton prochain,",
    c.hi_title = "पड़ोसी",
    c.hi_content = "अपने पड़ोसी के विरुद्ध बुरी योजना न बनाओ,",
    c.zh_title = "lín jū",
    c.zh_content = "bù kě móu hài lín shè ，"
RETURN c.name as updated;

// Update 7/12: passage.OBLIGATION
MATCH (c:CONTENT {name: "content.OBLIGATION"})
SET
    c.es_title = "OBLIGACIÓN",
    c.es_content = "No niegues el bien a quien es debido,",
    c.fr_title = "OBLIGATION",
    c.fr_content = "Ne refusez pas le bien à celui à qui il est dû,",
    c.hi_title = "दायित्व",
    c.hi_content = "उन लोगों से भलाई न रोको जिनका यह हक़ है,",
    c.zh_title = "yì wù",
    c.zh_content = "bú yào jù jué xiàng nà xiē yīng dé de rén xíng shàn ，"
RETURN c.name as updated;

// Update 8/12: passage.PRIDE-AS-EVIL
MATCH (c:CONTENT {name: "content.PRIDE-AS-EVIL"})
SET
    c.es_title = "ORGULLO COMO MAL",
    c.es_content = "No seas sabio en tu propia opinión; Teme al Señor y apártate del mal. Será sanidad para tu cuerpo y refrigerio para tus huesos.",
    c.fr_title = "LA FIERTÉ COMME LE MAL",
    c.fr_content = "Ne soyez pas sage à vos propres yeux ; Craignez l'Éternel et détournez-vous du mal. Cela guérira votre corps et rafraîchira vos os.",
    c.hi_title = "अहंकार-जैसा-बुराई",
    c.hi_content = "अपनी दृष्टि में बुद्धिमान मत बनो; यहोवा का भय मानो और बुराई से दूर रहो। यह आपके शरीर को स्वस्थ करेगा और आपकी हड्डियों को ताज़गी देगा।",
    c.zh_title = "jiāo ào shì xié è de",
    c.zh_content = "bú yào zì yǐ wéi cōng míng ； jìng wèi yē hé huá ， yuǎn lí è shì 。 tā jiāng zhì yù nín de shēn tǐ bìng shuā xīn nín de gǔ gé 。"
RETURN c.name as updated;

// Update 9/12: passage.SCORNERS
MATCH (c:CONTENT {name: "content.SCORNERS"})
SET
    c.es_title = "SCORNERADORES",
    c.es_content = "Con los escarnecedores Él [Jehová] es escarnecedor,",
    c.fr_title = "Les moqueurs",
    c.fr_content = "Il [l'Éternel] se moque des moqueurs,",
    c.hi_title = "उपहास करने वाले",
    c.hi_content = "वह [प्रभु] ठट्ठा करनेवालों के प्रति तिरस्कार करता है,",
    c.zh_title = "miè shì zhě",
    c.zh_content = "tā ［ yē hé huá ］ miǎo shì xiè màn de rén ，"
RETURN c.name as updated;

// Update 10/12: passage.TRUST_THE_LORD
MATCH (c:CONTENT {name: "content.TRUST_THE_LORD"})
SET
    c.es_title = "'Pasaje: CONFÍA EN EL SEÑOR'",
    c.es_content = "Confía en Jehová con todo tu corazón y no te apoyes en tu propia prudencia. Reconócelo en todos tus caminos, y él enderezará tus veredas.",
    c.fr_title = "\"Passage : FAITES CONFIANCE AU SEIGNEUR\"",
    c.fr_content = "Confie-toi à l'Éternel de tout ton cœur, et ne t'appuie pas sur ta propre intelligence. Dans toutes vos voies, reconnaissez-le, et il aplanira vos sentiers.",
    c.hi_title = "'मार्ग: प्रभु पर भरोसा रखें'",
    c.hi_content = "पूरे दिल से यहोवा पर भरोसा रखो और अपनी समझ का सहारा मत लो। अपने सभी मार्गों में उसे स्वीकार करो, और वह तुम्हारे लिए मार्ग सीधा करेगा।",
    c.zh_title = "“ jīng wén ： xiāng xìn yē hé huá ”",
    c.zh_content = "quán xīn quán yì dì xìn lài zhǔ ， bú yào yī kào zì jǐ de lǐ jiě 。 zài nǐ yī qiè suǒ xíng de lù shàng dōu yào chéng rèn tā ， tā jiù huì zhǐ yǐn nǐ de dào lù 。"
RETURN c.name as updated;

// Update 11/12: passage.FREEDOM_OF_DEATH
MATCH (c:CONTENT {name: "content.FREEDOM_OF_DEATH"})
SET
    c.es_title = "LIBERTAD DE MUERTE",
    c.es_content = "Porque el que está muerto queda libre del pecado.",
    c.fr_title = "LIBERTÉ DE MORT",
    c.fr_content = "Car celui qui est mort est libéré du péché.",
    c.hi_title = "मृत्यु की स्वतंत्रता",
    c.hi_content = "क्योंकि जो मर गया वह पाप से मुक्त हो गया।",
    c.zh_title = "sǐ wáng zì yóu",
    c.zh_content = "yīn wèi sǐ zhě jiù tuō lí le zuì niè 。"
RETURN c.name as updated;

// Update 12/12: passage.NOT-OF-FAITH
MATCH (c:CONTENT {name: "content.NOT-OF-FAITH"})
SET
    c.es_title = "NO-DE-FE",
    c.es_content = "Pero el que duda, si come, se condena, porque no come por fe; y todo lo que no proviene de la fe es pecado.",
    c.fr_title = "NON-DE-FOI",
    c.fr_content = "Mais celui qui doute est condamné s'il mange, parce que ce n'est pas par foi qu'il mange ; et tout ce qui ne vient pas de la foi est un péché.",
    c.hi_title = "आस्था का नहीं",
    c.hi_content = "परन्तु जो सन्देह करता है, यदि वह खाता है, तो दोषी ठहराया जाता है, क्योंकि उसका खाना विश्वास से नहीं होता; और जो कुछ विश्वास से नहीं वह पाप है।",
    c.zh_title = "bù xìn yǎng",
    c.zh_content = "dàn huái yí de rén ruò chī jiù huì bèi dìng zuì ， yīn wèi tā de chī bú shì chū yú xìn xīn ； tā de chī shì chū yú xìn xīn 。 fán bù chū yú xìn xīn de dōu shì zuì 。"
RETURN c.name as updated;

// Verification: Check all PASSAGE CONTENT nodes have complete translations
MATCH (p:PASSAGE)-[:HAS_CONTENT]->(c:CONTENT)
WHERE c.es_title IS NULL OR c.es_content IS NULL OR
      c.fr_title IS NULL OR c.fr_content IS NULL OR
      c.hi_title IS NULL OR c.hi_content IS NULL OR
      c.zh_title IS NULL OR c.zh_content IS NULL
RETURN p.name as passage_name, c.name as content_name,
       c.es_title IS NULL as missing_es,
       c.fr_title IS NULL as missing_fr,
       c.hi_title IS NULL as missing_hi,
       c.zh_title IS NULL as missing_zh;
// Should return 0 rows if all translations are complete
