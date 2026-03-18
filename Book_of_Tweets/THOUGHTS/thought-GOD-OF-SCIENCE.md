---
type: THOUGHT
name: "thought.GOD OF SCIENCE"
alias: "Thought: God Of Science"
parent: "topic.THE GODHEAD"
en_content: "Jesus Christ is The God of Wisdom, Knowledge, Science and Technology."
tags: ["jesus", "science", "technology", "wisdom", "knowledge"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jun-2011a)
CREATE (t:THOUGHT {    name: "thought.GOD OF SCIENCE",
    alias: "Thought: God Of Science",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'science', 'technology', 'wisdom', 'knowledge'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD OF SCIENCE",
    ctype: "THOUGHT",
    en_title: "God Of Science",
    en_content: "Jesus Christ is The God of Wisdom, Knowledge, Science and Technology.",
    es_title: "Dios de la Ciencia",
    es_content: "Jesucristo es el Dios de la Sabiduría, el Conocimiento, la Ciencia y la Tecnología.",
    fr_title: "Dieu de la Science",
    fr_content: "Jésus-Christ est le Dieu de la Sagesse, de la Connaissance, de la Science et de la Technologie.",
    hi_title: "विज्ञान के परमेश्वर",
    hi_content: "यीशु मसीह बुद्धि, ज्ञान, विज्ञान और प्रौद्योगिकी के परमेश्वर हैं।",
    zh_title: "Kē Xué de Shàng Dì",
    zh_content: "Yē Sū Jī Dū shì Zhì Huì, Zhī Shi, Kē Xué hé Jì Shù de Shàng Dì."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD OF SCIENCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD OF SCIENCE"
RETURN t, parent;
```
