---
name: "thought.GODS SELF PORTRAIT"
alias: "Thought: Gods Self Portrait"
type: THOUGHT
en_content: "Jesus Christ is God's Self Portrait, etched on the canvas of humanity by the Holy Spirit."
parent: "topic.THE GODHEAD"
tags:
- jesus
- christ
- portrait
- humanity
- holyspirit
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jan-2012a)
CREATE (t:THOUGHT {
    name: "thought.GODS SELF PORTRAIT",
    alias: "Thought: Gods Self Portrait",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'christ', 'portrait', 'humanity', 'holyspirit'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS SELF PORTRAIT",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GODS SELF PORTRAIT" AND c.name = "content.GODS SELF PORTRAIT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS SELF PORTRAIT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS SELF PORTRAIT"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS SELF PORTRAIT" }]->(child);
```
