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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INNER REALITY" AND c.name = "content.INNER REALITY"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.INNER REALITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.INNER REALITY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->INNER REALITY"}]->(child);
```
