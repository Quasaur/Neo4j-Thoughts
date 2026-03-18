---
type: THOUGHT
name: "thought.COMPREHENDING VS KNOWING"
alias: "Thought: Comprehending Vs Knowing"
parent: "topic.THE GODHEAD"
en_content: "If I could comprehend Him, He wouldn't be God; but I can know Him."
tags: ["knowledge", "comprehension", "god", "divinity", "relationship"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2013a)
CREATE (t:THOUGHT {    name: "thought.COMPREHENDING VS KNOWING",
    alias: "Thought: Comprehending Vs Knowing",
    parent: "topic.THE GODHEAD",
    tags: ['knowledge', 'comprehension', 'god', 'divinity', 'relationship'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.COMPREHENDING VS KNOWING",
    ctype: "THOUGHT",
    en_title: "Comprehending Vs Knowing",
    en_content: "If I could comprehend Him, He wouldn't be God; but I can know Him.",
    es_title: "Comprender Versus Conocer",
    es_content: "Si pudiera comprenderlo, Él no sería Dios; pero puedo conocerlo.",
    fr_title: "Comprendre Contre Connaître",
    fr_content: "Si je pouvais Le comprendre, Il ne serait pas Dieu ; mais je peux Le connaître.",
    hi_title: "समझना बनाम जानना",
    hi_content: "अगर मैं उन्हें समझ सकता, तो वे परमेश्वर नहीं होते; लेकिन मैं उन्हें जान सकता हूं।",
    zh_title: "Lǐjiě Duìbǐ Rènshí",
    zh_content: "Rúguǒ wǒ néng lǐjiě Tā, Tā jiù bùshì Shàngdì; Dàn wǒ kěyǐ rènshí Tā."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.COMPREHENDING VS KNOWING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->COMPREHENDING VS KNOWING"
RETURN t, parent;
```
