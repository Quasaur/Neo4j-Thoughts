---
type: THOUGHT
name: "thought.HEAVEN BY GRACE"
alias: "Thought: Heaven By Grace"
parent: "topic.GRACE"
en_content: "I know I have no business being in Heaven--but I'm going...such is the Power of Divine Grace!"
tags: ["grace", "heaven", "salvation", "power", "merit"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN BY GRACE",
    alias: "Thought: Heaven By Grace",
    parent: "topic.GRACE",
    tags: ['grace', 'heaven', 'salvation', 'power', 'merit'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HEAVEN BY GRACE",
    ctype: "THOUGHT",
    en_title: "Heaven By Grace",
    en_content: "I know I have no business being in Heaven--but I'm going...such is the Power of Divine Grace!",
    es_title: "El Cielo por Gracia",
    es_content: "Sé que no tengo derecho a estar en el Cielo--pero voy a ir...¡tal es el Poder de la Gracia Divina!",
    fr_title: "Le Ciel par Grâce",
    fr_content: "Je sais que je n'ai aucun droit d'être au Ciel--mais j'y vais...tel est le Pouvoir de la Grâce Divine !",
    hi_title: "अनुग्रह से स्वर्ग",
    hi_content: "मैं जानता हूं कि मेरा स्वर्ग में होने का कोई अधिकार नहीं है--लेकिन मैं जा रहा हूं...ऐसी है दिव्य अनुग्रह की शक्ति!",
    zh_title: "Yin En De Tian Tang",
    zh_content: "Wo zhi dao wo mei you zi ge jin ru tian tang--dan wo yao qu...zhe jiu shi shen sheng en dian de li liang!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HEAVEN BY GRACE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->HEAVEN BY GRACE"
RETURN t, parent;
```
