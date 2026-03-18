---
type: THOUGHT
name: "thought.FULFILLING DESTINY TOGETHER"
alias: "Thought: Fulfilling Destiny Together"
parent: "topic.HUMANITY"
en_content: "I can only fulfill my destiny by assisting you in fulfilling yours."
tags: ["destiny", "help", "humanity", "purpose", "service"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2012a)
CREATE (t:THOUGHT {    name: "thought.FULFILLING DESTINY TOGETHER",
    alias: "Thought: Fulfilling Destiny Together",
    parent: "topic.HUMANITY",
    tags: ['destiny', 'help', 'humanity', 'purpose', 'service'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.FULFILLING DESTINY TOGETHER",
    ctype: "THOUGHT",
    en_title: "Fulfilling Destiny Together",
    en_content: "I can only fulfill my destiny by assisting you in fulfilling yours.",
    es_title: "Cumpliendo el Destino Juntos",
    es_content: "Solo puedo cumplir mi destino ayudándote a cumplir el tuyo.",
    fr_title: "Accomplir Notre Destinée Ensemble",
    fr_content: "Je ne peux accomplir ma destinée qu'en t'aidant à accomplir la tienne.",
    hi_title: "एक साथ भाग्य की पूर्ति",
    hi_content: "मैं अपनी नियति को केवल तभी पूरा कर सकता हूँ जब मैं तुम्हारी नियति पूरी करने में तुम्हारी सहायता करूँ।",
    zh_title: "Yìqǐ Shíxiàn Mìngyùn",
    zh_content: "Wǒ zhǐyǒu bāngzhù nǐ shíxiàn nǐ de mìngyùn, cáinéng shíxiàn wǒ de mìngyùn."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FULFILLING DESTINY TOGETHER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->FULFILLING DESTINY TOGETHER"
RETURN t, parent;
```
