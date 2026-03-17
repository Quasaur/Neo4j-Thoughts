---
type: THOUGHT
name: "thought.ARROGANCE VS DIGNITY"
alias: "Thought: Arrogance Vs Dignity"
parent: "topic.ATTITUDE"
en_content: "Far too many black men have mistaken arrogance for dignity."
tags: ["dignity", "arrogance", "humanity", "character", "race"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ARROGANCE VS DIGNITY",
    alias: "Thought: Arrogance Vs Dignity",
    parent: "topic.ATTITUDE",
    tags: ['dignity', 'arrogance', 'humanity', 'character', 'race'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ARROGANCE VS DIGNITY",
    ctype: "THOUGHT",
    en_title: "Arrogance Vs Dignity",
    en_content: "Far too many black men have mistaken arrogance for dignity.",
    es_title: "Arrogancia vs Dignidad",
    es_content: "Demasiados hombres negros han confundido la arrogancia con la dignidad.",
    fr_title: "Arrogance vs Dignité",
    fr_content: "Beaucoup trop d'hommes noirs ont confondu l'arrogance avec la dignité.",
    hi_title: "अहंकार बनाम गरिमा",
    hi_content: "बहुत से अश्वेत पुरुषों ने अहंकार को गरिमा समझ लिया है।",
    zh_title: "Àomàn yǔ zūnyán",
    zh_content: "Tài duō hēirén nánxìng jiāng àomàn wù rènwéi shì zūnyán."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ARROGANCE VS DIGNITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->ARROGANCE VS DIGNITY"
RETURN t, parent;
```
