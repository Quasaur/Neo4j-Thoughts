---
name: "thought.DEFINE EXQUISITAGIOUS"
alias: "Thought: Define Exquisitagious"
type: THOUGHT
en_content: "New Word: exquisitagious Meaning: something so exquisite that the feeling's contagious!"
parent: "topic.BEAUTY"
tags:
- beauty
- language
- humor
- contagious
- aesthetics
level: 5
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jan-2012d)
CREATE (t:THOUGHT {
    name: "thought.DEFINE EXQUISITAGIOUS",
    alias: "Thought: Define Exquisitagious",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'language', 'humor', 'contagious', 'aesthetics'],
    notes: "",
    level: 5
});

CREATE (c:CONTENT {
    name: "content.DEFINE EXQUISITAGIOUS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEFINE EXQUISITAGIOUS" AND c.name = "content.DEFINE EXQUISITAGIOUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE EXQUISITAGIOUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.DEFINE EXQUISITAGIOUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "BEAUTY >DEFINE EXQUISITAGIOUS" }]->(child);
```
