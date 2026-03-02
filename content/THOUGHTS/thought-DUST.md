---
type: THOUGHT
name: "thought.DUST"
alias: "Thought: DUST"
parent: "topic.ATTITUDE"
tags: ["dust", "humanity", "humility", "worth", "dirt"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DUST",
    alias: "Thought: DUST",
    parent: "topic.ATTITUDE",
    tags: ["dust", "humanity", "humility", "worth", "dirt"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DUST",
    ctype: "THOUGHT",
    en_title: "DUST",
 es_title: "POLVO",
 fr_title: "POUSSIÈRE",
 hi_title: "धूल",
 zh_title: "huī chén",
    en_content: "",
 es_content: "DIOS creó al primer ser humano a partir de la sustancia más barata y abundante de la Tierra: LA SUCIEDAD. 
Nuestro valor no reside ni en nuestro contenido ni en nuestra capacidad, sino en para quién fuimos creados. 
¡Fuimos hechos para el placer de Cristo!",
 fr_content: "DIEU a créé le premier humain à partir de la substance la moins chère et la plus abondante sur Terre : la SALETÉ. 
Notre valeur ne réside ni dans notre contenu ni dans nos capacités, mais dans celui pour qui nous avons été créés. 
Nous avons été faits pour le plaisir du Christ !",
 hi_content: "भगवान ने पृथ्वी पर सबसे सस्ते, सबसे प्रचुर पदार्थ: गंदगी से पहला मानव बनाया। 
हमारा मूल्य न तो हमारी सामग्री में है और न ही हमारी क्षमता में, बल्कि इसमें है कि हम किसके लिए बने हैं। 
हम मसीह की ख़ुशी के लिए बनाये गये थे!",
 zh_content: "shàng dì yòng dì qiú shàng zuì pián yi 、 zuì fēng fù de wù zhì chuàng zào le dì yí gè rén lèi ： ní tǔ 。 
 wǒ men de jià zhí jì bù zài yú wǒ men de nèi róng ， yě bù zài yú wǒ men de néng lì ， ér zài yú wǒ men wèi shuí ér shēng 。 
 wǒ men shì wèi le jī dū de xǐ yuè ér bèi zào de ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DUST" AND c.name = "content.DUST"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.DUST"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.DUST"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->DUST"}]->(child);
```