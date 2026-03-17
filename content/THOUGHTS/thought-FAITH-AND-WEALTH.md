---
type: THOUGHT
name: "thought.FAITH AND WEALTH"
alias: "Thought: Faith And Wealth"
parent: "topic.WEALTH"
en_content: "Faith is the closest we can get to free wealth."
tags: ["faith", "wealth", "spiritual_riches", "provision", "belief"]
ptopic: "[[topic-WEALTH]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FAITH AND WEALTH",
    alias: "Thought: Faith And Wealth",
    parent: "topic.WEALTH",
    tags: ["faith", "wealth", "spiritual_riches", "provision", "belief"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FAITH AND WEALTH",
    ctype: "THOUGHT",
    en_title: "Faith And Wealth",
    en_content: "Faith is the closest we can get to free wealth.",
    es_title: "Fe Y Riqueza",
    es_content: "La fe es lo más cerca que podemos llegar de la riqueza gratuita.",
    fr_title: "Foi Et Richesse",
    fr_content: "La foi est ce qui nous rapproche le plus de la richesse gratuite.",
    hi_title: "विश्वास और धन",
    hi_content: "विश्वास निःशुल्क धन के सबसे करीब हम पहुँच सकते हैं।",
    zh_title: "Xinyang Yu Caifu",
    zh_content: "Xinyang shi women zui jiejin mianfei caifu de fangshi."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FAITH AND WEALTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->FAITH AND WEALTH"
RETURN t, parent;
```
