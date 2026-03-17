---
type: THOUGHT
name: "thought.AMERICAN"
alias: "Thought: American"
parent: "topic.POLITICAL SCIENCE"
tags: ["nationalism", "american", "addiction", "dependency", "codependency"]
ptopic: "[[topic-POLITICAL SCIENCE]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.AMERICAN",
    alias: "Thought: American",
    parent: "topic.POLITICAL SCIENCE",
    tags: ["nationalism", "american", "addiction", "dependency", "codependency"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.AMERICAN",
    ctype: "THOUGHT",
    en_title: "American",
    en_content: "",
    es_title: "AMERICANO",
    es_content: "No eres realmente estadounidense a menos que seas adicto a algo.",
    fr_title: "AMÉRICAIN",
    fr_content: "Vous n’êtes pas vraiment américain à moins d’être accro à quelque chose.",
    hi_title: "अमेरिकी",
    hi_content: "आप वास्तव में अमेरिकी नहीं हैं जब तक कि आप किसी चीज़ के आदी न हों।",
    zh_title: "měi guó rén",
    zh_content: "chú fēi nǐ duì mǒu jiàn shì shàng yǐn ， fǒu zé nǐ jiù bú shì zhēn zhèng de měi guó rén 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.AMERICAN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.POLITICAL-SCIENCE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.POLITICAL-SCIENCE->AMERICAN"
RETURN t, parent;
```
