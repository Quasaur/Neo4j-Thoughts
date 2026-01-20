---
name: "thought.COMPREHENDING VS KNOWING"
alias: "Thought: Comprehending Vs Knowing"
type: THOUGHT
en_content: "If I could comprehend Him, He wouldn't be God; but I can know Him."
parent: "topic.THE GODHEAD"
tags:
- knowledge
- comprehension
- god
- divinity
- relationship
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.COMPREHENDING VS KNOWING",
    alias: "Thought: Comprehending Vs Knowing",
    parent: "topic.THE GODHEAD",
    tags: ['knowledge', 'comprehension', 'god', 'divinity', 'relationship'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.COMPREHENDING VS KNOWING",
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

MATCH (t:THOUGHT {name: "thought.COMPREHENDING VS KNOWING"})
MATCH (c:CONTENT {name: "content.COMPREHENDING VS KNOWING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.COMPREHENDING VS KNOWING" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.COMPREHENDING VS KNOWING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >COMPREHENDING VS KNOWING" }]->(child);
```
