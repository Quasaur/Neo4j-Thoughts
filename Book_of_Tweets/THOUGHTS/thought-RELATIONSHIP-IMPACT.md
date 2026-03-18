---
type: THOUGHT
name: "thought.RELATIONSHIP IMPACT"
alias: "Thought: Relationship Impact"
parent: "topic.SPIRITUALITY"
en_content: "You are either a beneficiary or a casualty of my relationship with God."
tags: ["spirituality", "influence", "relationship", "god", "witness"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Jul-2010)
CREATE (t:THOUGHT {    name: "thought.RELATIONSHIP IMPACT",
    alias: "Thought: Relationship Impact",
    parent: "topic.SPIRITUALITY",
    tags: ['spirituality', 'influence', 'relationship', 'god', 'witness'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.RELATIONSHIP IMPACT",
    ctype: "THOUGHT",
    en_title: "Relationship Impact",
    en_content: "You are either a beneficiary or a casualty of my relationship with God.",
    es_title: "Impacto de la relación",
    es_content: "Eres un beneficiario o una víctima de mi relación con Dios.",
    fr_title: "Impact relationnel",
    fr_content: "Vous êtes soit un bénéficiaire, soit une victime de ma relation avec Dieu.",
    hi_title: "रिश्ते पर प्रभाव",
    hi_content: "आप या तो भगवान के साथ मेरे रिश्ते के लाभार्थी हैं या हताहत हैं।",
    zh_title: "guān xì yǐng xiǎng",
    zh_content: "nǐ yào me shì wǒ yǔ shàng dì guān xì de shòu yì zhě ， yào me shì shòu hài zhě 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.RELATIONSHIP IMPACT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->RELATIONSHIP IMPACT"
RETURN t, parent;
```
