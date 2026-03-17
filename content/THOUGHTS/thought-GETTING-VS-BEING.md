---
type: THOUGHT
name: "thought.GETTING VS BEING"
alias: "Thought: Getting Vs Being"
parent: "topic.WISDOM"
en_content: "We are more concerned with GETTING more than we are BEING more."
tags: ["possession", "character", "getting", "being", "attitude"]
ptopic: "[[topic-WISDOM]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GETTING VS BEING",
    alias: "Thought: Getting Vs Being",
    parent: "topic.WISDOM",
    tags: ['possession', 'character', 'getting', 'being', 'attitude'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GETTING VS BEING",
    ctype: "THOUGHT",
    en_title: "Getting Vs Being",
    en_content: "We are more concerned with GETTING more than we are BEING more.",
    es_title: "Obtener Vs Ser",
    es_content: "Estamos más preocupados por OBTENER más de lo que estamos por SER más.",
    fr_title: "Obtenir Vs Être",
    fr_content: "Nous sommes plus préoccupés par OBTENIR plus que nous le sommes par ÊTRE plus.",
    hi_title: "पाना बनाम होना",
    hi_content: "हम अधिक पाने की चिंता में अधिक होने की चिंता से ज्यादा व्यस्त हैं।",
    zh_title: "Dedao Yu Chenwei",
    zh_content: "Women geng guanxin DEDAO gengduo, er bu shi CHENWEI gengduo."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GETTING VS BEING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->GETTING VS BEING"
RETURN t, parent;
```
