---
type: THOUGHT
name: "thought.DUST"
alias: "Thought: Dust"
parent: "topic.ATTITUDE"
en_content: "God created the first human being from the cheapest and most abundant substance on Earth: DIRT.
Our value lies neither in our content nor in our capacity, but in The One for Whom we were created.
We were made for the pleasure of Christ!"
tags: ["dust", "humanity", "humility", "worth", "dirt"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DUST",
    alias: "Thought: Dust",
    parent: "topic.ATTITUDE",
    tags: ["dust", "humanity", "humility", "worth", "dirt"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DUST",
    ctype: "THOUGHT",
    en_title: "Thought: Dust",
    en_content: "God created the first human being from the cheapest and most abundant substance on Earth: DIRT.
Our value lies neither in our content nor in our capacity, but in The One for Whom we were created.
We were made for the pleasure of Christ!",
    es_title: "Pensamiento: polvo",
    es_content: "Dios creó al primer ser humano a partir de la sustancia más barata y abundante de la Tierra: LA SUCIEDAD.
Nuestro valor no reside ni en nuestro contenido ni en nuestra capacidad, sino en Aquel para quien fuimos creados.
¡Fuimos hechos para complacer a Cristo!",
    fr_title: "Pensée : Poussière",
    fr_content: "Dieu a créé le premier être humain à partir de la substance la moins chère et la plus abondante sur Terre : la SALETÉ.
Notre valeur ne réside ni dans notre contenu ni dans notre capacité, mais dans Celui pour qui nous avons été créés.
Nous avons été créés pour le plaisir du Christ !",
    hi_title: "विचार: धूल",
    hi_content: "भगवान ने पृथ्वी पर सबसे सस्ते और सबसे प्रचुर पदार्थ: गंदगी से पहला इंसान बनाया।
हमारा मूल्य न तो हमारी सामग्री में है और न ही हमारी क्षमता में, बल्कि उस व्यक्ति में है जिसके लिए हम बनाए गए हैं।
हम मसीह की ख़ुशी के लिए बनाये गये थे!",
    zh_title: "xiǎng fǎ : chén āi",
    zh_content: "shàng dì yòng dì qiú shàng zuì pián yi 、 zuì fēng fù de wù zhì chuàng zào le dì yí gè rén lèi : ní tǔ . wǒ men de jià zhí jì bù zài yú wǒ men de nèi róng , yě bù zài yú wǒ men de néng lì , ér zài yú wǒ men wèi zhī ér shēng de nà yī wèi . wǒ men bèi zào shì wèi le tǎo jī dū de xǐ yuè !"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DUST"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->DUST"
RETURN t, parent;
```
