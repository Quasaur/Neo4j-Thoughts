---
type: THOUGHT
name: "thought.DUST"
alias: "Thought: Dust"
parent: "topic.ATTITUDE"
tags: ["dust", "humanity", "humility", "worth", "dirt"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
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
    en_title: "Dust",
    en_content: "",
    es_title: "POLVO",
    es_content: "DIOS creó al primer ser humano a partir de la sustancia más barata y abundante de la Tierra: LA SUCIEDAD. 
Nuestro valor no reside ni en nuestro contenido ni en nuestra capacidad, sino en para quién fuimos creados. 
¡Fuimos hechos para el placer de Cristo!",
    fr_title: "POUSSIÈRE",
    fr_content: "DIEU a créé le premier humain à partir de la substance la moins chère et la plus abondante sur Terre : la SALETÉ. 
Notre valeur ne réside ni dans notre contenu ni dans nos capacités, mais dans celui pour qui nous avons été créés. 
Nous avons été faits pour le plaisir du Christ !",
    hi_title: "धूल",
    hi_content: "भगवान ने पृथ्वी पर सबसे सस्ते, सबसे प्रचुर पदार्थ: गंदगी से पहला मानव बनाया। 
हमारा मूल्य न तो हमारी सामग्री में है और न ही हमारी क्षमता में, बल्कि इसमें है कि हम किसके लिए बने हैं। 
हम मसीह की ख़ुशी के लिए बनाये गये थे!",
    zh_title: "huī chén",
    zh_content: "shàng dì yòng dì qiú shàng zuì pián yi 、 zuì fēng fù de wù zhì chuàng zào le dì yí gè rén lèi ： ní tǔ 。 
 wǒ men de jià zhí jì bù zài yú wǒ men de nèi róng ， yě bù zài yú wǒ men de néng lì ， ér zài yú wǒ men wèi shuí ér shēng 。 
 wǒ men shì wèi le jī dū de xǐ yuè ér bèi zào de ！"
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
