---
name: "thought.CREATING SELFLESS HEART"
alias: "Thought: Creating Selfless Heart"
type: THOUGHT
en_content: "Only God can create a selfless heart from a pile of dust."
parent: "topic.THE GODHEAD"
tags:
- heart
- transformation
- creation
- selfless
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.CREATING SELFLESS HEART",
    alias: "Thought: Creating Selfless Heart",
    parent: "topic.THE GODHEAD",
    tags: ['heart', 'transformation', 'creation', 'selfless', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CREATING SELFLESS HEART",
    en_title: "Creating Selfless Heart",
    en_content: "Only God can create a selfless heart from a pile of dust.",
    es_title: "Creando un Corazón Desinteresado",
    es_content: "Solo Dios puede crear un corazón desinteresado a partir de un montón de polvo.",
    fr_title: "Créer un Cœur Désintéressé",
    fr_content: "Seul Dieu peut créer un cœur désintéressé à partir d'un tas de poussière.",
    hi_title: "निःस्वार्थ हृदय बनाना",
    hi_content: "केवल परमेश्वर ही धूल के ढेर से एक निःस्वार्थ हृदय बना सकते हैं।",
    zh_title: "Chuàngzào wú sī zhī xīn 创造无私之心",
    zh_content: "Zhǐyǒu Shàngdì néng cóng chéntǔ zhōng chuàngzào chū yī kē wú sī de xīn. 只有上帝能从尘土中创造出一颗无私的心。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CREATING SELFLESS HEART" AND c.name = "content.CREATING SELFLESS HEART"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CREATING SELFLESS HEART" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.CREATING SELFLESS HEART"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CREATING SELFLESS HEART" }]->(child);
```
