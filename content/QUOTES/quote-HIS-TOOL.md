---
type: QUOTE
name: "quote.HIS TOOL"
alias: "Quote: His Tool"
parent: "topic.EVIL"
source: "The Narrow Way"
en_content: "The Truth is this: a small cabal of individuals rule the world; their master is the Devil (1 John 5:19) and his Masters are the GODHEAD. Evil is a tool in the Hand of a Holy GOD, used to accomplish His Good Purpose (Genesis 50:20; Romans 8:28)."
tags: ["knowing", "confidence", "guarantee", "holy_spirit", "divine_witness"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.HIS TOOL",
    alias: "Quote: His Tool",
    parent: "topic.EVIL",
    tags: ["knowing", "confidence", "guarantee", "holy_spirit", "divine_witness"],
    source: "The Narrow Way",
    booklink: "https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.HIS TOOL",
    ctype: "QUOTE",
    en_title: "Quote: His Tool",
    en_content: "The Truth is this: a small cabal of individuals rule the world; their master is the Devil (1 John 5:19) and his Masters are the GODHEAD. Evil is a tool in the Hand of a Holy GOD, used to accomplish His Good Purpose (Genesis 50:20; Romans 8:28).",
 es_title: "Cita: Su herramienta",
 es_content: "La Verdad es ésta: una pequeña camarilla de individuos gobierna el mundo; su amo es el Diablo (1 Juan 5:19) y sus Amos son la DIOSA. El mal es una herramienta en la Mano de un DIOS Santo, utilizada para lograr Su Buen Propósito (Génesis 50:20; Romanos 8:28).",
 fr_title: "Citation : Son outil",
 fr_content: "La Vérité est la suivante : une petite cabale d’individus gouverne le monde ; leur maître est le Diable (1 Jean 5:19) et ses Maîtres sont la DIVINITÉ. Le mal est un outil entre les mains d’un DIEU Saint, utilisé pour accomplir son bon dessein (Genèse 50:20 ; Romains 8:28).",
 hi_title: "उद्धरण: उसका उपकरण",
 hi_content: "सच्चाई यह है: व्यक्तियों का एक छोटा समूह दुनिया पर शासन करता है; उनका स्वामी शैतान है (1 यूहन्ना 5:19) और उसके स्वामी परमेश्वर हैं। बुराई पवित्र ईश्वर के हाथ में एक उपकरण है, जिसका उपयोग उसके अच्छे उद्देश्य को पूरा करने के लिए किया जाता है (उत्पत्ति 50:20; रोमियों 8:28)।",
 zh_title: "yǐn yòng ：tā de gōng jù",
 zh_content: "shì shí shì zhè yàng de : yī xiǎo qún rén tǒng zhì zhe shì jiè ; tā men de zhǔ rén shì mó guǐ （ yuē hàn yī shū 5:19）, ér tā de zhǔ rén shì shén . xié è shì shén shèng zhī shén de shǒu zhōng de gōng jù , yòng lái shí xiàn tā de měi hǎo mù dì （ chuàng shì jì 50:20; luó mǎ shū 8:28）."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.HIS TOOL"})
MATCH (c:CONTENT {name: "content.HIS TOOL"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.HIS TOOL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:QUOTE {name: "quote.HIS TOOL"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->HIS TOOL"}]->(child);

```
