---
type: THOUGHT
name: "thought.TERRIBLE SECRETS"
alias: "Thought: Terrible Secrets"
parent: "topic.PSYCHOLOGY"
en_content: "Secrets can be terrible things."
tags: ["secrets", "fear", "character", "attitude", "truth"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.TERRIBLE SECRETS",
    alias: "Thought: Terrible Secrets",
    parent: "topic.PSYCHOLOGY",
    tags: ['secrets', 'fear', 'character', 'attitude', 'truth'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TERRIBLE SECRETS",
    ctype: "THOUGHT",
    en_title: "Terrible Secrets",
    en_content: "Secrets can be terrible things.",
    es_title: "Secretos Terribles",
    es_content: "Los secretos pueden ser cosas terribles.",
    fr_title: "Secrets Terribles",
    fr_content: "Les secrets peuvent être des choses terribles.",
    hi_title: "भयानक रहस्य",
    hi_content: "रहस्य भयानक चीज़ें हो सकते हैं।",
    zh_title: "kě pà de mì mì",
    zh_content: "mì mì kě néng shì kě pà de shì qíng."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TERRIBLE SECRETS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->TERRIBLE SECRETS"
RETURN t, parent;
```
