---
type: THOUGHT
name: "thought.MURDER"
alias: "Thought: Murder"
parent: "topic.PSYCHOLOGY"
tags: ["crime", "punishment", "intent", "kill", "judgment"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.MURDER",
    alias: "Thought: Murder",
    parent: "topic.PSYCHOLOGY",
    tags: ["crime", "punishment", "intent", "kill", "judgment"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MURDER",
    ctype: "THOUGHT",
    en_title: "Murder",
    en_content: "",
    es_title: "ASESINATO",
    es_content: "Si tienes edad suficiente para asesinar con intención, tienes edad suficiente para ser ejecutado con prejuicios extremos.",
    fr_title: "MEURTRE",
    fr_content: "Si vous êtes assez vieux pour commettre un meurtre intentionnel, vous êtes assez vieux pour être exécuté avec des préjugés extrêmes.",
    hi_title: "हत्या",
    hi_content: "यदि आप इरादे से हत्या करने के लिए पर्याप्त बूढ़े हैं, तो आप अत्यधिक पूर्वाग्रह के साथ मारे जाने के लिए भी काफी बूढ़े हैं।",
    zh_title: "móu shā",
    zh_content: "rú guǒ nǐ yǐ jīng dào le kě yǐ xù yì móu shā de nián jì ， nà me nǐ yě yǐ jīng dào le kě yǐ dài zhe jí duān piān jiàn bèi chǔ jué de nián jì le 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MURDER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->MURDER"
RETURN t, parent;
```
