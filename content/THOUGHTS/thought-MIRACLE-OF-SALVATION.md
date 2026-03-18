---
type: THOUGHT
name: "thought.MIRACLE OF SALVATION"
alias: "Thought: Miracle Of Salvation"
parent: "topic.GRACE"
en_content: "Salvation (separating a sinner from their sin) is a miracle performed by God, not man."
tags: ["salvation", "miracle", "grace", "god", "transformation"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.MIRACLE OF SALVATION",
    alias: "Thought: Miracle Of Salvation",
    parent: "topic.GRACE",
    tags: ['salvation', 'miracle', 'grace', 'god', 'transformation'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MIRACLE OF SALVATION",
    ctype: "THOUGHT",
    en_title: "Miracle Of Salvation",
    en_content: "Salvation (separating a sinner from their sin) is a miracle performed by God, not man.",
    es_title: "Milagro de la Salvación",
    es_content: "La salvación (separar al pecador de su pecado) es un milagro realizado por Dios, no por el hombre.",
    fr_title: "Miracle du Salut",
    fr_content: "Le salut (séparer un pécheur de son péché) est un miracle accompli par Dieu, non par l'homme.",
    hi_title: "उद्धार का चमत्कार",
    hi_content: "उद्धार (पापी को उसके पाप से अलग करना) परमेश्वर द्वारा किया गया एक चमत्कार है, मनुष्य द्वारा नहीं।",
    zh_title: "jiù ēn de shén jì",
    zh_content: "jiù ēn (jiāng zuì rén cóng tā men de zuì è zhōng fēn lí chū lái) shì shàng dì suǒ xíng de shén jì, ér bù shì rén suǒ zuò de."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MIRACLE OF SALVATION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->MIRACLE OF SALVATION"
RETURN t, parent;
```
