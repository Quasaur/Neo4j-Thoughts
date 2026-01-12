---
name: "thought.FIRST LOVE WAITING"
alias: "Thought: First Love Waiting"
type: THOUGHT
en_content: "Prayer is where my First Love is always waiting for me!"
parent: "topic.SPIRITUALITY"
tags:
- prayer
- love
- waiting
- spirituality
- relationship
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013h)
CREATE (t:THOUGHT {
    name: "thought.FIRST LOVE WAITING",
    alias: "Thought: First Love Waiting",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'love', 'waiting', 'spirituality', 'relationship'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FIRST LOVE WAITING",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FIRST LOVE WAITING" AND c.name = "content.FIRST LOVE WAITING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FIRST LOVE WAITING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.FIRST LOVE WAITING"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >FIRST LOVE WAITING" }]->(child);
```
