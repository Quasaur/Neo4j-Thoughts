---
type: THOUGHT
name: "thought.POWER OF JESUS"
alias: "Thought: Power Of Jesus"
parent: "topic.THE GODHEAD"
en_content: "I have NEVER met anyone more powerful that Jesus...and I never will."
tags: ["jesus", "power", "divinity", "majesty", "lordship"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2010a)
CREATE (t:THOUGHT {    name: "thought.POWER OF JESUS",
    alias: "Thought: Power Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'power', 'divinity', 'majesty', 'lordship'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.POWER OF JESUS",
    ctype: "THOUGHT",
    en_title: "Power Of Jesus",
    en_content: "I have NEVER met anyone more powerful that Jesus...and I never will.",
    es_title: "El Poder de Jesús",
    es_content: "NUNCA he conocido a nadie más poderoso que Jesús... y nunca lo haré.",
    fr_title: "Le Pouvoir de Jésus",
    fr_content: "Je n'ai JAMAIS rencontré quelqu'un de plus puissant que Jésus... et je ne le ferai jamais.",
    hi_title: "यीशु की शक्ति",
    hi_content: "मैंने कभी यीशु से अधिक शक्तिशाली किसी से मुलाकात नहीं की... और न ही कभी करूंगा।",
    zh_title: "Yēsū de nénglì  yē sū de néng lì",
    zh_content: "Wǒ cónglái méiyǒu yùjiàn guò bǐ Yēsū gèng qiángdà de rén... wǒ yě yǒngyuǎn bù huì.  wǒ cóng lái méi yǒu yù jiàn guò bǐ yē sū gèng qiáng dà de rén ... wǒ yě yǒng yuǎn bú huì 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.POWER OF JESUS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->POWER OF JESUS"
RETURN t, parent;
```
