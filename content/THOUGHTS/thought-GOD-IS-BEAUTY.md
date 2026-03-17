---
type: THOUGHT
name: "thought.GOD IS BEAUTY"
alias: "Thought: God Is Beauty"
parent: "topic.BEAUTY"
en_content: "God is Beauty. Apart from Him we are ugly."
tags: ["beauty", "aesthetics", "divinity", "holiness", "character"]
ptopic: "[[topic-BEAUTY]]"
level: 5
neo4j: false
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD IS BEAUTY",
    alias: "Thought: God Is Beauty",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'aesthetics', 'divinity', 'holiness', 'character'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.GOD IS BEAUTY",
    ctype: "THOUGHT",
    en_title: "God Is Beauty",
    en_content: "God is Beauty. Apart from Him we are ugly.",
    es_title: "Dios Es Belleza",
    es_content: "Dios es Belleza. Aparte de Él somos feos.",
    fr_title: "Dieu Est Beauté",
    fr_content: "Dieu est Beauté. En dehors de Lui nous sommes laids.",
    hi_title: "परमेश्वर सुंदरता है",
    hi_content: "परमेश्वर सुंदरता है। उसके अलावा हम कुरूप हैं।",
    zh_title: "Shàngdì shì měilì",
    zh_content: "Shàngdì shì měilì. Chúle tā zhīwài, wǒmen dōu shì chǒulòu de."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD IS BEAUTY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.BEAUTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.BEAUTY->GOD IS BEAUTY"
RETURN t, parent;
```
