---
type: QUOTE
name: "quote.SOMETHING BETTER"
alias: "Quote: Something Better"
parent: "topic.THE-GOSPEL"
en_content: "The Gospel (the REAL Gospel of Jesus Christ) offers Something exponentially better and more exciting than religion...Something so simple, so pure and so wonderful that even those who claim to believe the Gospel still wrestle with the thought that It might be too good to be true!",
 es_title: "Cita: ALGO MEJOR",
 es_content: "El Evangelio (el VERDADERO Evangelio de Jesucristo) ofrece algo exponencialmente mejor y más emocionante que la religión... Algo tan simple, tan puro y tan maravilloso que incluso aquellos que afirman creer en el Evangelio todavía luchan con la idea de que podría ser demasiado bueno para ser verdad.",
 fr_title: "Citation : QUELQUE CHOSE DE MIEUX",
 fr_content: "L'Évangile (le VRAI Évangile de Jésus-Christ) offre quelque chose de exponentiellement meilleur et plus excitant que la religion... Quelque chose de si simple, de si pur et de si merveilleux que même ceux qui prétendent croire à l'Évangile luttent encore avec la pensée que c'est peut-être trop beau pour être vrai !",
 hi_title: "उद्धरण: कुछ बेहतर",
 hi_content: "गॉस्पेल (यीशु मसीह का वास्तविक गॉस्पेल) धर्म से कहीं अधिक बेहतर और अधिक रोमांचक कुछ प्रदान करता है... कुछ इतना सरल, इतना शुद्ध और इतना अद्भुत कि जो लोग गॉस्पेल पर विश्वास करने का दावा करते हैं वे अभी भी इस विचार से जूझते हैं कि यह सच होने के लिए बहुत अच्छा हो सकता है!",
 zh_title: "yǐn yòng ： gèng hǎo de dōng xī",
 zh_content: "fú yīn （ yē sū jī dū de zhēn zhèng fú yīn ） tí gōng le bǐ zōng jiào gèng hǎo 、 gèng lìng rén xīng fèn de dōng xī …… rú cǐ jiǎn dān 、 rú cǐ chún cuì 、 rú cǐ měi miào de dōng xī ， jí shǐ shì nà xiē shēng chēng xiāng xìn fú yīn de rén réng rán huì zhēng zhá zhe rèn wéi tā kě néng hǎo dé lìng rén nán yǐ zhì xìn ！"
tags: ["superior", "religion", "gospel", "jesus_christ", "simple"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SOMETHING BETTER",
    alias: "Quote: Something Better",
    parent: "topic.THE-GOSPEL",
    tags: ["superior", "religion", "gospel", "jesus_christ", "simple"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SOMETHING BETTER",
    ctype: "QUOTE",
    en_title: "Something Better",
    en_content: "The Gospel (the REAL Gospel of Jesus Christ) offers Something exponentially better and more exciting than religion...Something so simple, so pure and so wonderful that even those who claim to believe the Gospel still wrestle with the thought that It might be too good to be true!",
 es_title: "Cita: ALGO MEJOR",
 es_content: "El Evangelio (el VERDADERO Evangelio de Jesucristo) ofrece algo exponencialmente mejor y más emocionante que la religión... Algo tan simple, tan puro y tan maravilloso que incluso aquellos que afirman creer en el Evangelio todavía luchan con la idea de que podría ser demasiado bueno para ser verdad.",
 fr_title: "Citation : QUELQUE CHOSE DE MIEUX",
 fr_content: "L'Évangile (le VRAI Évangile de Jésus-Christ) offre quelque chose de exponentiellement meilleur et plus excitant que la religion... Quelque chose de si simple, de si pur et de si merveilleux que même ceux qui prétendent croire à l'Évangile luttent encore avec la pensée que c'est peut-être trop beau pour être vrai !",
 hi_title: "उद्धरण: कुछ बेहतर",
 hi_content: "गॉस्पेल (यीशु मसीह का वास्तविक गॉस्पेल) धर्म से कहीं अधिक बेहतर और अधिक रोमांचक कुछ प्रदान करता है... कुछ इतना सरल, इतना शुद्ध और इतना अद्भुत कि जो लोग गॉस्पेल पर विश्वास करने का दावा करते हैं वे अभी भी इस विचार से जूझते हैं कि यह सच होने के लिए बहुत अच्छा हो सकता है!",
 zh_title: "yǐn yòng ： gèng hǎo de dōng xī",
 zh_content: "fú yīn （ yē sū jī dū de zhēn zhèng fú yīn ） tí gōng le bǐ zōng jiào gèng hǎo 、 gèng lìng rén xīng fèn de dōng xī …… rú cǐ jiǎn dān 、 rú cǐ chún cuì 、 rú cǐ měi miào de dōng xī ， jí shǐ shì nà xiē shēng chēng xiāng xìn fú yīn de rén réng rán huì zhēng zhá zhe rèn wéi tā kě néng hǎo dé lìng rén nán yǐ zhì xìn ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.SOMETHING BETTER"})
MATCH (c:CONTENT {name: "content.SOMETHING BETTER"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SOMETHING BETTER"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MATCH (child:QUOTE {name: "quote.SOMETHING BETTER"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->SOMETHING BETTER"}]->(child);

```
