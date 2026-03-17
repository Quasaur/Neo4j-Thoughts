---
type: THOUGHT
name: "thought.EVOLUTION IS SCIENCE?"
alias: "Thought: Evolution is Science?"
parent: "topic.RELIGION"
en_content: "To equate science and evolution (considering the MOUNTAIN of evidence against evolution) would be premature, I think!"
tags: ["evolution", "science", "religion", "evidence", "faith"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.EVOLUTION IS SCIENCE?",
    alias: "Thought: Evolution is Science?",
    parent: "topic.RELIGION",
    tags: ["evolution", "science", "religion", "evidence", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVOLUTION IS SCIENCE?",
    ctype: "THOUGHT",
    en_title: "Evolution is Science?",
    en_content: "To equate science and evolution (considering the MOUNTAIN of evidence against evolution) would be premature, I think!",
    es_title: "¿LA EVOLUCIÓN ES CIENCIA?",
    es_content: "¡Creo que equiparar ciencia y evolución (teniendo en cuenta la MONTAÑA de evidencia contra la evolución) sería prematuro!",
    fr_title: "L'ÉVOLUTION EST-ELLE SCIENCE ?",
    fr_content: "Assumer science et évolution (compte tenu de la MONTAGNE de preuves contre l’évolution) serait prématuré, je pense !",
    hi_title: "विकास विज्ञान है?",
    hi_content: "मुझे लगता है कि विज्ञान और विकास को समान मानना ​​(विकास के विरुद्ध साक्ष्य के पहाड़ पर विचार करना) जल्दबाजी होगी!",
    zh_title: "jìn huà lùn shì kē xué ma ？",
    zh_content: "wǒ rèn wéi ， jiāng kē xué yǔ jìn huà lùn děng tóng qǐ lái （ kǎo lǜ dào fǎn duì jìn huà lùn de dà liàng zhèng jù ） hái wéi shí guò zǎo ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EVOLUTION IS SCIENCE?"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->EVOLUTION IS SCIENCE?"
RETURN t, parent;
```
