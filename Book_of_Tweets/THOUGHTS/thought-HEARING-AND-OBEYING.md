---
type: THOUGHT
name: "thought.HEARING AND OBEYING"
alias: "Thought: Hearing And Obeying"
parent: "topic.SPIRITUALITY"
en_content: "Half the battle: Hearing God's Voice; the Other Half: obeying it."
tags: ["obedience", "guidance", "spirituality", "listening", "faith"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Aug-2010)
CREATE (t:THOUGHT {    name: "thought.HEARING AND OBEYING",
    alias: "Thought: Hearing And Obeying",
    parent: "topic.SPIRITUALITY",
    tags: ['obedience', 'guidance', 'spirituality', 'listening', 'faith'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.HEARING AND OBEYING",
    ctype: "THOUGHT",
    en_title: "Hearing And Obeying",
    en_content: "Half the battle: Hearing God's Voice; the Other Half: obeying it.",
    es_title: "Escuchar y obedecer",
    es_content: "La mitad de la batalla: escuchar la voz de Dios;la Otra Mitad: obedecerla.",
    fr_title: "Entendre et obéir",
    fr_content: "La moitié de la bataille : entendre la voix de Dieu ;l'autre moitié : lui obéir.",
    hi_title: "सुनना और पालन करना",
    hi_content: "आधी लड़ाई: भगवान की आवाज सुनना;दूसरा भाग: इसका पालन करना।",
    zh_title: "líng tīng yǔ fú cóng",
    zh_content: "chéng gōng yí bàn ： líng tīng shàng dì de shēng yīn ； lìng yí bàn ： fú cóng tā 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HEARING AND OBEYING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->HEARING AND OBEYING"
RETURN t, parent;
```
