---
type: THOUGHT
name: "thought.WALKING WITH GOD"
alias: "Thought: Walking With God"
parent: "topic.SPIRITUALITY"
en_content: "The Bible doesn't say that God walked with Enoch, but that Enoch walked with God. Enoch was led by the Holy Spirit."
tags: ["holy_spirit", "enoch", "spirituality", "obedience", "fellowship"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Sep-2010)
CREATE (t:THOUGHT {    name: "thought.WALKING WITH GOD",
    alias: "Thought: Walking With God",
    parent: "topic.SPIRITUALITY",
    tags: ['holy_spirit', 'enoch', 'spirituality', 'obedience', 'fellowship'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.WALKING WITH GOD",
    ctype: "THOUGHT",
    en_title: "Walking With God",
    en_content: "The Bible doesn't say that God walked with Enoch, but that Enoch walked with God. Enoch was led by the Holy Spirit.",
    es_title: "Caminando con Dios",
    es_content: "La Biblia no dice que Dios caminó con Enoc, sino que Enoc caminó con Dios.Enoc fue guiado por el Espíritu Santo.",
    fr_title: "Marcher avec Dieu",
    fr_content: "La Bible ne dit pas que Dieu marchait avec Enoch, mais qu'Enoch marchait avec Dieu.Hénoc était dirigé par le Saint-Esprit.",
    hi_title: "भगवान के साथ चलना",
    hi_content: "बाइबल यह नहीं कहती कि परमेश्वर हनोक के साथ चला, बल्कि यह कि हनोक परमेश्वर के साथ चला।हनोक का नेतृत्व पवित्र आत्मा द्वारा किया गया था।",
    zh_title: "yǔ shén tóng háng",
    zh_content: "shèng jīng méi yǒu shuō shén yǔ yǐ nuò tóng háng ， ér shì shuō yǐ nuò yǔ shén tóng háng 。 yǐ nuò shì bèi shèng líng yǐn dǎo de 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WALKING WITH GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->WALKING WITH GOD"
RETURN t, parent;
```
