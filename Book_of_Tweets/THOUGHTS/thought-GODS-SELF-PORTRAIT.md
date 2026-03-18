---
type: THOUGHT
name: "thought.GODS SELF PORTRAIT"
alias: "Thought: Gods Self Portrait"
parent: "topic.THE GODHEAD"
en_content: "Jesus Christ is God's Self Portrait, etched on the canvas of humanity by the Holy Spirit."
tags: ["jesus", "christ", "portrait", "humanity", "holy_spirit"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jan-2012a)
CREATE (t:THOUGHT {    name: "thought.GODS SELF PORTRAIT",
    alias: "Thought: Gods Self Portrait",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'christ', 'portrait', 'humanity', 'holy_spirit'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GODS SELF PORTRAIT",
    ctype: "THOUGHT",
    en_title: "Gods Self Portrait",
    en_content: "Jesus Christ is God's Self Portrait, etched on the canvas of humanity by the Holy Spirit.",
    es_title: "El Autorretrato de Dios",
    es_content: "Jesucristo es el Autorretrato de Dios, grabado en el lienzo de la humanidad por el Espíritu Santo.",
    fr_title: "L'Autoportrait de Dieu",
    fr_content: "Jésus-Christ est l'Autoportrait de Dieu, gravé sur la toile de l'humanité par le Saint-Esprit.",
    hi_title: "परमेश्वर का स्वचित्र",
    hi_content: "यीशु मसीह परमेश्वर का स्वचित्र है, जो पवित्र आत्मा द्वारा मानवता के कैनवास पर अंकित किया गया है।",
    zh_title: "Shàngdì de Zìhuàxiàng",
    zh_content: "Yēsū Jīdū shì Shàngdì de Zìhuàxiàng, yóu Shènglíng kèhuà zài rénlèi de huàbù shàng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GODS SELF PORTRAIT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GODS SELF PORTRAIT"
RETURN t, parent;
```
