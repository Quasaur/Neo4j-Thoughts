---
type: THOUGHT
name: "thought.LOVING OR LOVED?"
alias: "Thought: Loving or Loved?"
parent: "topic.PSYCHOLOGY"
en_content: "So...which is better: loving God or being loved by God?"
tags: ["loving", "loved", "give", "receive", "preference"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LOVING OR LOVED?",
    alias: "Thought: Loving or Loved?",
    parent: "topic.PSYCHOLOGY",
    tags: ["loving", "loved", "give", "receive", "preference"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LOVING OR LOVED?",
    ctype: "THOUGHT",
    en_title: "Loving or Loved?",
    en_content: "So...which is better: loving God or being loved by God?",
    es_title: "¿AMAR O AMAR?",
    es_content: "Entonces... ¿qué es mejor: amar a Dios o ser amado por Dios?",
    fr_title: "AIMANT OU AIMÉ ?",
    fr_content: "Alors... qu'est-ce qui est mieux : aimer Dieu ou être aimé de Dieu ?",
    hi_title: "प्यार या प्यार?",
    hi_content: "तो...क्या बेहतर है: ईश्वर से प्रेम करना या ईश्वर द्वारा प्रेम किया जाना?",
    zh_title: "ài hái shì bèi ài ？",
    zh_content: "nà me …… nǎ ge gèng hǎo ： ài shén hái shì bèi shén ài ？"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOVING OR LOVED?"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->LOVING OR LOVED?"
RETURN t, parent;
```
