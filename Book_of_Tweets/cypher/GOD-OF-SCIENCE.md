---
name: "thought.GOD OF SCIENCE"
alias: "Thought: God Of Science"
type: THOUGHT
en_content: "Jesus Christ is The God of Wisdom, Knowledge, Science and Technology."
parent: "topic.THE GODHEAD"
tags:
- jesus
- science
- technology
- wisdom
- knowledge
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jun-2011a)
CREATE (t:THOUGHT {
    name: "thought.GOD OF SCIENCE",
    alias: "Thought: God Of Science",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'science', 'technology', 'wisdom', 'knowledge'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD OF SCIENCE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD OF SCIENCE" AND c.name = "content.GOD OF SCIENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD OF SCIENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD OF SCIENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD OF SCIENCE" }]->(child);
```
