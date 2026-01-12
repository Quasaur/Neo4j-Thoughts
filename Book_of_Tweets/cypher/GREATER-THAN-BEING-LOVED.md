---
name: "thought.GREATER THAN BEING LOVED"
alias: "Thought: Greater Than Being Loved"
type: THOUGHT
en_content: "What could be greater than being loved? Being able to love!"
parent: "topic.LOVE"
tags:
- love
- sacrifice
- ability
- emotion
- divinity
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.GREATER THAN BEING LOVED",
    alias: "Thought: Greater Than Being Loved",
    parent: "topic.LOVE",
    tags: ['love', 'sacrifice', 'ability', 'emotion', 'divinity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GREATER THAN BEING LOVED",
    en_title: "Greater Than Being Loved",
    en_content: "What could be greater than being loved? Being able to love!",
    es_title: "Más Grande Que Ser Amado",
    es_content: "¿Qué podría ser más grande que ser amado? ¡Poder amar!",
    fr_title: "Plus Grand Que D'être Aimé",
    fr_content: "Qu'est-ce qui pourrait être plus grand que d'être aimé ? Être capable d'aimer !",
    hi_title: "प्रेम पाने से भी महान",
    hi_content: "प्रेम पाने से भी महान क्या हो सकता है? प्रेम कर पाना!",
    zh_title: "Bǐ Bèi Ài Gèng Wěidà",
    zh_content: "Yǒu shénme néng bǐ bèi ài gèng wěidà ne? Nénggòu qù ài!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GREATER THAN BEING LOVED" AND c.name = "content.GREATER THAN BEING LOVED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GREATER THAN BEING LOVED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LOVE" AND child.name = "thought.GREATER THAN BEING LOVED"
MERGE (parent)-[:HAS_THOUGHT { "name": "LOVE >GREATER THAN BEING LOVED" }]->(child);
```
