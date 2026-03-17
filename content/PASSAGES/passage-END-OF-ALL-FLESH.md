---
type: PASSAGE
name: "passage.END OF ALL FLESH"
alias: "Passage: The End of All Flesh"
parent: "topic.DIVINE SOVEREIGNTY"
sortedsource: "Genesis 06:13"
en_content: "And God said unto Noah, 'The end of** all flesh is come before me; for the Earth is filled with violence through them; and, behold, I will destroy them with the** Earth.'"
tags: ["judgment", "sovereignty", "end_times", "justice", "divinity"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (p:PASSAGE {
    name: "passage.END OF ALL FLESH",
    alias: "Passage: The End of All Flesh",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ["judgment", "sovereignty", "end_times", "justice", "divinity"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.END OF ALL FLESH",
    ctype: "PASSAGE",
    en_title: "Passage: The End of All Flesh",
    en_content: "And God said unto Noah, 'The end of** all flesh is come before me; for the Earth is filled with violence through them; and, behold, I will destroy them with the** Earth.",
    es_title: "Pensamiento: El fin de toda carne",
    es_content: "Y dijo Dios a Noé: 'El fin de** toda carne ha llegado delante de mí; porque la Tierra se llena de violencia a través de ellos; y he aquí, los destruiré junto con la** Tierra.",
    fr_title: "Pensée : La fin de toute chair",
    fr_content: "Et Dieu dit à Noé : 'La fin de** toute chair est venue devant moi ; car la Terre est remplie de violence à cause d'eux ; et voici, je les détruirai avec la** Terre.",
    hi_title: "विचार: सभी प्राणियों का अंत",
    hi_content: "और परमेश्वर ने नूह से कहा, 'सभी प्राणियों का अंत** मेरे सामने आ गया है; क्योंकि पृय्वी उनके द्वारा उपद्रव से भर गई है; और देख, मैं उनको पृय्वी समेत नाश करूंगा।",
    zh_title: "sī xiǎng : suǒ yǒu ròu tǐ de zhōng jié",
    zh_content: "shén duì nuó yà shuō :“ yī qiè yǒu xuè qì de rén de mò rì yǐ jīng lái dào wǒ miàn qián ; yīn wèi dì qiú shàng chōng mǎn le tā men de bào lì ; ér qiě , kàn nǎ , wǒ huì yòng ** dì qiú huǐ miè tā men ."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (p)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "p.edge.END OF ALL FLESH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH p
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(p)
ON CREATE SET r2.name = "p.edge.DIVINE SOVEREIGNTY->END OF ALL FLESH"
RETURN p, parent;
```
