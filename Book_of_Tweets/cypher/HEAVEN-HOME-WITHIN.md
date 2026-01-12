---
name: "thought.HEAVEN HOME WITHIN"
alias: "Thought: Heaven Home Within"
type: THOUGHT
en_content: "Before I can go Home to Heaven, Heaven must find a home in me."
parent: "topic.SPIRITUALITY"
tags:
- heaven
- home
- spirituality
- transformation
- presence
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN HOME WITHIN",
    alias: "Thought: Heaven Home Within",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'home', 'spirituality', 'transformation', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEAVEN HOME WITHIN",
    en_title: "Heaven Home Within",
    en_content: "Before I can go Home to Heaven, Heaven must find a home in me.",
    es_title: "El Cielo Como Hogar Interior",
    es_content: "Antes de poder ir al Hogar del Cielo, el Cielo debe encontrar un hogar en mí.",
    fr_title: "Le Ciel Demeure Intérieure",
    fr_content: "Avant de pouvoir rentrer à la Maison du Ciel, le Ciel doit trouver une demeure en moi.",
    hi_title: "स्वर्ग का आंतरिक निवास",
    hi_content: "इससे पहले कि मैं स्वर्ग के घर जा सकूं, स्वर्ग को मुझमें अपना घर बनाना होगा।",
    zh_title: "Tiāntáng Nèi Zài Zhī Jiā",
    zh_content: "Zài wǒ néng gòu huí dào tiāntáng de jiā zhīqián, tiāntáng bìxū xiān zài wǒ xīn zhōng zhǎo dào yī gè jiā."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HEAVEN HOME WITHIN" AND c.name = "content.HEAVEN HOME WITHIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN HOME WITHIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HEAVEN HOME WITHIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEAVEN HOME WITHIN" }]->(child);
```
