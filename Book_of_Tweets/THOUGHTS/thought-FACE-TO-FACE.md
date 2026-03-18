---
type: THOUGHT
name: "thought.FACE TO FACE"
alias: "Thought: Face To Face"
parent: "topic.THE GODHEAD"
en_content: "When you meet God face to Face you will not ask any questions; His Glory is the answer to every question and the end of every dispute."
tags: ["glory", "encounter", "presence", "truth", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011b)
CREATE (t:THOUGHT {    name: "thought.FACE TO FACE",
    alias: "Thought: Face To Face",
    parent: "topic.THE GODHEAD",
    tags: ['glory', 'encounter', 'presence', 'truth', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.FACE TO FACE",
    ctype: "THOUGHT",
    en_title: "Face To Face",
    en_content: "When you meet God face to Face you will not ask any questions; His Glory is the answer to every question and the end of every dispute.",
    es_title: "Cara a Cara",
    es_content: "Cuando te encuentres con Dios cara a cara no harás ninguna pregunta; Su Gloria es la respuesta a toda pregunta y el fin de toda disputa.",
    fr_title: "Face à Face",
    fr_content: "Quand vous rencontrerez Dieu face à face, vous ne poserez aucune question ; Sa Gloire est la réponse à toute question et la fin de tout différend.",
    hi_title: "आमने-सामने",
    hi_content: "जब आप परमेश्वर से आमने-सामने मिलेंगे तो आप कोई प्रश्न नहीं पूछेंगे; उनकी महिमा हर प्रश्न का उत्तर है और हर विवाद का अंत है।",
    zh_title: "mian dui mian",
    zh_content: "dang ni yu shen mian dui mian xiang yu shi, ni bu hui ti ren he wen ti; ta de rong yao shi mei ge wen ti de da an, ye shi mei chang zheng lun de zhong jie."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FACE TO FACE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->FACE TO FACE"
RETURN t, parent;
```
