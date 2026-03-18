---
type: THOUGHT
name: "thought.DANGEROUS AND SAFE"
alias: "Thought: Dangerous And Safe"
parent: "topic.THE GODHEAD"
en_content: "Who is more dangerous than God? Who is more safe than The Almighty?"
tags: ["god", "majesty", "safety", "danger", "power"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jan-2012c)
CREATE (t:THOUGHT {    name: "thought.DANGEROUS AND SAFE",
    alias: "Thought: Dangerous And Safe",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'majesty', 'safety', 'danger', 'power'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.DANGEROUS AND SAFE",
    ctype: "THOUGHT",
    en_title: "Dangerous And Safe",
    en_content: "Who is more dangerous than God? Who is more safe than The Almighty?",
    es_title: "Peligroso y Seguro",
    es_content: "¿Quién es más peligroso que Dios? ¿Quién es más seguro que El Todopoderoso?",
    fr_title: "Dangereux et Sûr",
    fr_content: "Qui est plus dangereux que Dieu ? Qui est plus sûr que le Tout-Puissant ?",
    hi_title: "खतरनाक और सुरक्षित",
    hi_content: "परमेश्वर से अधिक खतरनाक कौन है? सर्वशक्तिमान से अधिक सुरक्षित कौन है?",
    zh_title: "Wéixiǎn yǔ Ānquán",
    zh_content: "Shéi bǐ Shàngdì gèng wéixiǎn? Shéi bǐ Quánnéng Zhě gèng ānquán?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DANGEROUS AND SAFE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->DANGEROUS AND SAFE"
RETURN t, parent;
```
