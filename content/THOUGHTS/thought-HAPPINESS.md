---
type: THOUGHT
name: "thought.HAPPINESS"
alias: "Thought: Happiness"
parent: "topic.ATTITUDE"
tags: ["happy", "fulfilled", "satisfied", "delighted", "content"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HAPPINESS",
    alias: "Thought: Happiness",
    parent: "topic.ATTITUDE",
    tags: ["happy", "fulfilled", "satisfied", "delighted", "content"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HAPPINESS",
    ctype: "THOUGHT",
    en_title: "Happiness",
    en_content: "",
    es_title: "FELICIDAD",
    es_content: "LA FELICIDAD no es producto de hacer lo que quieres...
...sino de hacer lo CORRECTO.",
    fr_title: "BONHEUR",
    fr_content: "LE BONHEUR n'est pas le produit du fait de faire ce que l'on veut...
... mais de faire ce qui est BIEN.",
    hi_title: "ख़ुशी",
    hi_content: "ख़ुशी वह करने का परिणाम नहीं है जो आप चाहते हैं...
...लेकिन वही करना जो सही है।",
    zh_title: "xìng fú",
    zh_content: "xìng fú bú shì zuò nǐ xiǎng zuò de shì de jié guǒ ......
... ér shì zuò zhèng què de shì 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HAPPINESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->HAPPINESS"
RETURN t, parent;
```
