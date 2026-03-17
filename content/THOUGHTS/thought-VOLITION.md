---
type: THOUGHT
name: "thought.VOLITION"
alias: "Thought: Volition"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["paradox", "volition", "free_will", "fullness", "jesus_christ"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.VOLITION",
    alias: "Thought: Volition",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["paradox", "volition", "free_will", "fullness", "jesus_christ"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION",
    ctype: "THOUGHT",
    en_title: "Volition",
    en_content: "",
    es_title: "VOLUNTAD",
    es_content: "¡Tu voluntad nunca es más libre que cuando está bajo el control absoluto del Espíritu Santo de Jesucristo! 
Juan 14:11",
    fr_title: "VOLITION",
    fr_content: "Votre volonté n’est jamais plus libre que lorsqu’elle est sous le contrôle absolu du Saint-Esprit de Jésus-Christ ! 
Jean 14:11",
    hi_title: "इच्छाशक्ति",
    hi_content: "आपकी इच्छा कभी भी इससे अधिक स्वतंत्र नहीं होती जब यह यीशु मसीह की पवित्र आत्मा के पूर्ण नियंत्रण में होती है! 
यूहन्ना 14:11",
    zh_title: "yì zhì",
    zh_content: "dāng nǐ de yì zhì chǔ yú yē sū jī dū shèng líng de jué duì kòng zhì zhī xià shí ， nǐ de yì zhì shì zuì zì yóu de ！ 
 yuē hàn fú yīn  14:11"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.VOLITION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE-SOVEREIGNTY->VOLITION"
RETURN t, parent;
```
