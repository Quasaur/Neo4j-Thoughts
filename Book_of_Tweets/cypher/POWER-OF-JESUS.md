---
name: "thought.POWER OF JESUS"
alias: "Thought: Power Of Jesus"
type: THOUGHT
en_content: "I have NEVER met anyone more powerful that Jesus...and I never will."
parent: "topic.THE GODHEAD"
tags:
- jesus
- power
- divinity
- majesty
- lordship
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2010a)
CREATE (t:THOUGHT {
    name: "thought.POWER OF JESUS",
    alias: "Thought: Power Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'power', 'divinity', 'majesty', 'lordship'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.POWER OF JESUS",
    en_title: "Power Of Jesus",
    en_content: "I have NEVER met anyone more powerful that Jesus...and I never will.",
    es_title: "El Poder de Jesús",
    es_content: "NUNCA he conocido a nadie más poderoso que Jesús... y nunca lo haré.",
    fr_title: "Le Pouvoir de Jésus",
    fr_content: "Je n'ai JAMAIS rencontré quelqu'un de plus puissant que Jésus... et je ne le ferai jamais.",
    hi_title: "यीशु की शक्ति",
    hi_content: "मैंने कभी यीशु से अधिक शक्तिशाली किसी से मुलाकात नहीं की... और न ही कभी करूंगा।",
    zh_title: "Yēsū de nénglì 耶稣的能力",
    zh_content: "Wǒ cónglái méiyǒu yùjiàn guò bǐ Yēsū gèng qiángdà de rén... wǒ yě yǒngyuǎn bù huì. 我从来没有遇见过比耶稣更强大的人...我也永远不会。"
});

MATCH (t:THOUGHT {name: "thought.POWER OF JESUS"})
MATCH (c:CONTENT {name: "content.POWER OF JESUS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.POWER OF JESUS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.POWER OF JESUS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >POWER OF JESUS" }]->(child);
```
