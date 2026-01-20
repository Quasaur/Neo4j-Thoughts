---
name: "thought.DANGEROUS AND SAFE"
alias: "Thought: Dangerous And Safe"
type: THOUGHT
en_content: "Who is more dangerous than God? Who is more safe than The Almighty?"
parent: "topic.THE GODHEAD"
tags:
- god
- majesty
- safety
- danger
- power
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jan-2012c)
CREATE (t:THOUGHT {
    name: "thought.DANGEROUS AND SAFE",
    alias: "Thought: Dangerous And Safe",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'majesty', 'safety', 'danger', 'power'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.DANGEROUS AND SAFE",
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

MATCH (t:THOUGHT {name: "thought.DANGEROUS AND SAFE"})
MATCH (c:CONTENT {name: "content.DANGEROUS AND SAFE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DANGEROUS AND SAFE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.DANGEROUS AND SAFE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >DANGEROUS AND SAFE" }]->(child);
```
