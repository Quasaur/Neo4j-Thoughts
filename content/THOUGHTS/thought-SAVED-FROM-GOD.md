---
type: THOUGHT
name: "thought.SAVED FROM GOD"
alias: "Thought: Saved From God"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "God can save you from anybody...but who can save you from God?"
tags: ["salvation", "sovereignty", "power", "judgment", "mercy"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SAVED FROM GOD",
    alias: "Thought: Saved From God",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['salvation', 'sovereignty', 'power', 'judgment', 'mercy'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SAVED FROM GOD",
    ctype: "THOUGHT",
    en_title: "Saved From God",
    en_content: "God can save you from anybody...but who can save you from God?",
    es_title: "Salvado de Dios",
    es_content: "Dios puede salvarte de cualquiera...pero ¿quién puede salvarte de Dios?",
    fr_title: "Sauvé de Dieu",
    fr_content: "Dieu peut vous sauver de n'importe qui...mais qui peut vous sauver de Dieu ?",
    hi_title: "परमेश्वर से छुटकारा",
    hi_content: "परमेश्वर आपको किसी से भी बचा सकता है...लेकिन कौन आपको परमेश्वर से बचा सकता है?",
    zh_title: "Cóng Shàngdì Zhōng Déjiù",
    zh_content: "Shàngdì kěyǐ jiù nǐ tuōlí rènhé rén...dàn shuí néng jiù nǐ tuōlí Shàngdì ne?"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SAVED FROM GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->SAVED FROM GOD"
RETURN t, parent;
```
