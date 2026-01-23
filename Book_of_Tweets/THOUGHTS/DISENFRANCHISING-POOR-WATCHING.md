---
name: "thought.DISENFRANCHISING POOR WATCHING"
alias: "Thought: Disenfranchising Poor Watching"
type: THOUGHT
en_content: "To those that continue to disenfranchise the poor and minorities: GOD IS WATCHING."
parent: "topic.MORALITY"
tags:
- poor
- minorities
- watching
- justice
- morality
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.DISENFRANCHISING POOR WATCHING",
    alias: "Thought: Disenfranchising Poor Watching",
    parent: "topic.MORALITY",
    tags: ['poor', 'minorities', 'watching', 'justice', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DISENFRANCHISING POOR WATCHING",
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

MATCH (t:THOUGHT {name: "thought.DISENFRANCHISING POOR WATCHING"})
MATCH (c:CONTENT {name: "content.DISENFRANCHISING POOR WATCHING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DISENFRANCHISING POOR WATCHING" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.DISENFRANCHISING POOR WATCHING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >DISENFRANCHISING POOR WATCHING" }]->(child);
```
