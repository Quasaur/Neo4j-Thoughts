---
type: QUOTE
name: "quote.WRONG REASON"
alias: "Quote: Wrong Reason"
parent: "topic.ATTITUDE"
en_content: "IT IS POSSIBLE TO PERFORM A GOOD DEED FOR THE WRONG REASON (Luke 18:9-14). Is there anything wrong with fasting or tithing? No; BUT the Pharisee's bad ATTITUDE turned his good deeds into iniquity!"
tags: ["deed", "reason", "attitude", "parable", "prayer"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.WRONG REASON",
    alias: "Quote: Wrong Reason",
    parent: "topic.ATTITUDE",
    tags: ["deed", "reason", "attitude", "parable", "prayer"],
    source: "'The Basics and More: A Year's Sermons'",
    booklink: "(https://www.amazon.com/Basics-More-Years-Sermons-ebook/dp/B00XLMBDR8)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.WRONG REASON",
    ctype: "QUOTE",
    en_title: "Wrong Reason",
    en_content: "IT IS POSSIBLE TO PERFORM A GOOD DEED FOR THE WRONG REASON (Luke 18:9-14). Is there anything wrong with fasting or tithing? No; BUT the Pharisee's bad ATTITUDE turned his good deeds into iniquity!",
 es_title: "Cita: RAZÓN EQUIVOCADA",
 es_content: "ES POSIBLE REALIZAR UNA BUENA OBRA POR LA RAZÓN EQUIVOCADA (Lucas 18:9-14). ¿Hay algo malo en ayunar o diezmar? No; ¡PERO la mala ACTITUD del fariseo convirtió sus buenas obras en iniquidad!",
 fr_title: "Citation : MAUVAISE RAISON",
 fr_content: "IL EST POSSIBLE DE FAIRE UNE BONNE ACTION POUR UNE MAUVAISE RAISON (Luc 18 :9-14). Y a-t-il quelque chose de mal à jeûner ou à donner la dîme ? Non; MAIS la mauvaise ATTITUDE du pharisien a transformé ses bonnes actions en iniquité !",
 hi_title: "उद्धरण: गलत कारण",
 hi_content: "गलत कारण से अच्छा कार्य करना संभव है (लूका 18:9-14)। क्या उपवास या दशमांश देने में कोई बुराई है? नहीं; परन्तु फरीसी के बुरे व्यवहार ने उसके भले कामों को अधर्म में बदल दिया!",
 zh_title: "yǐn yòng ： cuò wù de lǐ yóu",
 zh_content: "chū yú cuò wù de yuán yīn xíng shàn shì yǒu kě néng de （ lù jiā fú yīn  18:9-14）。 jìn shí huò shén yī fèng xiàn yǒu shén me wèn tí ma ？ bù ; dàn fǎ lì sài rén de huài tài dù bǎ tā de shàn xíng biàn chéng le zuì niè ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.WRONG REASON"})
MATCH (c:CONTENT {name: "content.WRONG REASON"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.WRONG REASON"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MATCH (child:QUOTE {name: "quote.WRONG REASON"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.ATTITUDE->WRONG REASON"}]->(child);

```
