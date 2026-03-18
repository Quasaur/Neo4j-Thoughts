---
type: THOUGHT
name: "thought.DEFINING PORNOGRAPHY"
alias: "Thought: Defining Pornography"
parent: "topic.MORALITY"
en_content: "Matthew 5:27-30: Porn is adultery to a married man and fornication to a bachelor."
tags: ["morality", "purity", "adultery", "bible", "sin"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2011a)
CREATE (t:THOUGHT {    name: "thought.DEFINING PORNOGRAPHY",
    alias: "Thought: Defining Pornography",
    parent: "topic.MORALITY",
    tags: ['morality', 'purity', 'adultery', 'bible', 'sin'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.DEFINING PORNOGRAPHY",
    ctype: "THOUGHT",
    en_title: "Defining Pornography",
    en_content: "Matthew 5:27-30: Porn is adultery to a married man and fornication to a bachelor.",
    es_title: "Definiendo la Pornografía",
    es_content: "Mateo 5:27-30: La pornografía es adulterio para un hombre casado y fornicación para un soltero.",
    fr_title: "Définir la Pornographie",
    fr_content: "Matthieu 5:27-30: La pornographie est un adultère pour un homme marié et une fornication pour un célibataire.",
    hi_title: "अश्लीलता को परिभाषित करना",
    hi_content: "मत्ती 5:27-30: अश्लीलता विवाहित पुरुष के लिए व्यभिचार है और अविवाहित के लिए व्यभिचार है।",
    zh_title: "Ding Yi Se Qing Zuo Pin",
    zh_content: "Ma Tai Fu Yin 5:27-30: Se qing zuo pin dui yi ge yi hun nan ren lai shuo shi tong jian, dui yi ge dan shen nan ren lai shuo shi xing yin luan."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINING PORNOGRAPHY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->DEFINING PORNOGRAPHY"
RETURN t, parent;
```
