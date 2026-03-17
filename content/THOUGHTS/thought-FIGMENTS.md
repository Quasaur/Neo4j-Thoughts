---
type: THOUGHT
name: "thought.FIGMENTS"
alias: "Thought: Figments"
parent: "topic.CREATION"
tags: ["imagination", "fables", "lessreal", "fictitious", "created"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FIGMENTS",
    alias: "Thought: Figments",
    parent: "topic.CREATION",
    tags: ["imagination", "fables", "lessreal", "fictitious", "created"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FIGMENTS",
    ctype: "THOUGHT",
    en_title: "Figments",
    en_content: "",
    es_title: "FIGMENTOS",
    es_content: "Todos somos producto de la Imaginación Divina... ¡y qué Imaginación!",
    fr_title: "FIGURES",
    fr_content: "Nous sommes tous le produit de l’imagination divine – et quelle imagination !",
    hi_title: "चित्र",
    hi_content: "हम सभी दिव्य कल्पना की प्रतिमूर्ति हैं--और क्या कल्पना है!",
    zh_title: "rén wù",
    zh_content: "wǒ men dōu shì shén shèng xiǎng xiàng lì de xū gòu —— zhè shì duō me měi miào de xiǎng xiàng lì a ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FIGMENTS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->FIGMENTS"
RETURN t, parent;
```
