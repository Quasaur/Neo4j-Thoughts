---
type: THOUGHT
name: "thought.ADOPTION"
alias: "Thought: Adoption"
parent: "topic.THE-GOSPEL"
tags: ["adoption", "abba", "father", "child_of_god", "everlasting"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ADOPTION",
    alias: "Thought: Adoption",
    parent: "topic.THE-GOSPEL",
    tags: ["adoption", "abba", "father", "child_of_god", "everlasting"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ADOPTION",
    ctype: "THOUGHT",
    en_title: "Adoption",
    en_content: "",
    es_title: "ADOPCIÓN",
    es_content: "Él es el Arquitecto del Cosmos y la Sede del Poder Absoluto... ¡y mi Papá!",
    fr_title: "ADOPTION",
    fr_content: "Il est l'architecte du cosmos et le siège du pouvoir absolu... et mon papa !",
    hi_title: "दत्तक ग्रहण",
    hi_content: "वह ब्रह्मांड के वास्तुकार और पूर्ण शक्ति के केंद्र हैं...और मेरे पिताजी!",
    zh_title: "cǎi yòng",
    zh_content: "tā shì yǔ zhòu de jiàn zhù shī hé jué duì quán lì de bǎo zuò …… hái yǒu wǒ de bà bà ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ADOPTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE-GOSPEL->ADOPTION"
RETURN t, parent;
```
