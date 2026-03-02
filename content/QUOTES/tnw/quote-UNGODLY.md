---
type: QUOTE
name: "quote.UNGODLY"
alias: "Quote: Quote: UNGODLY"
parent: "topic.EVIL"
en_content: "And this is what the Bible means by the term 'ungodly' ([Psalms 1:4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)): not that we deliberately choose to spend every waking moment committing atrocities, but that as much as we desire to live good, just and quiet lives, WE'D RATHER DO SO WITHOUT GOD.",
 es_title: "Cita: IMPÍO",
 es_content: "Y esto es lo que la Biblia quiere decir con el término 'impío' ([Salmos 1:4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)): no es que elegimos deliberadamente pasar cada momento de vigilia cometiendo atrocidades, sino que por mucho que deseemos vivir una vida buena, justa y tranquila, PREFERIRÍAMOS HACERLO SIN DIOS.",
 fr_title: "Citation : IMPODLY",
 fr_content: "Et c'est ce que la Bible entend par le terme « impie » ([Psaumes 1 : 4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)) : non pas que nous choisissions délibérément de passer chaque moment de notre journée à commettre des atrocités, mais que même si nous désirons vivre une vie bonne, juste et tranquille, NOUS PRÉFÉRONS LE FAIRE SANS DIEU.",
 hi_title: "उद्धरण: अधर्मी",
 hi_content: "और बाइबल में 'अधर्मी' शब्द का यही अर्थ है ([भजन 1:4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)): ऐसा नहीं है कि हम जानबूझकर हर जागृत क्षण को अत्याचार करते हुए बिताना चुनते हैं, बल्कि यह कि जितना हम अच्छा, न्यायपूर्ण और शांत जीवन जीने की इच्छा रखते हैं, हम ईश्वर के बिना ऐसा करना पसंद करते हैं।",
 zh_title: "yǐn yòng ： bù jìng qián",
 zh_content: "zhè jiù shì shèng jīng zhōng “ bù jìng qián ” yī cí de hán yì （[ shī piān  1:4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)）： bìng bú shì wǒ men gù yì xuǎn zé zài xǐng zhe de měi yī kè dōu fàn xià bào xíng ， ér shì jǐn guǎn wǒ men kě wàng guò měi hǎo 、 gōng zhèng hé ān jìng de shēng huó ， dàn wǒ men nìng yuàn zài méi yǒu shàng dì de qíng kuàng xià zhè yàng zuò 。"
tags: ["ungodly", "godless", "self_worship", "humanitarian", "damned"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.UNGODLY",
    alias: "Quote: Quote: UNGODLY",
    parent: "topic.EVIL",
    tags: ["ungodly", "godless", "self_worship", "humanitarian", "damned"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.UNGODLY",
    ctype: "QUOTE",
    en_title: "Quote: UNGODLY",
    en_content: "And this is what the Bible means by the term 'ungodly' ([Psalms 1:4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)): not that we deliberately choose to spend every waking moment committing atrocities, but that as much as we desire to live good, just and quiet lives, WE'D RATHER DO SO WITHOUT GOD.",
 es_title: "Cita: IMPÍO",
 es_content: "Y esto es lo que la Biblia quiere decir con el término 'impío' ([Salmos 1:4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)): no es que elegimos deliberadamente pasar cada momento de vigilia cometiendo atrocidades, sino que por mucho que deseemos vivir una vida buena, justa y tranquila, PREFERIRÍAMOS HACERLO SIN DIOS.",
 fr_title: "Citation : IMPODLY",
 fr_content: "Et c'est ce que la Bible entend par le terme « impie » ([Psaumes 1 : 4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)) : non pas que nous choisissions délibérément de passer chaque moment de notre journée à commettre des atrocités, mais que même si nous désirons vivre une vie bonne, juste et tranquille, NOUS PRÉFÉRONS LE FAIRE SANS DIEU.",
 hi_title: "उद्धरण: अधर्मी",
 hi_content: "और बाइबल में 'अधर्मी' शब्द का यही अर्थ है ([भजन 1:4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)): ऐसा नहीं है कि हम जानबूझकर हर जागृत क्षण को अत्याचार करते हुए बिताना चुनते हैं, बल्कि यह कि जितना हम अच्छा, न्यायपूर्ण और शांत जीवन जीने की इच्छा रखते हैं, हम ईश्वर के बिना ऐसा करना पसंद करते हैं।",
 zh_title: "yǐn yòng ： bù jìng qián",
 zh_content: "zhè jiù shì shèng jīng zhōng “ bù jìng qián ” yī cí de hán yì （[ shī piān  1:4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)）： bìng bú shì wǒ men gù yì xuǎn zé zài xǐng zhe de měi yī kè dōu fàn xià bào xíng ， ér shì jǐn guǎn wǒ men kě wàng guò měi hǎo 、 gōng zhèng hé ān jìng de shēng huó ， dàn wǒ men nìng yuàn zài méi yǒu shàng dì de qíng kuàng xià zhè yàng zuò 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.UNGODLY"})
MATCH (c:CONTENT {name: "content.UNGODLY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.UNGODLY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:QUOTE {name: "quote.UNGODLY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->UNGODLY"}]->(child);

```
