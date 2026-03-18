---
type: THOUGHT
name: "thought.HOME SWEET HOME"
alias: "Thought: Home, Sweet Home"
parent: "topic.THE-GOSPEL"
en_content: "GOD is my Home...and I am His!"
tags: ["home", "sweet", "safety", "fellowship", "godhead"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HOME SWEET HOME",
    alias: "Thought: Home, Sweet Home",
    parent: "topic.THE-GOSPEL",
    tags: ["home", "sweet", "safety", "fellowship", "godhead"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HOME SWEET HOME",
    ctype: "THOUGHT",
    en_title: "Home, Sweet Home",
    en_content: "GOD is my Home...and I am His!",
    es_title: "HOGAR DULCE HOGAR",
    es_content: "DIOS es mi Hogar...y yo soy Suyo!",
    fr_title: "HOME SWEET HOME",
    fr_content: "DIEU est ma Maison... et je suis la Sienne !",
    hi_title: "मेरा प्यारा घर",
    hi_content: "ईश्वर मेरा घर है...और मैं उसका हूँ!",
    zh_title: "jiā ， tián mì de jiā",
    zh_content: "shàng dì shì wǒ de jiā …… wǒ shì tā de ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HOME SWEET HOME"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GOSPEL->HOME SWEET HOME"
RETURN t, parent;
```
