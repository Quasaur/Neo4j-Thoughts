---
type: THOUGHT
name: "thought.SOL ROTATION"
alias: "Thought: Sol Rotation"
parent: "topic.CREATION"
en_content: "Creation Wonder: A point at the Sun's equator takes 25 days to rotate, while points 15° from the sun's north and south poles take 34 days!"
tags: ["sol", "sun", "star", "rotation", "axis"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SOL ROTATION",
    alias: "Thought: Sol Rotation",
    parent: "topic.CREATION",
    tags: ["sol", "sun", "star", "rotation", "axis"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SOL ROTATION",
    ctype: "THOUGHT",
    en_title: "Sol Rotation",
    en_content: "Creation Wonder: A point at the Sun's equator takes 25 days to rotate, while points 15° from the sun's north and south poles take 34 days!",
    es_title: "ROTACIÓN SOLAR",
    es_content: "Maravilla de la creación: un punto en el ecuador del Sol tarda 25 días en girar, mientras que los puntos a 15° de los polos norte y sur del Sol tardan 34 días.",
    fr_title: "ROTATION DU SOL",
    fr_content: "Merveille de création : un point à l'équateur du Soleil met 25 jours pour tourner, tandis que les points à 15° des pôles nord et sud du Soleil mettent 34 jours !",
    hi_title: "एसओएल रोटेशन",
    hi_content: "सृष्टि का आश्चर्य: सूर्य के भूमध्य रेखा पर एक बिंदु को घूमने में 25 दिन लगते हैं, जबकि सूर्य के उत्तरी और दक्षिणी ध्रुव से 15° की दूरी पर स्थित बिंदुओं को घूमने में 34 दिन लगते हैं!",
    zh_title: "róng jiāo xuán zhuǎn",
    zh_content: "chuàng shì qí guān ： tài yáng chì dào shàng de yì diǎn xū yào 25 tiān cái néng zì zhuàn ， ér yǔ tài yáng nán běi liǎng jí chéng 15° de diǎn zé xū yào 34 tiān ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SOL ROTATION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->SOL ROTATION"
RETURN t, parent;
```
