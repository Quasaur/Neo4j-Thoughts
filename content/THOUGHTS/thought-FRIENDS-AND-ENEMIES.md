---
type: THOUGHT
name: "thought.FRIENDS AND ENEMIES"
alias: "Thought: Divine Design"
parent: "topic.CREATION"
en_content: "Something to think about: God created His friends AND His enemies!"
tags: ["creation", "purpose", "sovereignty", "relations", "divine_will"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FRIENDS AND ENEMIES",
    alias: "Thought: Divine Design",
    parent: "topic.CREATION",
    tags: ["creation", "purpose", "sovereignty", "relations", "divine_will"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FRIENDS AND ENEMIES",
    ctype: "THOUGHT",
    en_title: "Friends and Enemies",
    en_content: "Something to think about: God created His friends AND His enemies!",
    es_title: "Amigos y enemigos",
    es_content: "¡Dios creó a Sus amigos Y a Sus enemigos!",
    fr_title: "Amis et ennemis",
    fr_content: "Dieu a créé Ses amis ET Ses ennemis !",
    hi_title: "dost aur dushman",
    hi_content: "सोचने वाली बात: भगवान ने अपने दोस्तों और अपने दुश्मनों को बनाया!",
    zh_title: "péng yǒu hé dírén",
    zh_content: "zhí dé sī kǎo de shì : shàng dì chuàng zào le tā de péng yǒu, yě chuàng zào le tā de dírén!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FRIENDS AND ENEMIES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->FRIENDS AND ENEMIES"
RETURN t, parent;
```
