---
name: "thought.THREE TYPES OF HUMANITY"
alias: "Thought: Three Types Of Humanity"
type: THOUGHT
en_content: "Humanity: (1) those who place God 1st; (2) those who give God a priority other than 1st; (3) those who give God no priority at all."
parent: "topic.HUMANITY"
tags:
- humanity
- priority
- god
- world
- classification
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.THREE TYPES OF HUMANITY",
    alias: "Thought: Three Types Of Humanity",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'priority', 'god', 'world', 'classification'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.THREE TYPES OF HUMANITY",
    en_title: "Three Types Of Humanity",
    en_content: "Humanity: (1) those who place God 1st; (2) those who give God a priority other than 1st; (3) those who give God no priority at all.",
    es_title: "Tres Tipos de Humanidad",
    es_content: "Humanidad: (1) aquellos que ponen a Dios en primer lugar; (2) aquellos que dan a Dios una prioridad distinta al primer lugar; (3) aquellos que no dan a Dios ninguna prioridad en absoluto.",
    fr_title: "Trois Types d'Humanité",
    fr_content: "Humanité : (1) ceux qui placent Dieu en premier ; (2) ceux qui donnent à Dieu une priorité autre que la première ; (3) ceux qui ne donnent aucune priorité à Dieu.",
    hi_title: "मानवता के तीन प्रकार",
    hi_content: "मानवता: (1) वे जो परमेश्वर को प्रथम स्थान देते हैं; (2) वे जो परमेश्वर को प्रथम के अतिरिक्त कोई अन्य प्राथमिकता देते हैं; (3) वे जो परमेश्वर को बिल्कुल भी कोई प्राथमिकता नहीं देते।",
    zh_title: "Rénlèi de Sān Zhǒng Lèixíng",
    zh_content: "Rénlèi: (1) nàxiē bǎ Shàngdì fàng zài dì yī wèi de rén; (2) nàxiē gěi Shàngdì dì yī wèi yǐwài qítā yōuxiān quán de rén; (3) nàxiē gēnběn bù gěi Shàngdì rènhé yōuxiān quán de rén."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THREE TYPES OF HUMANITY" AND c.name = "content.THREE TYPES OF HUMANITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.THREE TYPES OF HUMANITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.THREE TYPES OF HUMANITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >THREE TYPES OF HUMANITY" }]->(child);
```
