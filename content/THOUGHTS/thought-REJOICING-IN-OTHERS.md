---
type: THOUGHT
name: "thought.REJOICING IN OTHERS"
alias: "Thought: Rejoicing In Others"
parent: "topic.LOVE"
en_content: "I rejoice in the achievements God accomplished in you as though He had accomplished them in me."
tags: ["joy", "character", "comparison", "attitude", "success"]
ptopic: "[[topic-LOVE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.REJOICING IN OTHERS",
    alias: "Thought: Rejoicing In Others",
    parent: "topic.LOVE",
    tags: ['joy', 'character', 'comparison', 'attitude', 'success'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.REJOICING IN OTHERS",
    ctype: "THOUGHT",
    en_title: "Rejoicing In Others",
    en_content: "I rejoice in the achievements God accomplished in you as though He had accomplished them in me.",
    es_title: "Regocijándose en Otros",
    es_content: "Me regocijo en los logros que Dios realizó en ti como si los hubiera realizado en mí.",
    fr_title: "Se Réjouir en Autrui",
    fr_content: "Je me réjouis des accomplissements que Dieu a réalisés en toi comme s'Il les avait accomplis en moi.",
    hi_title: "दूसरों में आनंदित होना",
    hi_content: "मैं उन उपलब्धियों में आनंदित होता हूँ जो परमेश्वर ने तुम में पूर्ण की हैं, जैसे कि उसने उन्हें मुझ में पूर्ण किया हो।",
    zh_title: "Zài Tārén Zhōng Xǐlè",
    zh_content: "Wǒ wèi Shàngdì zài nǐ shēnshang suǒ chéngjiù de shìqíng ér xǐlè, jiù hǎoxiàng Tā zài wǒ shēnshang chéngjiù le zhèxiē shìqíng yīyàng."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.REJOICING IN OTHERS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->REJOICING IN OTHERS"
RETURN t, parent;
```
