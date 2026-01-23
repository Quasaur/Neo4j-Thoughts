---
name: "thought.THE PRICE OF PROMISCUITY"
alias: "Thought: The Price Of Promiscuity"
type: THOUGHT
en_content: "People who are promiscuous wind up paying a terrible price."
parent: "topic.MORALITY"
tags:
- morality
- purity
- consequences
- society
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Nov-2011c)
CREATE (t:THOUGHT {
    name: "thought.THE PRICE OF PROMISCUITY",
    alias: "Thought: The Price Of Promiscuity",
    parent: "topic.MORALITY",
    tags: ['morality', 'purity', 'consequences', 'society', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.THE PRICE OF PROMISCUITY",
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

MATCH (t:THOUGHT {name: "thought.THE PRICE OF PROMISCUITY"})
MATCH (c:CONTENT {name: "content.THE PRICE OF PROMISCUITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE PRICE OF PROMISCUITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.THE PRICE OF PROMISCUITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >THE PRICE OF PROMISCUITY" }]->(child);
```
