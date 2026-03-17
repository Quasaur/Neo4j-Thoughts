---
type: THOUGHT
name: "thought.DEFINE EXQUISITAGIOUS"
alias: "Thought: Define Exquisitagious"
parent: "topic.LINGUISTICS"
en_content: "New Word: exquisitagious Meaning: something so exquisite that the feeling's contagious!"
tags: ["beauty", "language", "humor", "contagious", "aesthetics"]
ptopic: "[[topic-LINGUISTICS]]"
level: 5
neo4j: false
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE EXQUISITAGIOUS",
    alias: "Thought: Define Exquisitagious",
    parent: "topic.LINGUISTICS",
    tags: ['beauty', 'language', 'humor', 'contagious', 'aesthetics'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.DEFINE EXQUISITAGIOUS",
    ctype: "THOUGHT",
    en_title: "Define Exquisitagious",
    en_content: "New Word: exquisitagious Meaning: something so exquisite that the feeling's contagious!",
    es_title: "Definir Exquisitagioso",
    es_content: "Nueva Palabra: exquisitagioso Significado: ¡algo tan exquisito que el sentimiento es contagioso!",
    fr_title: "Définir Exquisitagieux",
    fr_content: "Nouveau Mot : exquisitagieux Signification : quelque chose de si exquis que le sentiment est contagieux !",
    hi_title: "एक्सक्विसिटागियस को परिभाषित करें",
    hi_content: "नया शब्द: एक्सक्विसिटागियस अर्थ: कुछ इतना उत्कृष्ट कि भावना संक्रामक है!",
    zh_title: "Dìngyì jīngzhì de",
    zh_content: "Xīn cí: Jīngzhì de Yìsi: Mǒu wù rúcǐ jīngzhì, gǎnqíng jiù chuánrǎn!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE EXQUISITAGIOUS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LINGUISTICS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LINGUISTICS->DEFINE EXQUISITAGIOUS"
RETURN t, parent;
```
