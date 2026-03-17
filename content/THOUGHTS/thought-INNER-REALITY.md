---
type: THOUGHT
name: "thought.INNER REALITY"
alias: "Thought: Inner Reality"
parent: "topic.ATTITUDE"
en_content: "What's going on INSIDE of you is far more potent, effectual and real—to you--than what's going on outside of you."
tags: ["heart", "feelings", "perception", "reaction", "reality"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.INNER REALITY",
    alias: "Thought: Inner Reality",
    parent: "topic.ATTITUDE",
    tags: ["heart", "feelings", "perception", "reaction", "reality"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INNER REALITY",
    ctype: "THOUGHT",
    en_title: "Inner Reality",
    en_content: "What's going on INSIDE of you is far more potent, effectual and real—to you--than what's going on outside of you.",
    es_title: "REALIDAD INTERIOR",
    es_content: "Lo que sucede DENTRO de usted es mucho más potente, eficaz y real (para usted) que lo que sucede fuera de usted.",
    fr_title: "RÉALITÉ INTÉRIEURE",
    fr_content: "Ce qui se passe à l'INTÉRIEUR de vous est bien plus puissant, efficace et réel – pour vous – que ce qui se passe à l'extérieur de vous.",
    hi_title: "आंतरिक वास्तविकता",
    hi_content: "आपके अंदर जो चल रहा है वह आपके लिए कहीं अधिक सशक्त, प्रभावशाली और वास्तविक है--आपके बाहर जो चल रहा है उससे कहीं अधिक।",
    zh_title: "nèi zài xiàn shí",
    zh_content: "duì nǐ lái shuō ， nǐ nèi xīn fā shēng de shì qíng bǐ nǐ wài bù fā shēng de shì qíng gèng jiā yǒu lì 、 yǒu xiào hé zhēn shí 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INNER REALITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->INNER REALITY"
RETURN t, parent;
```
