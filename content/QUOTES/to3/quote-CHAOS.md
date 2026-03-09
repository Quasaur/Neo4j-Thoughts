---
type: QUOTE
name: "quote.CHAOS"
alias: "Quote: Chaos"
parent: "topic.PSYCHOLOGY"
en_content: "We fear Chaos above little else and, consciously or subconsciously, are constantly trying to create order where there may actually be none.",
 es_title: "Cita: CAOS",
 es_content: "Tememos al Caos por encima de cualquier otra cosa y, consciente o inconscientemente, intentamos constantemente crear orden donde en realidad no lo hay.",
 fr_title: "Citation : CHAOS",
 fr_content: "Nous craignons le chaos par-dessus tout et, consciemment ou inconsciemment, essayons constamment de créer de l’ordre là où il n’y en a peut-être pas.",
 hi_title: "उद्धरण: अराजकता",
 hi_content: "हम किसी भी चीज से ऊपर अराजकता से डरते हैं और, सचेत रूप से या अवचेतन रूप से, लगातार ऐसी व्यवस्था बनाने की कोशिश कर रहे हैं जहां वास्तव में कुछ भी नहीं हो सकता है।",
 zh_title: "yǐn yòng ： hùn luàn",
 zh_content: "wǒ men zuì hài pà de shì hùn luàn ， bìng qiě yǒu yì shí huò wú yì shí dì bù duàn cháng shì zài shí jì shàng méi yǒu zhì xù de dì fāng chuàng zào zhì xù 。"
tags: ["chaos", "disorder", "fear", "perception", "delusion"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHAOS",
    alias: "Quote: Chaos",
    parent: "topic.PSYCHOLOGY",
    tags: ["chaos", "disorder", "fear", "perception", "delusion"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHAOS",
    ctype: "QUOTE",
    en_title: "Chaos",
    en_content: "We fear Chaos above little else and, consciously or subconsciously, are constantly trying to create order where there may actually be none.",
 es_title: "Cita: CAOS",
 es_content: "Tememos al Caos por encima de cualquier otra cosa y, consciente o inconscientemente, intentamos constantemente crear orden donde en realidad no lo hay.",
 fr_title: "Citation : CHAOS",
 fr_content: "Nous craignons le chaos par-dessus tout et, consciemment ou inconsciemment, essayons constamment de créer de l’ordre là où il n’y en a peut-être pas.",
 hi_title: "उद्धरण: अराजकता",
 hi_content: "हम किसी भी चीज से ऊपर अराजकता से डरते हैं और, सचेत रूप से या अवचेतन रूप से, लगातार ऐसी व्यवस्था बनाने की कोशिश कर रहे हैं जहां वास्तव में कुछ भी नहीं हो सकता है।",
 zh_title: "yǐn yòng ： hùn luàn",
 zh_content: "wǒ men zuì hài pà de shì hùn luàn ， bìng qiě yǒu yì shí huò wú yì shí dì bù duàn cháng shì zài shí jì shàng méi yǒu zhì xù de dì fāng chuàng zào zhì xù 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.CHAOS"})
MATCH (c:CONTENT {name: "content.CHAOS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHAOS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MATCH (child:QUOTE {name: "quote.CHAOS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.PSYCHOLOGY->CHAOS"}]->(child);

```
