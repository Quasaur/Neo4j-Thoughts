---
type: THOUGHT
name: "thought.GORGEOUS DIVINITY"
alias: "Thought: Gorgeous Divinity"
parent: "topic.BEAUTY"
en_content: "God is overwhelmingly gorgeous...both inside and out!"
tags: ["beauty", "aesthetics", "holiness", "character", "divinity"]
ptopic: "[[topic-BEAUTY]]"
level: 5
neo4j: false
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GORGEOUS DIVINITY",
    alias: "Thought: Gorgeous Divinity",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'aesthetics', 'holiness', 'character', 'divinity'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.GORGEOUS DIVINITY",
    ctype: "THOUGHT",
    en_title: "Gorgeous Divinity",
    en_content: "God is overwhelmingly gorgeous...both inside and out!",
    es_title: "Divinidad Hermosa",
    es_content: "¡Dios es abrumadoramente hermoso...tanto por dentro como por fuera!",
    fr_title: "Divinité Magnifique",
    fr_content: "Dieu est d'une beauté écrasante...à l'intérieur comme à l'extérieur !",
    hi_title: "भव्य दिव्यता",
    hi_content: "परमेश्वर अत्यंत सुंदर है...अंदर और बाहर दोनों तरफ से!",
    zh_title: "huáměi de shénxìng",
    zh_content: "Shàngdì shì yāo rén de měilì...nèizài hé wàizài dōu shì!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GORGEOUS DIVINITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.BEAUTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.BEAUTY->GORGEOUS DIVINITY"
RETURN t, parent;
```
