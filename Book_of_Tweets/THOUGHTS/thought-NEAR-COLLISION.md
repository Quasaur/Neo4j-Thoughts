---
type: THOUGHT
name: "thought.NEAR COLLISION"
alias: "Thought: Near Collision"
parent: "topic.SPIRITUALITY"
en_content: "An AA jet had a near collision with a United over AL...my sister was on the AA plane and could read the writing on the other plane."
tags: ["providence", "protection", "safety", "miracle", "spirituality"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Apr-2011)
CREATE (t:THOUGHT {    name: "thought.NEAR COLLISION",
    alias: "Thought: Near Collision",
    parent: "topic.SPIRITUALITY",
    tags: ['providence', 'protection', 'safety', 'miracle', 'spirituality'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.NEAR COLLISION",
    ctype: "THOUGHT",
    en_title: "Near Collision",
    en_content: "An AA jet had a near collision with a United over AL...my sister was on the AA plane and could read the writing on the other plane.",
    es_title: "Casi colisión",
    es_content: "Un avión AA estuvo a punto de colisionar con un United sobre AL... mi hermana estaba en el avión AA y podía leer la escritura en el otro avión.",
    fr_title: "Quasi-collision",
    fr_content: "Un avion à réaction AA a failli entrer en collision avec un United au-dessus d'AL... ma sœur était dans l'avion AA et pouvait lire les écrits sur l'autre avion.",
    hi_title: "टक्कर के निकट",
    hi_content: "एक एए जेट की एएल के ऊपर युनाइटेड से सीधी टक्कर हो गई...मेरी बहन एए विमान में थी और दूसरे विमान में लिखा पढ़ सकती थी।",
    zh_title: "xiǎn xiē fā shēng pèng zhuàng",
    zh_content: "yī jià  AA  pēn qì shì fēi jī zài  AL  shàng yǔ yī jià lián hé háng kōng chà diǎn xiāng zhuàng …… wǒ jiě jiě zài  AA  fēi jī shàng ， kě yǐ yuè dú lìng yī jià fēi jī shàng de wén zì 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NEAR COLLISION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->NEAR COLLISION"
RETURN t, parent;
```
