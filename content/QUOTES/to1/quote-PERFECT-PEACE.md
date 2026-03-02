---
type: QUOTE
name: "quote.PERFECT_PEACE"
alias: "Quote: Quote: PERFECT PEACE"
parent: "topic.GRACE"
en_content: "Every cell in my body relaxed in Perfect Peace. Every fear was vanquished. And that's why my body collapsed like a rag doll to the floor on that stage in front of all those people.",
 es_title: "Cita: PAZ PERFECTA",
 es_content: "Cada célula de mi cuerpo se relajó en Perfecta Paz. Todo temor fue vencido. Y es por eso que mi cuerpo se desplomó como un muñeco de trapo en el suelo en ese escenario frente a toda esa gente.",
 fr_title: "Citation : PAIX PARFAITE",
 fr_content: "Chaque cellule de mon corps s'est détendue dans une paix parfaite. Chaque peur a été vaincue. Et c'est pour ça que mon corps s'est effondré comme une poupée de chiffon sur le sol sur scène devant tous ces gens.",
 hi_title: "उद्धरण: पूर्ण शांति",
 hi_content: "मेरे शरीर की प्रत्येक कोशिका पूर्ण शांति में शिथिल हो गई। हर डर ख़त्म हो गया. और तभी मेरा शरीर उन सभी लोगों के सामने उस मंच पर एक चिथड़े की गुड़िया की तरह फर्श पर गिर गया।",
 zh_title: "yǐn yòng ： wán měi de hé píng",
 zh_content: "wǒ shēn tǐ de měi yí gè xì bāo dōu zài wán měi de píng jìng zhōng fàng sōng 。 suǒ yǒu de kǒng jù dōu bèi zhēng fú le 。 zhè jiù shì wèi shén me wǒ de shēn tǐ xiàng bù wá wá yī yàng dào zài wǔ tái shàng suǒ yǒu guān zhòng miàn qián de dì bǎn shàng 。"
tags: ["peace", "perfect", "grace", "holiness", "love"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.PERFECT_PEACE",
    alias: "Quote: Quote: PERFECT PEACE",
    parent: "topic.GRACE",
    tags: ["peace", "perfect", "grace", "holiness", "love"],
    source: "'The Traveler's Oasis, Book One'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-One-ebook/dp/B00Y43B2OC)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PERFECT_PEACE",
    ctype: "QUOTE",
    en_title: "Quote: PERFECT PEACE",
    en_content: "Every cell in my body relaxed in Perfect Peace. Every fear was vanquished. And that's why my body collapsed like a rag doll to the floor on that stage in front of all those people.",
 es_title: "Cita: PAZ PERFECTA",
 es_content: "Cada célula de mi cuerpo se relajó en Perfecta Paz. Todo temor fue vencido. Y es por eso que mi cuerpo se desplomó como un muñeco de trapo en el suelo en ese escenario frente a toda esa gente.",
 fr_title: "Citation : PAIX PARFAITE",
 fr_content: "Chaque cellule de mon corps s'est détendue dans une paix parfaite. Chaque peur a été vaincue. Et c'est pour ça que mon corps s'est effondré comme une poupée de chiffon sur le sol sur scène devant tous ces gens.",
 hi_title: "उद्धरण: पूर्ण शांति",
 hi_content: "मेरे शरीर की प्रत्येक कोशिका पूर्ण शांति में शिथिल हो गई। हर डर ख़त्म हो गया. और तभी मेरा शरीर उन सभी लोगों के सामने उस मंच पर एक चिथड़े की गुड़िया की तरह फर्श पर गिर गया।",
 zh_title: "yǐn yòng ： wán měi de hé píng",
 zh_content: "wǒ shēn tǐ de měi yí gè xì bāo dōu zài wán měi de píng jìng zhōng fàng sōng 。 suǒ yǒu de kǒng jù dōu bèi zhēng fú le 。 zhè jiù shì wèi shén me wǒ de shēn tǐ xiàng bù wá wá yī yàng dào zài wǔ tái shàng suǒ yǒu guān zhòng miàn qián de dì bǎn shàng 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.PERFECT_PEACE"})
MATCH (c:CONTENT {name: "content.PERFECT_PEACE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.PERFECT_PEACE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.PERFECT_PEACE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->PERFECT_PEACE"}]->(child);

```
