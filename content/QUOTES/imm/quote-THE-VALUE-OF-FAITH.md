---
type: QUOTE
name: "quote.THE_VALUE_OF_FAITH"
alias: "Quote: Quote: THE VALUE OF FAITH"
parent: "topic.FAITH"
en_content: "Faith is only as potent and valuable (or, only as REAL) as the idea, object or person in/upon which that faith is placed.",
 es_title: "Cita: EL VALOR DE LA FE",
 es_content: "La fe es tan potente y valiosa (o tan REAL) como la idea, el objeto o la persona en la que se deposita esa fe.",
 fr_title: "Citation : LA VALEUR DE LA FOI",
 fr_content: "La foi n’est aussi puissante et précieuse (ou aussi RÉELLE) que l’idée, l’objet ou la personne dans/sur laquelle cette foi est placée.",
 hi_title: "उद्धरण: आस्था का मूल्य",
 hi_content: "विश्वास उतना ही शक्तिशाली और मूल्यवान है (या, केवल उतना ही वास्तविक) जितना कि वह विचार, वस्तु या व्यक्ति जिस पर वह विश्वास रखा गया है।",
 zh_title: "yǐn yòng ： xìn yǎng de jià zhí",
 zh_content: "xìn yǎng zhǐ yǒu yǔ xìn yǎng suǒ zài de xiǎng fǎ 、 wù tǐ huò rén yī yàng yǒu xiào hé yǒu jià zhí （ huò zhě shuō ， zhǐ yǒu hé zhēn shí yī yàng ）。"
tags: ["faith", "value", "worth", "target", "object"]
ptopic: "[[topic-FAITH]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_VALUE_OF_FAITH",
    alias: "Quote: Quote: THE VALUE OF FAITH",
    parent: "topic.FAITH",
    tags: ["faith", "value", "worth", "target", "object"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_VALUE_OF_FAITH",
    ctype: "QUOTE",
    en_title: "Quote: THE VALUE OF FAITH",
    en_content: "Faith is only as potent and valuable (or, only as REAL) as the idea, object or person in/upon which that faith is placed.",
 es_title: "Cita: EL VALOR DE LA FE",
 es_content: "La fe es tan potente y valiosa (o tan REAL) como la idea, el objeto o la persona en la que se deposita esa fe.",
 fr_title: "Citation : LA VALEUR DE LA FOI",
 fr_content: "La foi n’est aussi puissante et précieuse (ou aussi RÉELLE) que l’idée, l’objet ou la personne dans/sur laquelle cette foi est placée.",
 hi_title: "उद्धरण: आस्था का मूल्य",
 hi_content: "विश्वास उतना ही शक्तिशाली और मूल्यवान है (या, केवल उतना ही वास्तविक) जितना कि वह विचार, वस्तु या व्यक्ति जिस पर वह विश्वास रखा गया है।",
 zh_title: "yǐn yòng ： xìn yǎng de jià zhí",
 zh_content: "xìn yǎng zhǐ yǒu yǔ xìn yǎng suǒ zài de xiǎng fǎ 、 wù tǐ huò rén yī yàng yǒu xiào hé yǒu jià zhí （ huò zhě shuō ， zhǐ yǒu hé zhēn shí yī yàng ）。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_VALUE_OF_FAITH"})
MATCH (c:CONTENT {name: "content.THE_VALUE_OF_FAITH"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_VALUE_OF_FAITH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:QUOTE {name: "quote.THE_VALUE_OF_FAITH"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.FAITH->THE_VALUE_OF_FAITH"}]->(child);

```
