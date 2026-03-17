---
type: THOUGHT
name: "thought.FORGIVING OTHERS PROBLEM"
alias: "Thought: Forgiving Others Problem"
parent: "topic.GRACE"
en_content: "If a person has received forgiveness from God for EVERY sin, why would they have a problem forgiving anyone else?"
tags: ["forgiveness", "grace", "character", "love", "peace"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FORGIVING OTHERS PROBLEM",
    alias: "Thought: Forgiving Others Problem",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'grace', 'character', 'love', 'peace'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FORGIVING OTHERS PROBLEM",
    ctype: "THOUGHT",
    en_title: "Forgiving Others Problem",
    en_content: "If a person has received forgiveness from God for EVERY sin, why would they have a problem forgiving anyone else?",
    es_title: "Problema de Perdonar a Otros",
    es_content: "Si una persona ha recibido el perdón de Dios por CADA pecado, ¿por qué tendría problemas para perdonar a cualquier otra persona?",
    fr_title: "Problème de Pardonner aux Autres",
    fr_content: "Si une personne a reçu le pardon de Dieu pour CHAQUE péché, pourquoi aurait-elle un problème à pardonner à quelqu'un d'autre?",
    hi_title: "दूसरों को क्षमा करने की समस्या",
    hi_content: "यदि किसी व्यक्ति को परमेश्वर से हर पाप के लिए क्षमा मिली है, तो वह किसी और को क्षमा करने में समस्या क्यों करेगा?",
    zh_title: "Kuangshu Taren Wenti",
    zh_content: "Ruguo yi ge ren yijing cong Shangdi dedao le dui mei yi ge zuie de kuangshu, weishenme ta hai hui zai kuangshu bieren shang you wenti ne?"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FORGIVING OTHERS PROBLEM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->FORGIVING OTHERS PROBLEM"
RETURN t, parent;
```
