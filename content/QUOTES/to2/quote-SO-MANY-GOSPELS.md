---
type: QUOTE
name: "quote.SO MANY GOSPELS"
alias: "Quote: So Many Gospels"
parent: "topic.RELIGION"
en_content: "The fact is that there are many 'gospels' floating around in religious sects (both Catholic and Protestant, as well as non-Christian esoterics); most of them not really giving any glory to the Lordship of Jesus Christ nor agreeing with the doctrines handed down by those who were witnesses to His Holy Resurrection.",
 es_title: "Cita: TANTOS EVANGELIOS",
 es_content: "El hecho es que hay muchos 'evangelios' flotando en sectas religiosas (tanto católicas como protestantes, así como esotéricas no cristianas); la mayoría de ellos realmente no dan ninguna gloria al Señorío de Jesucristo ni están de acuerdo con las doctrinas transmitidas por aquellos que fueron testigos de Su Santa Resurrección.",
 fr_title: "Citation : TANT D'ÉVANGILES",
 fr_content: "Le fait est qu'il existe de nombreux « évangiles » qui circulent dans les sectes religieuses (à la fois catholiques et protestantes, ainsi que ésotériques non chrétiennes) ; la plupart d’entre eux ne donnent pas vraiment de gloire à la Seigneurie de Jésus-Christ et ne sont pas non plus d’accord avec les doctrines transmises par ceux qui furent témoins de sa sainte résurrection.",
 hi_title: "उद्धरण: बहुत सारे सुसमाचार",
 hi_content: "तथ्य यह है कि धार्मिक संप्रदायों (कैथोलिक और प्रोटेस्टेंट दोनों, साथ ही गैर-ईसाई गूढ़ लोगों) में कई 'सुसमाचार' तैर रहे हैं; उनमें से अधिकांश वास्तव में यीशु मसीह के प्रभुत्व की कोई महिमा नहीं कर रहे हैं और न ही उन लोगों द्वारा दिए गए सिद्धांतों से सहमत हैं जो उनके पवित्र पुनरुत्थान के गवाह थे।",
 zh_title: "yǐn yòng ： zhè me duō fú yīn shū",
 zh_content: "shì shí shàng ， zōng jiào jiào pài （ tiān zhǔ jiào hé xīn jiào ， yǐ jí fēi jī dū jiào de shēn ào jiào pài ） zhōng liú chuán zhe xǔ duō “ fú yīn ”； tā men zhōng de dà duō shù rén bìng méi yǒu zhēn zhèng róng yào yē sū jī dū de zhǔ quán ， yě bù tóng yì nà xiē jiàn zhèng tā shén shèng fù huó de rén suǒ chuán shòu de jiào yì 。"
tags: ["gospels", "False", "religion", "doctrine", "jesus_christ"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SO MANY GOSPELS",
    alias: "Quote: So Many Gospels",
    parent: "topic.RELIGION",
    tags: ["gospels", "False", "religion", "doctrine", "jesus_christ"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SO MANY GOSPELS",
    ctype: "QUOTE",
    en_title: "So Many Gospels",
    en_content: "The fact is that there are many 'gospels' floating around in religious sects (both Catholic and Protestant, as well as non-Christian esoterics); most of them not really giving any glory to the Lordship of Jesus Christ nor agreeing with the doctrines handed down by those who were witnesses to His Holy Resurrection.",
 es_title: "Cita: TANTOS EVANGELIOS",
 es_content: "El hecho es que hay muchos 'evangelios' flotando en sectas religiosas (tanto católicas como protestantes, así como esotéricas no cristianas); la mayoría de ellos realmente no dan ninguna gloria al Señorío de Jesucristo ni están de acuerdo con las doctrinas transmitidas por aquellos que fueron testigos de Su Santa Resurrección.",
 fr_title: "Citation : TANT D'ÉVANGILES",
 fr_content: "Le fait est qu'il existe de nombreux « évangiles » qui circulent dans les sectes religieuses (à la fois catholiques et protestantes, ainsi que ésotériques non chrétiennes) ; la plupart d’entre eux ne donnent pas vraiment de gloire à la Seigneurie de Jésus-Christ et ne sont pas non plus d’accord avec les doctrines transmises par ceux qui furent témoins de sa sainte résurrection.",
 hi_title: "उद्धरण: बहुत सारे सुसमाचार",
 hi_content: "तथ्य यह है कि धार्मिक संप्रदायों (कैथोलिक और प्रोटेस्टेंट दोनों, साथ ही गैर-ईसाई गूढ़ लोगों) में कई 'सुसमाचार' तैर रहे हैं; उनमें से अधिकांश वास्तव में यीशु मसीह के प्रभुत्व की कोई महिमा नहीं कर रहे हैं और न ही उन लोगों द्वारा दिए गए सिद्धांतों से सहमत हैं जो उनके पवित्र पुनरुत्थान के गवाह थे।",
 zh_title: "yǐn yòng ： zhè me duō fú yīn shū",
 zh_content: "shì shí shàng ， zōng jiào jiào pài （ tiān zhǔ jiào hé xīn jiào ， yǐ jí fēi jī dū jiào de shēn ào jiào pài ） zhōng liú chuán zhe xǔ duō “ fú yīn ”； tā men zhōng de dà duō shù rén bìng méi yǒu zhēn zhèng róng yào yē sū jī dū de zhǔ quán ， yě bù tóng yì nà xiē jiàn zhèng tā shén shèng fù huó de rén suǒ chuán shòu de jiào yì 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.SO MANY GOSPELS"})
MATCH (c:CONTENT {name: "content.SO MANY GOSPELS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SO MANY GOSPELS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:QUOTE {name: "quote.SO MANY GOSPELS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->SO MANY GOSPELS"}]->(child);

```
