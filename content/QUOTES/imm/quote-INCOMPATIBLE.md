---
type: QUOTE
name: "quote.INCOMPATIBLE"
alias: "Quote: Quote: INCOMPATIBLE"
parent: "topic.SPIRITUALITY"
en_content: "The life you were born into as a human is ABSOLUTELY INCOMPATIBLE with the Life you were born-again into as a Child of GOD.",
 es_title: "Cita: INCOMPATIBLE",
 es_content: "La vida en la que naciste como ser humano es ABSOLUTAMENTE INCOMPATIBLE con la vida en la que naciste de nuevo como Hijo de DIOS.",
 fr_title: "Citation : INCOMPATIBLE",
 fr_content: "La vie dans laquelle vous êtes né en tant qu’humain est ABSOLUMENT INCOMPATIBLE avec la vie dans laquelle vous êtes né de nouveau en tant qu’enfant de DIEU.",
 hi_title: "उद्धरण: असंगत",
 hi_content: "जिस जीवन में आप एक इंसान के रूप में पैदा हुए थे, वह उस जीवन के साथ बिल्कुल असंगत है जिसमें आप फिर से भगवान के बच्चे के रूप में पैदा हुए थे।",
 zh_title: "yǐn yòng ： bù jiān róng",
 zh_content: "nǐ zuò wéi rén lèi ér dàn shēng de shēng huó yǔ nǐ zuò wéi shàng dì zhī zi ér chóng shēng de shēng huó jué duì bù xiāng róng 。"
tags: ["flesh", "spirit", "holy_spirit", "god", "adoption"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.INCOMPATIBLE",
    alias: "Quote: Quote: INCOMPATIBLE",
    parent: "topic.SPIRITUALITY",
    tags: ["flesh", "spirit", "holy_spirit", "god", "adoption"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.INCOMPATIBLE",
    ctype: "QUOTE",
    en_title: "Quote: INCOMPATIBLE",
    en_content: "The life you were born into as a human is ABSOLUTELY INCOMPATIBLE with the Life you were born-again into as a Child of GOD.",
 es_title: "Cita: INCOMPATIBLE",
 es_content: "La vida en la que naciste como ser humano es ABSOLUTAMENTE INCOMPATIBLE con la vida en la que naciste de nuevo como Hijo de DIOS.",
 fr_title: "Citation : INCOMPATIBLE",
 fr_content: "La vie dans laquelle vous êtes né en tant qu’humain est ABSOLUMENT INCOMPATIBLE avec la vie dans laquelle vous êtes né de nouveau en tant qu’enfant de DIEU.",
 hi_title: "उद्धरण: असंगत",
 hi_content: "जिस जीवन में आप एक इंसान के रूप में पैदा हुए थे, वह उस जीवन के साथ बिल्कुल असंगत है जिसमें आप फिर से भगवान के बच्चे के रूप में पैदा हुए थे।",
 zh_title: "yǐn yòng ： bù jiān róng",
 zh_content: "nǐ zuò wéi rén lèi ér dàn shēng de shēng huó yǔ nǐ zuò wéi shàng dì zhī zi ér chóng shēng de shēng huó jué duì bù xiāng róng 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.INCOMPATIBLE"})
MATCH (c:CONTENT {name: "content.INCOMPATIBLE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.INCOMPATIBLE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:QUOTE {name: "quote.INCOMPATIBLE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.SPIRITUALITY->INCOMPATIBLE"}]->(child);

```
