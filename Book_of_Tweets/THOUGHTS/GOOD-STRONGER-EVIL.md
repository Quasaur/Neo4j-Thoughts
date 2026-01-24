---
name: "thought.GOOD STRONGER EVIL"
alias: "Thought: Good Stronger Evil"
type: THOUGHT
en_content: "Jesus PROVED that Good is stronger than Evil...that Righteousness is MORE POWERFUL than Sin!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- victory
- evil
- goodness
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.GOOD STRONGER EVIL",
    alias: "Thought: Good Stronger Evil",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'victory', 'evil', 'goodness', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOOD STRONGER EVIL",
    en_title: "Good Stronger Evil",
    en_content: "Jesus PROVED that Good is stronger than Evil...that Righteousness is MORE POWERFUL than Sin!",
    es_title: "El Bien es Más Fuerte que el Mal",
    es_content: "Jesús DEMOSTRÓ que el Bien es más fuerte que el Mal...¡que la Justicia es MÁS PODEROSA que el Pecado!",
    fr_title: "Le Bien Plus Fort que le Mal",
    fr_content: "Jésus a PROUVÉ que le Bien est plus fort que le Mal...que la Droiture est PLUS PUISSANTE que le Péché !",
    hi_title: "अच्छाई बुराई से श्रेष्ठ",
    hi_content: "यीशु ने सिद्ध किया कि अच्छाई बुराई से श्रेष्ठ है...कि धार्मिकता पाप से अधिक शक्तिशाली है!",
    zh_title: "Shan E Sheng E",
    zh_content: "Yesu ZHENGMING le Shan bi E geng qiangda...Gongyi bi Zuie geng you LILIANG!"
});

MATCH (t:THOUGHT {name: "thought.GOOD STRONGER EVIL"})
MATCH (c:CONTENT {name: "content.GOOD STRONGER EVIL"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOOD STRONGER EVIL" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOOD STRONGER EVIL"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GOOD STRONGER EVIL" }]->(child);
```
