---
type: THOUGHT
name: "thought.ADDICTION"
alias: "Thought: Addiction"
parent: "topic.PSYCHOLOGY"
tags: ["sanctification", "addiction", "flesh", "the_cross", "jesus_christ"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ADDICTION",
    alias: "Thought: Addiction",
    parent: "topic.PSYCHOLOGY",
    tags: ["sanctification", "addiction", "flesh", "the_cross", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ADDICTION",
    ctype: "THOUGHT",
    en_title: "Addiction",
    en_content: "",
    es_title: "ADICCIÓN",
    es_content: "Ya sea homosexualidad, pornografía, drogas, alcohol, codicia o simple arrogancia... sólo hay UNA CURA para la adicción: la muerte de Cristo en la cruz. 
Si tú, por El Espíritu de Cristo, puedes PARTICIPAR en Su Muerte, ¡también puedes experimentar la Gloria y el Poder de Su VIDA SIN PECADO! 
Romanos 6:7",
    fr_title: "DÉPENDANCE",
    fr_content: "Qu’il s’agisse d’homosexualité, de porno, de drogues, d’alcool, de convoitise ou de simple orgueil… il n’y a qu’UN SEUL REMÈDE contre la dépendance : la mort du Christ sur la croix. 
Si vous, par l'Esprit du Christ, pouvez PARTICIPER à Sa mort, vous pouvez également expérimenter la Gloire et la Puissance de Sa VIE SANS PÉCHÉ ! 
Romains 6:7",
    hi_title: "लत",
    hi_content: "चाहे वह समलैंगिकता हो, पोर्न हो, ड्रग्स हो, शराब हो, लोभ हो या साधारण अभिमान हो... व्यसन का केवल एक ही इलाज है: क्रूस पर मसीह की मृत्यु। 
यदि आप, मसीह की आत्मा के द्वारा, उनकी मृत्यु में भाग ले सकते हैं, तो आप उनके निष्पाप जीवन की महिमा और शक्ति का भी अनुभव कर सकते हैं! 
रोमियों 6:7",
    zh_title: "yǐn",
    zh_content: "wú lùn shì tóng xìng liàn 、 sè qíng 、 dú pǐn 、 jiǔ jīng 、 tān lán hái shì jiǎn dān de ào màn …… zhì liáo chéng yǐn de fāng fǎ zhǐ yǒu yī zhǒng ： jī dū sǐ zài shí zì jià shàng 。 
 rú guǒ nǐ kào zhe jī dū de líng ， néng cān yù tā de sǐ wáng ， nǐ yě néng tǐ yàn dào tā wú zuì shēng mìng de róng yào hé lì liàng ！ 
 luó mǎ shū  6:7"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ADDICTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->ADDICTION"
RETURN t, parent;
```
