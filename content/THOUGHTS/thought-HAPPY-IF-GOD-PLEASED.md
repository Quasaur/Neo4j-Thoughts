---
type: THOUGHT
name: "thought.HAPPY IF GOD PLEASED"
alias: "Thought: Happy If God Pleased"
parent: "topic.WORSHIP"
en_content: "How can I not be happy if God is pleased with me?"
tags: ["happiness", "pleasure", "god", "attitude"]
ptopic: "[[topic-WORSHIP]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HAPPY IF GOD PLEASED",
    alias: "Thought: Happy If God Pleased",
    parent: "topic.WORSHIP",
    tags: ['happiness', 'pleasure', 'god', 'attitude'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HAPPY IF GOD PLEASED",
    ctype: "THOUGHT",
    en_title: "Happy If God Pleased",
    en_content: "How can I not be happy if God is pleased with me?",
    es_title: "Feliz Si Dios Está Complacido",
    es_content: "¿Cómo no puedo estar feliz si Dios está complacido conmigo?",
    fr_title: "Heureux Si Dieu Est Satisfait",
    fr_content: "Comment ne puis-je pas être heureux si Dieu est satisfait de moi ?",
    hi_title: "खुश यदि भगवान प्रसन्न हैं",
    hi_content: "यदि भगवान मुझसे प्रसन्न हैं तो मैं कैसे खुश नहीं हो सकता?",
    zh_title: "Ruò Shén Xǐyuè Zé Kuàilè",
    zh_content: "Rúguǒ Shén duì wǒ mǎnyì, wǒ zěnme néng bù kuàilè ne?"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HAPPY IF GOD PLEASED"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WORSHIP"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WORSHIP->HAPPY IF GOD PLEASED"
RETURN t, parent;
```
