---
type: THOUGHT
name: "thought.CREATING SELFLESS HEART"
alias: "Thought: Creating Selfless Heart"
parent: "topic.THE GODHEAD"
en_content: "Only God can create a selfless heart from a pile of dust."
tags: ["heart", "transformation", "creation", "selfless", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Feb-2012a)
CREATE (t:THOUGHT {    name: "thought.CREATING SELFLESS HEART",
    alias: "Thought: Creating Selfless Heart",
    parent: "topic.THE GODHEAD",
    tags: ['heart', 'transformation', 'creation', 'selfless', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.CREATING SELFLESS HEART",
    ctype: "THOUGHT",
    en_title: "Creating Selfless Heart",
    en_content: "Only God can create a selfless heart from a pile of dust.",
    es_title: "Creando un Corazón Desinteresado",
    es_content: "Solo Dios puede crear un corazón desinteresado a partir de un montón de polvo.",
    fr_title: "Créer un Cœur Désintéressé",
    fr_content: "Seul Dieu peut créer un cœur désintéressé à partir d'un tas de poussière.",
    hi_title: "निःस्वार्थ हृदय बनाना",
    hi_content: "केवल परमेश्वर ही धूल के ढेर से एक निःस्वार्थ हृदय बना सकते हैं।",
    zh_title: "Chuàngzào wú sī zhī xīn  chuàng zào wú sī zhī xīn",
    zh_content: "Zhǐyǒu Shàngdì néng cóng chéntǔ zhōng chuàngzào chū yī kē wú sī de xīn.  zhǐ yǒu shàng dì néng cóng chén tǔ zhōng chuàng zào chū yī kē wú sī de xīn 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CREATING SELFLESS HEART"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->CREATING SELFLESS HEART"
RETURN t, parent;
```
