---
type: THOUGHT
name: "thought.WANTING LOVE ONLY"
alias: "Thought: Wanting Love Only"
parent: "topic.LOVE"
en_content: "We want to be loved, but we don't want to love...how pathetic."
tags: ["love", "selfishness", "attitude", "pathetic", "character"]
ptopic: "[[topic-LOVE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.WANTING LOVE ONLY",
    alias: "Thought: Wanting Love Only",
    parent: "topic.LOVE",
    tags: ['love', 'selfishness', 'attitude', 'pathetic', 'character'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WANTING LOVE ONLY",
    ctype: "THOUGHT",
    en_title: "Wanting Love Only",
    en_content: "We want to be loved, but we don't want to love...how pathetic.",
    es_title: "Solo Querer Ser Amado",
    es_content: "Queremos ser amados, pero no queremos amar... qué patético.",
    fr_title: "Vouloir Être Aimé Seulement",
    fr_content: "Nous voulons être aimés, mais nous ne voulons pas aimer... comme c'est pathétique.",
    hi_title: "केवल प्यार पाना चाहना",
    hi_content: "हम प्यार पाना चाहते हैं, लेकिन हम प्यार करना नहीं चाहते... कितना दयनीय है।",
    zh_title: "Zhǐ xiǎng bèi ài 只想被爱",
    zh_content: "Wǒmen xiǎng bèi ài, dàn wǒmen bù xiǎng ài rén... zhēn kělǐan. 我们想被爱，但我们不想爱人...真可怜。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WANTING LOVE ONLY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->WANTING LOVE ONLY"
RETURN t, parent;
```
