---
type: THOUGHT
name: "thought.PERSEVERANCE"
alias: "Thought: Perseverance"
parent: "topic.ATTITUDE"
tags: ["persistence", "failure", "quitting", "consequence", "success"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PERSEVERANCE",
    alias: "Thought: Perseverance",
    parent: "topic.ATTITUDE",
    tags: ["persistence", "failure", "quitting", "consequence", "success"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PERSEVERANCE",
    ctype: "THOUGHT",
    en_title: "Perseverance",
    en_content: "",
    es_title: "PERSERVERANCIA",
    es_content: "El fracaso está asegurado para quien deja de intentarlo.",
    fr_title: "PERSÉVÉRANCE",
    fr_content: "L'échec est assuré à celui qui cesse d'essayer.",
    hi_title: "दृढ़ता",
    hi_content: "जो प्रयास करना बंद कर देता है, उसकी असफलता निश्चित है।",
    zh_title: "yì lì",
    zh_content: "duì yú tíng zhǐ cháng shì de rén lái shuō ， shī bài shì zhù dìng de 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PERSEVERANCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->PERSEVERANCE"
RETURN t, parent;
```
