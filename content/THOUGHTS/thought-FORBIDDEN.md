---
type: THOUGHT
name: "thought.FORBIDDEN"
alias: "Thought: Forbidden"
parent: "topic.EVIL"
en_content: "What attracts us to the forbidden? It's forbidden!"
tags: ["prohibited", "restricted", "banned", "outlawed", "taboo"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FORBIDDEN",
    alias: "Thought: Forbidden",
    parent: "topic.EVIL",
    tags: ["prohibited", "restricted", "banned", "outlawed", "taboo"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FORBIDDEN",
    ctype: "THOUGHT",
    en_title: "Forbidden",
    en_content: "What attracts us to the forbidden? It's forbidden!",
    es_title: "Prohibido",
    es_content: "¿Qué nos atrae de lo prohibido? ¡Está prohibido!",
    fr_title: "Interdit",
    fr_content: "Pourquoi est-ce que l'interdit nous attire ? Parce que c'est interdit !",
    hi_title: "मना किया हुआ",
    hi_content: "हमें मना की हुई चीज़ों की तरफ़ क्या आकर्षित करता है? यह मना है!",
    zh_title: "Jìnjì",
    zh_content: "shì shénme xīyǐn wǒmen qù zhuīqiú jìnjì? Yīnwèi tā jìnjì!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FORBIDDEN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->FORBIDDEN"
RETURN t, parent;
```
