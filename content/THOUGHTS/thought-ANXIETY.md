---
type: THOUGHT
name: "thought.ANXIETY"
alias: "Thought: Anxiety"
parent: "topic.FAITH"
tags: ["peace", "faith", "carefree", "confident", "trust"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ANXIETY",
    alias: "Thought: Anxiety",
    parent: "topic.FAITH",
    tags: ["peace", "faith", "carefree", "confident", "trust"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANXIETY",
    ctype: "THOUGHT",
    en_title: "Anxiety",
    en_content: "Don't worry...be obedient!",
    es_title: "ANSIEDAD",
    es_content: "No te preocupes... ¡sé obediente!",
    fr_title: "ANXIÉTÉ",
    fr_content: "Ne vous inquiétez pas... soyez obéissant !",
    hi_title: "चिंता",
    hi_content: "चिंता मत करो...आज्ञाकारी बनो!",
    zh_title: "jiāo lǜ",
    zh_content: "bié dān xīn …… tīng huà ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ANXIETY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FAITH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FAITH->ANXIETY"
RETURN t, parent;
```
