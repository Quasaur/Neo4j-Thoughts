---
type: THOUGHT
name: "thought.CAT LICK NECK"
alias: "Thought: Cat Lick Neck"
parent: "topic.BIOLOGY"
en_content: "My cat can lick its own neck...God is great!"
tags: ["creation", "nature", "design", "cat", "humor"]
ptopic: "[[topic-BIOLOGY]]"
level: 6
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.CAT LICK NECK",
    alias: "Thought: Cat Lick Neck",
    parent: "topic.BIOLOGY",
    tags: ['creation', 'nature', 'design', 'cat', 'humor'],
    level: 6
});

CREATE (c:CONTENT {
    name: "content.CAT LICK NECK",
    ctype: "THOUGHT",
    en_title: "Cat Lick Neck",
    en_content: "My cat can lick its own neck...God is great!",
    es_title: "El Gato Lame su Cuello",
    es_content: "Mi gato puede lamerse su propio cuello... ¡Dios es grande!",
    fr_title: "Le Chat Lèche son Cou",
    fr_content: "Mon chat peut lécher son propre cou... Dieu est grand !",
    hi_title: "बिल्ली अपनी गर्दन चाटती है",
    hi_content: "मेरी बिल्ली अपनी गर्दन चाट सकती है... भगवान महान हैं!",
    zh_title: "Māo Tiǎn Bózi",
    zh_content: "Wǒ de māo kěyǐ tiǎn zìjǐ de bózi... Shàngdì shì wěidà de!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CAT LICK NECK"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.BIOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.BIOLOGY->CAT LICK NECK"
RETURN t, parent;
```
