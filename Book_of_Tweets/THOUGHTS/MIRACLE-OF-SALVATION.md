---
name: "thought.MIRACLE OF SALVATION"
alias: "Thought: Miracle Of Salvation"
type: THOUGHT
en_content: "Salvation (separating a sinner from their sin) is a miracle performed by God, not man."
parent: "topic.GRACE"
tags:
- salvation
- miracle
- grace
- god
- transformation
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Oct-2011d)
CREATE (t:THOUGHT {
    name: "thought.MIRACLE OF SALVATION",
    alias: "Thought: Miracle Of Salvation",
    parent: "topic.GRACE",
    tags: ['salvation', 'miracle', 'grace', 'god', 'transformation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MIRACLE OF SALVATION",
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

MATCH (t:THOUGHT {name: "thought.MIRACLE OF SALVATION"})
MATCH (c:CONTENT {name: "content.MIRACLE OF SALVATION"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.MIRACLE OF SALVATION" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.MIRACLE OF SALVATION"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE->MIRACLE OF SALVATION" }]->(child);
```
