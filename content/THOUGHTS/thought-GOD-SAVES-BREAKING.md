---
type: THOUGHT
name: "thought.GOD SAVES BREAKING"
alias: "Thought: God Saves Breaking"
parent: "topic.GRACE"
en_content: "God will save you...after He breaks you. Matthew 21:44"
tags: ["salvation", "breaking", "grace", "god", "transformation"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD SAVES BREAKING",
    alias: "Thought: God Saves Breaking",
    parent: "topic.GRACE",
    tags: ['salvation', 'breaking', 'grace', 'god', 'transformation'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GOD SAVES BREAKING",
    ctype: "THOUGHT",
    en_title: "God Saves Breaking",
    en_content: "God will save you...after He breaks you. Matthew 21:44",
    es_title: "Dios Salva Quebrantando",
    es_content: "Dios te salvará...después de quebrantarte. Mateo 21:44",
    fr_title: "Dieu Sauve en Brisant",
    fr_content: "Dieu te sauvera...après t'avoir brisé. Matthieu 21:44",
    hi_title: "परमेश्वर तोड़कर बचाता है",
    hi_content: "परमेश्वर तुम्हें बचाएगा...तुम्हें तोड़ने के बाद। मत्ती 21:44",
    zh_title: "Shén Pòsuì Ér Zhěngjiù",
    zh_content: "Shén huì zhěngjiù nǐ...zài Tā pòsuì nǐ zhīhòu. Mǎtàifúyīn 21:44"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD SAVES BREAKING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->GOD SAVES BREAKING"
RETURN t, parent;
```
