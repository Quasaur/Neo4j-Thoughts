---
type: THOUGHT
name: "thought.DEFINE APATHY"
alias: "Thought: Apathy Defined"
parent: "topic.ATTITUDE"
en_content: "Love & Hate are not opposites; they are two halves of the same coin; the opposite of Love / Hate is Apathy."
tags: ["love", "hate", "apathy", "attitude", "philosophy"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE APATHY",
    alias: "Thought: Apathy Defined",
    parent: "topic.ATTITUDE",
    tags: ['love', 'hate', 'apathy', 'attitude', 'philosophy'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINE APATHY",
    ctype: "THOUGHT",
    en_title: "Thought: Apathy Defined",
    en_content: "Love & Hate are not opposites; they are two halves of the same coin; the opposite of Love / Hate is Apathy.",
    es_title: "Pensamiento: Definición de apatía",
    es_content: "El amor y el odio no son opuestos; son dos mitades de una misma moneda; lo opuesto al Amor/Odio es la Apatía.",
    fr_title: "Pensée : définition de l'apathie",
    fr_content: "L'amour et la haine ne sont pas opposés ; ce sont les deux moitiés d’une même pièce ; le contraire de l’Amour/Haine est l’Apathie.",
    hi_title: "विचार: उदासीनता परिभाषित",
    hi_content: "प्यार और नफरत विपरीत नहीं हैं; वे एक ही सिक्के के दो हिस्से हैं; प्रेम/नफरत का विपरीत उदासीनता है।",
    zh_title: "sī xiǎng : lěng mò de dìng yì",
    zh_content: "ài yǔ hèn bú shì duì lì de ; tā men shì tóng yī méi yìng bì de liǎng bàn ; ài / hèn de fǎn miàn shì lěng mò ."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE APATHY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->DEFINE APATHY"
RETURN t, parent;
```
