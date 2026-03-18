---
type: THOUGHT
name: "thought.THE PRICE OF PROMISCUITY"
alias: "Thought: The Price Of Promiscuity"
parent: "topic.MORALITY"
en_content: "People who are promiscuous wind up paying a terrible price."
tags: ["morality", "purity", "consequences", "society", "character"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Nov-2011c)
CREATE (t:THOUGHT {    name: "thought.THE PRICE OF PROMISCUITY",
    alias: "Thought: The Price Of Promiscuity",
    parent: "topic.MORALITY",
    tags: ['morality', 'purity', 'consequences', 'society', 'character'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.THE PRICE OF PROMISCUITY",
    ctype: "THOUGHT",
    en_title: "The Price Of Promiscuity",
    en_content: "People who are promiscuous wind up paying a terrible price.",
    es_title: "El Precio de la Promiscuidad",
    es_content: "Las personas que son promiscuas terminan pagando un precio terrible.",
    fr_title: "Le Prix de la Promiscuité",
    fr_content: "Les personnes qui sont promiscues finissent par payer un prix terrible.",
    hi_title: "व्यभिचार की कीमत",
    hi_content: "जो लोग व्यभिचारी होते हैं, वे अंततः भयानक कीमत चुकाते हैं।",
    zh_title: "Fàngdàng de Dàijià",
    zh_content: "Fàngdàng bùjiǎn de rén zuìzhōng huì fùchū kěpà de dàijià."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.THE PRICE OF PROMISCUITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->THE PRICE OF PROMISCUITY"
RETURN t, parent;
```
