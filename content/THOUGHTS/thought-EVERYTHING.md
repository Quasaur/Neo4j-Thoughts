---
type: THOUGHT
name: "thought.EVERYTHING"
alias: "Thought: Everything"
parent: "topic.CREATION"
tags: ["god", "creator", "all", "kingdom", "cosmos"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.EVERYTHING",
    alias: "Thought: Everything",
    parent: "topic.CREATION",
    tags: ["god", "creator", "all", "kingdom", "cosmos"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EVERYTHING",
    ctype: "THOUGHT",
    en_title: "Everything",
    en_content: "",
    es_title: "TODO",
    es_content: "¡Fue el Acto supremo de Humildad para Dios, que no necesita nada, para crearlo todo!",
    fr_title: "TOUT",
    fr_content: "C'était l'acte suprême d'humilité pour Dieu, qui n'a besoin de rien, pour tout créer !",
    hi_title: "सब कुछ",
    hi_content: "यह ईश्वर के लिए विनम्रता का सर्वोच्च कार्य था, जिसे सब कुछ बनाने के लिए किसी चीज़ की आवश्यकता नहीं है!",
    zh_title: "yī qiè",
    zh_content: "zhè shì shàng dì zuì gāo de qiān bēi xíng wéi ， tā bù xū yào rèn hé dōng xī ， jiù chuàng zào le yī qiè ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EVERYTHING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->EVERYTHING"
RETURN t, parent;
```
