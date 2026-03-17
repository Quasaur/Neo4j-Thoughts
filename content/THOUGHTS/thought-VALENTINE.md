---
type: THOUGHT
name: "thought.VALENTINE"
alias: "Thought: Valentine"
parent: "topic.PSYCHOLOGY"
tags: ["valentine", "couples", "romance", "relationships", "love"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.VALENTINE",
    alias: "Thought: Valentine",
    parent: "topic.PSYCHOLOGY",
    tags: ["valentine", "couples", "romance", "relationships", "love"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.VALENTINE",
    ctype: "THOUGHT",
    en_title: "Valentine",
    en_content: "",
    es_title: "ENAMORADO",
    es_content: "En este San Valentín me pregunto: ¿Cómo puedo evitar dar por sentado a mi esposa?
¿Por qué Dios escogió a esta mujer para mí?\\\"",
    fr_title: "VALENTIN",
    fr_content: "",
    hi_title: "प्रेमी",
    hi_content: "इस सेंट वैलेंटाइन दिवस पर मैं अपने आप से पूछता हूं \\\"मैं अपनी पत्नी को हल्के में लेने से कैसे बच सकता हूं?
भगवान ने मेरे लिए इस महिला को क्यों चुना?\\\"",
    zh_title: "qíng rén jié",
    zh_content: ""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.VALENTINE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->VALENTINE"
RETURN t, parent;
```
