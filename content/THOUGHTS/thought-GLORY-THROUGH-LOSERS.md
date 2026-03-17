---
type: THOUGHT
name: "thought.GLORY THROUGH LOSERS"
alias: "Thought: Glory Through Losers"
parent: "topic.GRACE"
en_content: "God prefers losers so that when we win God gets the glory!"
tags: ["grace", "glory", "humility", "weakness", "blessing"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GLORY THROUGH LOSERS",
    alias: "Thought: Glory Through Losers",
    parent: "topic.GRACE",
    tags: ['grace', 'glory', 'humility', 'weakness', 'blessing'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GLORY THROUGH LOSERS",
    ctype: "THOUGHT",
    en_title: "Glory Through Losers",
    en_content: "God prefers losers so that when we win God gets the glory!",
    es_title: "Gloria a Través de los Perdedores",
    es_content: "¡Dios prefiere a los perdedores para que cuando ganemos Dios reciba la gloria!",
    fr_title: "Gloire à Travers les Perdants",
    fr_content: "Dieu préfère les perdants pour que lorsque nous gagnons, Dieu reçoive la gloire !",
    hi_title: "हारने वालों के द्वारा महिमा",
    hi_content: "परमेश्वर हारने वालों को पसंद करता है ताकि जब हम जीतें तो परमेश्वर को महिमा मिले!",
    zh_title: "tōng guò shī bài zhě de róng yào",
    zh_content: "shàng dì xǐ huān shī bài zhě, zhè yàng dāng wǒ men dé shèng shí shàng dì jiù dé dào róng yào!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GLORY THROUGH LOSERS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->GLORY THROUGH LOSERS"
RETURN t, parent;
```
