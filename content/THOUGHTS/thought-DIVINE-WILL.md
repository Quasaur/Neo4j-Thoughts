---
type: THOUGHT
name: "thought.DIVINE WILL"
alias: "Thought: Sovereignty of God's Will"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "Do you really believe that God has EVER done something He didn't want to do?"
tags: ["sovereignty", "gods_will", "omnipotence", "authority", "providence"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DIVINE WILL",
    alias: "Thought: Sovereignty of God's Will",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ["sovereignty", "gods_will", "omnipotence", "authority", "providence"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DIVINE WILL",
    ctype: "THOUGHT",
    en_title: "Divine Will",
    en_content: "Do you really believe that God has EVER done something He didn't want to do?",
    es_title: "VOLUNTAD DIVINA",
    es_content: "¿De verdad crees que Dios ha hecho ALGUNA VEZ algo que no quería hacer?",
    fr_title: "VOLONTÉ DIVINE",
    fr_content: "Croyez-vous vraiment que Dieu a JAMAIS fait quelque chose qu'il ne voulait pas faire ?",
    hi_title: "ईश्वरीय इच्छा",
    hi_content: "क्या आप वास्तव में मानते हैं कि ईश्वर ने कभी भी ऐसा कुछ किया है जो वह नहीं करना चाहता था?",
    zh_title: "shén dì yì zhì",
    zh_content: "nǐ zhēn de xiāng xìn shàng dì céng jīng zhuò guò tā bù xiǎng zhuò de shì ma ？"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DIVINE WILL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->DIVINE WILL"
RETURN t, parent;
```
