---
type: QUOTE
name: "quote.ETERNAL DAMNATION"
alias: "Quote: Eternal Damnation"
parent: "topic.APOCALYPSE"
source: "'The Narrow Way'"
en_content: "Likewise, those who participate in the Second Resurrection will come forth completely intact: spirit, soul and body with no parts or organs missing. There is a reason the word 'resurrection' must be defined this way... Look carefully at the [Twentieth Chapter of Revelation](https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV). After all of the Damned are resurrected Death and Hades (the place of disembodied souls) are themselves cast into the Lake of Fire and Sulfur! The implication is horrifyingly obvious: if Death no longer exists, then no matter what damage is done to you by the Fire and Sulfur, you can never die! There is no relief and there is no reprieve.",
 es_title: "Cita: CONDENACIÓN ETERNA",
 es_content: "Asimismo, quienes participen en la Segunda Resurrección saldrán completamente intactos: espíritu, alma y cuerpo, sin que les falte ninguna parte ni órgano. Hay una razón por la que la palabra 'resurrección' debe definirse de esta manera... Mire cuidadosamente el [Capítulo Vigésimo de Apocalipsis](https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV). Después de que todos los Condenados resuciten, ¡la Muerte y el Hades (el lugar de las almas incorpóreas) son arrojados al Lago de Fuego y Azufre! La implicación es terriblemente obvia: si la Muerte ya no existe, entonces no importa el daño que te hagan el Fuego y el Azufre, ¡nunca podrás morir! No hay alivio ni respiro.",
 fr_title: "Citation : DAMNATION ÉTERNELLE",
 fr_content: "De même, ceux qui participent à la Deuxième Résurrection en ressortiront complètement intacts : esprit, âme et corps sans aucune partie ni organe manquant. Il y a une raison pour laquelle le mot « résurrection » doit être défini de cette façon... Regardez attentivement le [Vingtième chapitre de l'Apocalypse](https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV). Après que tous les Damnés soient ressuscités, la Mort et Hadès (le lieu des âmes désincarnées) sont eux-mêmes jetés dans le Lac de Feu et de Soufre ! L'implication est horriblement évidente : si la Mort n'existe plus, alors quels que soient les dégâts que vous infligent le Feu et le Soufre, vous ne pourrez jamais mourir ! Il n’y a ni soulagement ni répit.",
 hi_title: "उद्धरण: शाश्वत अभिशाप",
 hi_content: "इसी तरह, जो लोग दूसरे पुनरुत्थान में भाग लेते हैं वे पूरी तरह से अक्षुण्ण होकर सामने आएंगे: आत्मा, प्राण और शरीर, जिनका कोई अंग या अंग गायब नहीं होगा। एक कारण है कि 'पुनरुत्थान' शब्द को इस तरह से परिभाषित किया जाना चाहिए... [रहस्योद्घाटन के बीसवें अध्याय] (https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV) को ध्यान से देखें। सभी शापितों के पुनर्जीवित होने के बाद मृत्यु और पाताल (अशरीरी आत्माओं का स्थान) स्वयं आग और सल्फर की झील में डाल दिए जाते हैं! निहितार्थ भयावह रूप से स्पष्ट है: यदि मृत्यु अब अस्तित्व में नहीं है, तो चाहे आग और सल्फर से आपको कितना भी नुकसान हो, आप कभी नहीं मर सकते! न कोई राहत है और न कोई राहत।",
 zh_title: "yǐn yòng ： yǒng héng de zǔ zhòu",
 zh_content: "tóng yàng ， nà xiē cān jiā dì èr cì fù huó de rén jiāng wán hǎo wú sǔn dì chū lái ： jīng shén 、 líng hún hé shēn tǐ ， méi yǒu rèn hé bù fèn huò qì guān quē shī 。 “ fù huó ” zhè ge cí bì xū zhè yàng dìng yì shì yǒu yuán yīn de …… zǐ xì kàn kàn [ qǐ shì lù dì èr shí zhāng ](https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV)。 suǒ yǒu bèi zǔ zhòu de rén dōu fù huó hòu ， sǐ wáng hé dì yù （ líng hún de dì fāng ） běn shēn jiù bèi rēng jìn le huǒ hé liú huáng hú lǐ ！ qí hán yì fēi cháng míng xiǎn ： rú guǒ sǐ wáng bù zài cún zài ， nà me wú lùn huǒ hé liú huáng duì nǐ zào chéng shén me shāng hài ， nǐ dōu yǒng yuǎn bú huì sǐ ！ méi yǒu rèn hé huǎn jiě ， yě méi yǒu rèn hé huǎn xíng 。"
tags: ["lake_of_fire", "sulfur", "wrath", "torment", "breathless"]
ptopic: "[[topic-APOCALYPSE]]"
level: 5
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ETERNAL DAMNATION",
    alias: "Quote: Eternal Damnation",
    parent: "topic.APOCALYPSE",
    tags: ["lake_of_fire", "sulfur", "wrath", "torment", "breathless"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ETERNAL DAMNATION",
    ctype: "QUOTE",
    en_title: "Eternal Damnation",
    en_content: "Likewise, those who participate in the Second Resurrection will come forth completely intact: spirit, soul and body with no parts or organs missing. There is a reason the word 'resurrection' must be defined this way... Look carefully at the [Twentieth Chapter of Revelation](https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV). After all of the Damned are resurrected Death and Hades (the place of disembodied souls) are themselves cast into the Lake of Fire and Sulfur! The implication is horrifyingly obvious: if Death no longer exists, then no matter what damage is done to you by the Fire and Sulfur, you can never die! There is no relief and there is no reprieve.",
 es_title: "Cita: CONDENACIÓN ETERNA",
 es_content: "Asimismo, quienes participen en la Segunda Resurrección saldrán completamente intactos: espíritu, alma y cuerpo, sin que les falte ninguna parte ni órgano. Hay una razón por la que la palabra 'resurrección' debe definirse de esta manera... Mire cuidadosamente el [Capítulo Vigésimo de Apocalipsis](https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV). Después de que todos los Condenados resuciten, ¡la Muerte y el Hades (el lugar de las almas incorpóreas) son arrojados al Lago de Fuego y Azufre! La implicación es terriblemente obvia: si la Muerte ya no existe, entonces no importa el daño que te hagan el Fuego y el Azufre, ¡nunca podrás morir! No hay alivio ni respiro.",
 fr_title: "Citation : DAMNATION ÉTERNELLE",
 fr_content: "De même, ceux qui participent à la Deuxième Résurrection en ressortiront complètement intacts : esprit, âme et corps sans aucune partie ni organe manquant. Il y a une raison pour laquelle le mot « résurrection » doit être défini de cette façon... Regardez attentivement le [Vingtième chapitre de l'Apocalypse](https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV). Après que tous les Damnés soient ressuscités, la Mort et Hadès (le lieu des âmes désincarnées) sont eux-mêmes jetés dans le Lac de Feu et de Soufre ! L'implication est horriblement évidente : si la Mort n'existe plus, alors quels que soient les dégâts que vous infligent le Feu et le Soufre, vous ne pourrez jamais mourir ! Il n’y a ni soulagement ni répit.",
 hi_title: "उद्धरण: शाश्वत अभिशाप",
 hi_content: "इसी तरह, जो लोग दूसरे पुनरुत्थान में भाग लेते हैं वे पूरी तरह से अक्षुण्ण होकर सामने आएंगे: आत्मा, प्राण और शरीर, जिनका कोई अंग या अंग गायब नहीं होगा। एक कारण है कि 'पुनरुत्थान' शब्द को इस तरह से परिभाषित किया जाना चाहिए... [रहस्योद्घाटन के बीसवें अध्याय] (https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV) को ध्यान से देखें। सभी शापितों के पुनर्जीवित होने के बाद मृत्यु और पाताल (अशरीरी आत्माओं का स्थान) स्वयं आग और सल्फर की झील में डाल दिए जाते हैं! निहितार्थ भयावह रूप से स्पष्ट है: यदि मृत्यु अब अस्तित्व में नहीं है, तो चाहे आग और सल्फर से आपको कितना भी नुकसान हो, आप कभी नहीं मर सकते! न कोई राहत है और न कोई राहत।",
 zh_title: "yǐn yòng ： yǒng héng de zǔ zhòu",
 zh_content: "tóng yàng ， nà xiē cān jiā dì èr cì fù huó de rén jiāng wán hǎo wú sǔn dì chū lái ： jīng shén 、 líng hún hé shēn tǐ ， méi yǒu rèn hé bù fèn huò qì guān quē shī 。 “ fù huó ” zhè ge cí bì xū zhè yàng dìng yì shì yǒu yuán yīn de …… zǐ xì kàn kàn [ qǐ shì lù dì èr shí zhāng ](https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV)。 suǒ yǒu bèi zǔ zhòu de rén dōu fù huó hòu ， sǐ wáng hé dì yù （ líng hún de dì fāng ） běn shēn jiù bèi rēng jìn le huǒ hé liú huáng hú lǐ ！ qí hán yì fēi cháng míng xiǎn ： rú guǒ sǐ wáng bù zài cún zài ， nà me wú lùn huǒ hé liú huáng duì nǐ zào chéng shén me shāng hài ， nǐ dōu yǒng yuǎn bú huì sǐ ！ méi yǒu rèn hé huǎn jiě ， yě méi yǒu rèn hé huǎn xíng 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.ETERNAL DAMNATION"})
MATCH (c:CONTENT {name: "content.ETERNAL DAMNATION"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ETERNAL DAMNATION"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.APOCALYPSE"})
MATCH (child:QUOTE {name: "quote.ETERNAL DAMNATION"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.APOCALYPSE->ETERNAL DAMNATION"}]->(child);

```
