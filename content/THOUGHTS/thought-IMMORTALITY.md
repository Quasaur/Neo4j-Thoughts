---
type: THOUGHT
name: "thought.IMMORTALITY"
alias: "Thought: Immortality"
parent: "topic.FAITHFULNESS"
tags: ["immortality", "eternal_life", "salvation", "desire", "jesus_christ"]
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.IMMORTALITY",
    alias: "Thought: Immortality",
    parent: "topic.FAITHFULNESS",
    tags: ["immortality", "eternal_life", "salvation", "desire", "jesus_christ"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IMMORTALITY",
    ctype: "THOUGHT",
    en_title: "Immortality",
    en_content: "",
    es_title: "INMORTALIDAD",
    es_content: "Nos han lavado el cerebro para creer que nuestra MAYOR NECESIDAD está, en el mejor de los casos, fuera de nuestro alcance o, en el peor, no existe.
Incluso en el mejor de los casos lo definimos erróneamente como el cumplimiento de todo deseo.
¡¡¡INMORTALIDAD es estar TAN LLENO DE JESÚS que el propio Deseo deja de existir!!!!",
    fr_title: "IMMORTALITÉ",
    fr_content: "Nous avons subi un lavage de cerveau en nous faisant croire que notre PLUS GRAND BESOIN est, au mieux, hors de notre portée ou, au pire, n’existe pas.
Même au mieux, nous le définissons à tort comme l’accomplissement de tous les désirs.
L'IMMORTALITÉ, c'est être TELLEMENT PLEINE DE JÉSUS que le Désir lui-même cesse d'exister !!!!",
    hi_title: "अमरता",
    hi_content: "हमें यह विश्वास दिला दिया गया है कि हमारी सबसे बड़ी जरूरत हमारी समझ से परे है या बुरी स्थिति में उसका अस्तित्व ही नहीं है।
सर्वोत्तम स्थिति में भी हम इसे सभी इच्छाओं की पूर्ति के रूप में गलत परिभाषित करते हैं।
अमरता का अर्थ यीशु से इतना परिपूर्ण होना है कि इच्छा का अस्तित्व ही समाप्त हो जाए!!!!",
    zh_title: "bù xiǔ",
    zh_content: "wǒ men bèi xǐ nǎo ， xiāng xìn wǒ men zuì dà de xū qiú chōng qí liàng shì chāo chū wǒ men de néng lì fàn wéi ， huò zhě zuì huài de qíng kuàng shì bù cún zài 。
 jí shǐ zài zuì hǎo de qíng kuàng xià ， wǒ men yě huì cuò wù dì jiāng qí dìng yì wèi suǒ yǒu yuàn wàng de shí xiàn 。
 bù xiǔ jiù shì chōng mǎn yē sū ， yǐ zhì yù wàng běn shēn bù fù cún zài ！！！！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.IMMORTALITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FAITHFULNESS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FAITHFULNESS->IMMORTALITY"
RETURN t, parent;
```
