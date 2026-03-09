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
 es_title: "INMORTALIDAD",
 fr_title: "IMMORTALITÉ",
 hi_title: "अमरता",
 zh_title: "bù xiǔ",
    en_content: "",
 es_content: "Nos han lavado el cerebro para creer que nuestra MAYOR NECESIDAD está, en el mejor de los casos, fuera de nuestro alcance o, en el peor, no existe.
Incluso en el mejor de los casos lo definimos erróneamente como el cumplimiento de todo deseo.
¡¡¡INMORTALIDAD es estar TAN LLENO DE JESÚS que el propio Deseo deja de existir!!!!",
 fr_content: "Nous avons subi un lavage de cerveau en nous faisant croire que notre PLUS GRAND BESOIN est, au mieux, hors de notre portée ou, au pire, n’existe pas.
Même au mieux, nous le définissons à tort comme l’accomplissement de tous les désirs.
L'IMMORTALITÉ, c'est être TELLEMENT PLEINE DE JÉSUS que le Désir lui-même cesse d'exister !!!!",
 hi_content: "हमें यह विश्वास दिला दिया गया है कि हमारी सबसे बड़ी जरूरत हमारी समझ से परे है या बुरी स्थिति में उसका अस्तित्व ही नहीं है।
सर्वोत्तम स्थिति में भी हम इसे सभी इच्छाओं की पूर्ति के रूप में गलत परिभाषित करते हैं।
अमरता का अर्थ यीशु से इतना परिपूर्ण होना है कि इच्छा का अस्तित्व ही समाप्त हो जाए!!!!",
 zh_content: "wǒ men bèi xǐ nǎo ， xiāng xìn wǒ men zuì dà de xū qiú chōng qí liàng shì chāo chū wǒ men de néng lì fàn wéi ， huò zhě zuì huài de qíng kuàng shì bù cún zài 。
 jí shǐ zài zuì hǎo de qíng kuàng xià ， wǒ men yě huì cuò wù dì jiāng qí dìng yì wèi suǒ yǒu yuàn wàng de shí xiàn 。
 bù xiǔ jiù shì chōng mǎn yē sū ， yǐ zhì yù wàng běn shēn bù fù cún zài ！！！！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IMMORTALITY" AND c.name = "content.IMMORTALITY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.IMMORTALITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITHFULNESS" AND child.name = "thought.IMMORTALITY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITHFULNESS->IMMORTALITY"}]->(child);
```