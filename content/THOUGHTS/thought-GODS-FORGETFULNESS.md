---
type: THOUGHT
name: "thought.GODS FORGETFULNESS"
alias: "Thought: Gods Forgetfulness"
parent: "topic.GRACE"
en_content: "Don't bring to mind what God has decided to forget."
tags: ["forgiveness", "memory", "grace", "peace", "character"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GODS FORGETFULNESS",
    alias: "Thought: Gods Forgetfulness",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'memory', 'grace', 'peace', 'character'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GODS FORGETFULNESS",
    ctype: "THOUGHT",
    en_title: "Gods Forgetfulness",
    en_content: "Don't bring to mind what God has decided to forget.",
    es_title: "El Olvido de Dios",
    es_content: "No traigas a la mente lo que Dios ha decidido olvidar.",
    fr_title: "L'Oubli de Dieu",
    fr_content: "Ne rappelle pas à l'esprit ce que Dieu a décidé d'oublier.",
    hi_title: "परमेश्वर की विस्मृति",
    hi_content: "जिसे परमेश्वर ने भुलाने का निर्णय लिया है, उसे मन में न लाएं।",
    zh_title: "Shén de Yíwàng",
    zh_content: "Bùyào tí qǐ Shàngdì juédìng yíwàng de shìqíng."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GODS FORGETFULNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->GODS FORGETFULNESS"
RETURN t, parent;
```
