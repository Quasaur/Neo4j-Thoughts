---
type: THOUGHT
name: "thought.DISENFRANCHISING POOR WATCHING"
alias: "Thought: Disenfranchising Poor Watching"
parent: "topic.MORALITY"
en_content: "To those that continue to disenfranchise the poor and minorities: GOD IS WATCHING."
tags: ["poor", "minorities", "watching", "justice", "morality"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jul-2013a)
CREATE (t:THOUGHT {    name: "thought.DISENFRANCHISING POOR WATCHING",
    alias: "Thought: Disenfranchising Poor Watching",
    parent: "topic.MORALITY",
    tags: ['poor', 'minorities', 'watching', 'justice', 'morality'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.DISENFRANCHISING POOR WATCHING",
    ctype: "THOUGHT",
    en_title: "Disenfranchising Poor Watching",
    en_content: "To those that continue to disenfranchise the poor and minorities: GOD IS WATCHING.",
    es_title: "Dios Observa la Privación de Derechos de los Pobres",
    es_content: "A aquellos que continúan privando de derechos a los pobres y las minorías: DIOS ESTÁ OBSERVANDO.",
    fr_title: "Dieu Observe la Privation des Droits des Pauvres",
    fr_content: "À ceux qui continuent de priver de leurs droits les pauvres et les minorités : DIEU REGARDE.",
    hi_title: "गरीबों के अधिकार हनन को देख रहा परमेश्वर",
    hi_content: "उन लोगों के लिए जो गरीबों और अल्पसंख्यकों के अधिकारों का हनन करते रहते हैं: परमेश्वर देख रहा है।",
    zh_title: "Shén Zhèngzài Kànzhe Duóqǔ Qióngmín Quánlì",
    zh_content: "Duìyú nàxiē jìxù bōduó qióngmín hé shǎoshù mínzú quánlì de rén: SHÀNGDÌ ZHÈNGZÀI KÀNZHE."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DISENFRANCHISING POOR WATCHING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->DISENFRANCHISING POOR WATCHING"
RETURN t, parent;
```
