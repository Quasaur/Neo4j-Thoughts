---
type: THOUGHT
name: "thought.FIRST LOVE WAITING"
alias: "Thought: First Love Waiting"
parent: "topic.SPIRITUALITY"
en_content: "Prayer is where my First Love is always waiting for me!"
tags: ["prayer", "love", "waiting", "spirituality", "relationship"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013h)
CREATE (t:THOUGHT {    name: "thought.FIRST LOVE WAITING",
    alias: "Thought: First Love Waiting",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'love', 'waiting', 'spirituality', 'relationship'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.FIRST LOVE WAITING",
    ctype: "THOUGHT",
    en_title: "First Love Waiting",
    en_content: "Prayer is where my First Love is always waiting for me!",
    es_title: "Primer Amor Esperando",
    es_content: "¡La oración es donde mi Primer Amor siempre me está esperando!",
    fr_title: "Premier Amour qui Attend",
    fr_content: "La prière est là où mon Premier Amour m'attend toujours !",
    hi_title: "प्रथम प्रेम प्रतीक्षा",
    hi_content: "प्रार्थना वह स्थान है जहाँ मेरा प्रथम प्रेम हमेशा मेरी प्रतीक्षा कर रहा है!",
    zh_title: "Chū Ài Děng Hòu",
    zh_content: "Dǎo gào shì wǒ de Chū Ài yǒng yuǎn zài děng dài wǒ de dì fāng!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FIRST LOVE WAITING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->FIRST LOVE WAITING"
RETURN t, parent;
```
