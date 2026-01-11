---
name: "thought.SOL_ROTATION"
alias: "Thought: SOL ROTATION"
type: THOUGHT
parent: topic.CREATION
tags:
- sol
- sun
- star
- rotation
- axis
neo4j: true
ptopic: "[[topic-CREATION]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SOL_ROTATION",
    alias: "Thought: SOL ROTATION",
    parent: "topic.CREATION",
    tags: ["sol", "sun", "star", "rotation", "axis"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SOL_ROTATION",
    en_title: "SOL ROTATION",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SOL_ROTATION" AND c.name = "content.SOL_ROTATION"
MERGE (t)-[:HAS_CONTENT {name: "edge.SOL_ROTATION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.SOL_ROTATION"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->SOL_ROTATION"}]->(child);
```
