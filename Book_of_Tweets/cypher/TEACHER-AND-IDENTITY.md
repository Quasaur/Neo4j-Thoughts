---
name: "thought.TEACHER AND IDENTITY"
alias: "Thought: Teacher And Identity"
type: THOUGHT
en_content: "A teacher challenges your identity and your knowledge, then helps you discover both so that you can stand strong under pressure."
parent: "topic.WISDOM"
tags:
- wisdom
- teaching
- identity
- growth
- knowledge
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.TEACHER AND IDENTITY",
    alias: "Thought: Teacher And Identity",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'teaching', 'identity', 'growth', 'knowledge'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TEACHER AND IDENTITY",
    en_title: "Teacher And Identity",
    en_content: "A teacher challenges your identity and your knowledge, then helps you discover both so that you can stand strong under pressure.",
    es_title: "Maestro E Identidad",
    es_content: "Un maestro desafía tu identidad y tu conocimiento, luego te ayuda a descubrir ambos para que puedas mantenerte firme bajo presión.",
    fr_title: "Maître Et Identité",
    fr_content: "Un maître défie votre identité et votre connaissance, puis vous aide à découvrir les deux afin que vous puissiez rester ferme sous la pression.",
    hi_title: "शिक्षक और पहचान",
    hi_content: "एक शिक्षक आपकी पहचान और आपके ज्ञान को चुनौती देता है, फिर दोनों की खोज करने में आपकी सहायता करता है ताकि आप दबाव में मजबूत खड़े रह सकें।",
    zh_title: "Lǎoshī Yǔ Shēnfèn",
    zh_content: "Lǎoshī tiǎozhàn nǐ de shēnfèn hé nǐ de zhīshi, ránhòu bāngzhù nǐ fāxiàn zhè liǎng zhě, shǐ nǐ néng zài yālì xià jiānqiáng dìzhù."
});

MATCH (t:THOUGHT {name: "thought.TEACHER AND IDENTITY"})
MATCH (c:CONTENT {name: "content.TEACHER AND IDENTITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.TEACHER AND IDENTITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.WISDOM"})
MATCH (child:THOUGHT {name: "thought.TEACHER AND IDENTITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >TEACHER AND IDENTITY" }]->(child);
```
