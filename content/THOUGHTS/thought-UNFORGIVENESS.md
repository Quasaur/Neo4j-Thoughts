---
type: THOUGHT
name: "thought.UNFORGIVENESS"
alias: "Thought: Unforgiveness"
parent: "topic.ATTITUDE"
tags: ["unforgiveness", "hell", "unmerciful", "condemnation", "salvation"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.UNFORGIVENESS",
    alias: "Thought: Unforgiveness",
    parent: "topic.ATTITUDE",
    tags: ["unforgiveness", "hell", "unmerciful", "condemnation", "salvation"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNFORGIVENESS",
    ctype: "THOUGHT",
    en_title: "Unforgiveness",
    en_content: "",
    es_title: "PERDÓN",
    es_content: "¡Las ÚNICAS personas que van al infierno son aquellas que NO PODRÍAN PERDONAR!",
    fr_title: "IMPARDONNANCE",
    fr_content: "Les SEULS gens qui vont en Enfer sont ceux qui NE PEUVENT PAS PARDONNER !",
    hi_title: "क्षमा न करना",
    hi_content: "नर्क में जाने वाले केवल वही लोग हैं जो क्षमा नहीं कर सकते!",
    zh_title: "bù kě ráo shù",
    zh_content: "wéi yī xià dì yù de rén jiù shì nà xiē wú fǎ kuān shù de rén ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNFORGIVENESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->UNFORGIVENESS"
RETURN t, parent;
```
