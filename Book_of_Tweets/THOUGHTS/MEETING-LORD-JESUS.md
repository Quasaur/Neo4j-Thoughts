---
name: "thought.MEETING LORD JESUS"
alias: "Thought: Meeting Lord Jesus"
type: THOUGHT
en_content: "I have met the Lord Jesus: He is to live for, and to die for!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- commitment
- life
- death
- faith
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.MEETING LORD JESUS",
    alias: "Thought: Meeting Lord Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'commitment', 'life', 'death', 'faith'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MEETING LORD JESUS",
    en_title: "Meeting Lord Jesus",
    en_content: "I have met the Lord Jesus: He is to live for, and to die for!",
    es_title: "Conociendo al Señor Jesús",
    es_content: "He encontrado al Señor Jesús: ¡Él debe vivir y morir por Él!",
    fr_title: "Rencontrer le Seigneur Jésus",
    fr_content: "J'ai rencontré le Seigneur Jésus : il faut vivre et mourir !",
    hi_title: "प्रभु यीशु से मुलाकात",
    hi_content: "मैं प्रभु यीशु से मिल चुका हूँ: उसके लिए जीना है, और उसके लिए मरना है!",
    zh_title: "yù jiàn zhǔ yē sū",
    zh_content: "wǒ yù jiàn le zhǔ yē sū ： wèi tā ér shēng ， wèi tā ér sǐ ！"
});

MATCH (t:THOUGHT {name: "thought.MEETING LORD JESUS"})
MATCH (c:CONTENT {name: "content.MEETING LORD JESUS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.MEETING LORD JESUS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.MEETING LORD JESUS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->MEETING LORD JESUS" }]->(child);
```
