---
name: "thought.LOYALTY TO GOD"
alias: "Thought: Loyalty To God"
type: THOUGHT
en_content: "What pleases God? Loyalty...at whatever cost to yourself, your family or your friends."
parent: "topic.SPIRITUALITY"
tags:
- loyalty
- devotion
- spirituality
- commitment
- sacrifice
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.LOYALTY TO GOD",
    alias: "Thought: Loyalty To God",
    parent: "topic.SPIRITUALITY",
    tags: ['loyalty', 'devotion', 'spirituality', 'commitment', 'sacrifice'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOYALTY TO GOD",
    en_title: "Loyalty To God",
    en_content: "What pleases God? Loyalty...at whatever cost to yourself, your family or your friends.",
    es_title: "Lealtad a Dios",
    es_content: "¿Qué agrada a Dios? La lealtad...sin importar el costo para ti mismo, tu familia o tus amigos.",
    fr_title: "Loyauté envers Dieu",
    fr_content: "Qu'est-ce qui plaît à Dieu ? La loyauté...quel qu'en soit le coût pour vous-même, votre famille ou vos amis.",
    hi_title: "ईश्वर के प्रति निष्ठा",
    hi_content: "ईश्वर को क्या प्रसन्न करता है? निष्ठा...चाहे इसकी कीमत आपको, आपके परिवार या आपके मित्रों को चुकानी पड़े।",
    zh_title: "Dui Shang Di De Zhong Cheng",
    zh_content: "Shen Me Shi Qing Shang Di Xi Yue De? Zhong Cheng...Wu Lun Dui Ni Zi Ji, Ni De Jia Ting Huo Ni De Peng You Fu Chu Shen Me Dai Jia."
});

MATCH (t:THOUGHT {name: "thought.LOYALTY TO GOD"})
MATCH (c:CONTENT {name: "content.LOYALTY TO GOD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOYALTY TO GOD" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.LOYALTY TO GOD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >LOYALTY TO GOD" }]->(child);
```
