---
type: THOUGHT
name: "thought.DEFINE GRACE"
alias: "Thought: Define Grace"
parent: "topic.GRACE"
en_content: "GRACE is God saying \"I like you! I'm gonna cut you a break!\""
tags: ["grace", "mercy", "love", "salvation", "favor"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE GRACE",
    alias: "Thought: Define Grace",
    parent: "topic.GRACE",
    tags: ['grace', 'mercy', 'love', 'salvation', 'favor'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINE GRACE",
    ctype: "THOUGHT",
    en_title: "Define Grace",
    en_content: "GRACE is God saying \\\"I like you! I'm gonna cut you a break!\\\"",
    es_title: "Definir Gracia",
    es_content: "La GRACIA es Dios diciendo \\\"¡Me gustas! ¡Voy a darte un respiro!\\\"",
    fr_title: "",
    fr_content: "La GRÂCE est Dieu disant \\\"Je t'aime bien ! Je vais te donner une chance !\\\"",
    hi_title: "",
    hi_content: "अनुग्रह भगवान का कहना है \\\"मुझे तुम पसंद हो! मैं तुम्हें एक मौका दूंगा!\\\"",
    zh_title: "",
    zh_content: "Ēnhuì shì shàngdì shuō \\\"Wǒ xǐhuān nǐ! Wǒ yào gěi nǐ yīgè jīhuì!\\\""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE GRACE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->DEFINE GRACE"
RETURN t, parent;
```
