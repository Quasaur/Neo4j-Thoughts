---
type: QUOTE
name: "quote.ONE FAMILY"
alias: "Quote: One Family"
parent: "topic.THE-GOSPEL"
en_content: "GOD created the human family with the intent of filling its members with the SAME FULLNESS His Divine Family enjoys; since the advent of sin, however, humans have conspired with demons to so darken that which was designed to be glorious that the Presence of Divinity would be temporarily forced out.",
 es_title: "Cita: UNA FAMILIA",
 es_content: "DIOS creó la familia humana con la intención de llenar a sus miembros de la MISMA PLENITUD de la que disfruta Su Divina Familia; Sin embargo, desde la llegada del pecado, los humanos han conspirado con los demonios para oscurecer tanto lo que fue diseñado para ser glorioso que la Presencia de la Divinidad sería temporalmente expulsada.",
 fr_title: "Citation : UNE FAMILLE",
 fr_content: "DIEU a créé la famille humaine dans le but de remplir ses membres de la MÊME PLÉNITÉ dont jouit Sa Divine Famille ; Cependant, depuis l'avènement du péché, les humains ont conspiré avec les démons pour assombrir tellement ce qui était conçu pour être glorieux, de sorte que la Présence de la Divinité soit temporairement expulsée.",
 hi_title: "उद्धरण: एक परिवार",
 hi_content: "भगवान ने मानव परिवार की रचना इसके सदस्यों को उसी पूर्णता से भरने के इरादे से की जिसका आनंद उनके दिव्य परिवार को मिलता है; हालाँकि, पाप के आगमन के बाद से, मनुष्यों ने राक्षसों के साथ मिलकर उसे इतना अंधकारमय बनाने की साजिश रची है कि जिसे गौरवशाली बनाया गया था, देवत्व की उपस्थिति अस्थायी रूप से समाप्त हो जाएगी।",
 zh_title: "yǐn yòng ： yí gè jiā tíng",
 zh_content: "shàng dì chuàng zào le rén lèi jiā tíng ， qí mù dì shì ràng qí chéng yuán chōng mǎn tā shén shèng jiā tíng suǒ xiǎng yǒu de tóng yàng de chōng shí ； rán ér ， zì cóng zuì è chū xiàn yǐ lái ， rén lèi jiù yǔ è mó mì móu ， shǐ yuán běn róng yào de shì wù biàn dé hēi àn ， yǐ zhì shén xìng de cún zài jiāng zàn shí bèi qū zhú 。"
tags: ["tribe", "clan", "family", "united", "jesus_christ"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ONE FAMILY",
    alias: "Quote: One Family",
    parent: "topic.THE-GOSPEL",
    tags: ["tribe", "clan", "family", "united", "jesus_christ"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ONE FAMILY",
    ctype: "QUOTE",
    en_title: "One Family",
    en_content: "GOD created the human family with the intent of filling its members with the SAME FULLNESS His Divine Family enjoys; since the advent of sin, however, humans have conspired with demons to so darken that which was designed to be glorious that the Presence of Divinity would be temporarily forced out.",
 es_title: "Cita: UNA FAMILIA",
 es_content: "DIOS creó la familia humana con la intención de llenar a sus miembros de la MISMA PLENITUD de la que disfruta Su Divina Familia; Sin embargo, desde la llegada del pecado, los humanos han conspirado con los demonios para oscurecer tanto lo que fue diseñado para ser glorioso que la Presencia de la Divinidad sería temporalmente expulsada.",
 fr_title: "Citation : UNE FAMILLE",
 fr_content: "DIEU a créé la famille humaine dans le but de remplir ses membres de la MÊME PLÉNITÉ dont jouit Sa Divine Famille ; Cependant, depuis l'avènement du péché, les humains ont conspiré avec les démons pour assombrir tellement ce qui était conçu pour être glorieux, de sorte que la Présence de la Divinité soit temporairement expulsée.",
 hi_title: "उद्धरण: एक परिवार",
 hi_content: "भगवान ने मानव परिवार की रचना इसके सदस्यों को उसी पूर्णता से भरने के इरादे से की जिसका आनंद उनके दिव्य परिवार को मिलता है; हालाँकि, पाप के आगमन के बाद से, मनुष्यों ने राक्षसों के साथ मिलकर उसे इतना अंधकारमय बनाने की साजिश रची है कि जिसे गौरवशाली बनाया गया था, देवत्व की उपस्थिति अस्थायी रूप से समाप्त हो जाएगी।",
 zh_title: "yǐn yòng ： yí gè jiā tíng",
 zh_content: "shàng dì chuàng zào le rén lèi jiā tíng ， qí mù dì shì ràng qí chéng yuán chōng mǎn tā shén shèng jiā tíng suǒ xiǎng yǒu de tóng yàng de chōng shí ； rán ér ， zì cóng zuì è chū xiàn yǐ lái ， rén lèi jiù yǔ è mó mì móu ， shǐ yuán běn róng yào de shì wù biàn dé hēi àn ， yǐ zhì shén xìng de cún zài jiāng zàn shí bèi qū zhú 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.ONE FAMILY"})
MATCH (c:CONTENT {name: "content.ONE FAMILY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ONE FAMILY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MATCH (child:QUOTE {name: "quote.ONE FAMILY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->ONE FAMILY"}]->(child);

```
