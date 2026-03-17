---
type: THOUGHT
name: "thought.BENEFICIARIES"
alias: "Thought: Beneficiaries"
parent: "topic.EVANGELISM"
tags: ["interpersonal", "encounter", "daily", "victims", "beneficiaries"]
ptopic: "[[topic-EVANGELISM]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.BENEFICIARIES",
    alias: "Thought: Beneficiaries",
    parent: "topic.EVANGELISM",
    tags: ["interpersonal", "encounter", "daily", "victims", "beneficiaries"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BENEFICIARIES",
    ctype: "THOUGHT",
    en_title: "Beneficiaries",
    en_content: "Those I encounter in my everyday life are either victims or beneficiaries of my relationship with God.",
    es_title: "BENEFICIARIOS",
    es_content: "Aquellos con los que me encuentro en mi vida diaria son víctimas o beneficiarios de mi relación con Dios.",
    fr_title: "BÉNÉFICIAIRES",
    fr_content: "Ceux que je rencontre dans ma vie quotidienne sont soit des victimes, soit des bénéficiaires de ma relation avec Dieu.",
    hi_title: "लाभार्थी नहीं",
    hi_content: "मैं अपने रोजमर्रा के जीवन में जिन लोगों से मिलता हूं वे या तो पीड़ित हैं या भगवान के साथ मेरे रिश्ते के लाभार्थी हैं।",
    zh_title: "shòu yì rén",
    zh_content: "wǒ zài rì cháng shēng huó zhōng yù dào de rén yào me shì wǒ yǔ shàng dì guān xì de shòu hài zhě ， yào me shì shòu yì zhě 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BENEFICIARIES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVANGELISM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVANGELISM->BENEFICIARIES"
RETURN t, parent;
```
