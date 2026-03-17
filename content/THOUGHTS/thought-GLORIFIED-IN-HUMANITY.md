---
type: THOUGHT
name: "thought.GLORIFIED IN HUMANITY"
alias: "Thought: Glorified In Humanity"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "God WILL be glorified in Humanity: either by rewarding obedience, faith and courage...or by punishing rebellion, unbelief and cowardice."
tags: ["glory", "humanity", "obedience", "rebellion"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GLORIFIED IN HUMANITY",
    alias: "Thought: Glorified In Humanity",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['glory', 'humanity', 'obedience', 'rebellion'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLORIFIED IN HUMANITY",
    ctype: "THOUGHT",
    en_title: "Glorified In Humanity",
    en_content: "God WILL be glorified in Humanity: either by rewarding obedience, faith and courage...or by punishing rebellion, unbelief and cowardice.",
    es_title: "Glorificado en la Humanidad",
    es_content: "Dios SERÁ glorificado en la Humanidad: ya sea recompensando la obediencia, la fe y el valor...o castigando la rebelión, la incredulidad y la cobardía.",
    fr_title: "Glorifié dans l'Humanité",
    fr_content: "Dieu SERA glorifié dans l'Humanité : soit en récompensant l'obéissance, la foi et le courage...soit en punissant la rébellion, l'incrédulité et la lâcheté.",
    hi_title: "मानवता में महिमामंडित",
    hi_content: "परमेश्वर मानवता में महिमामंडित होंगे: या तो आज्ञाकारिता, विश्वास और साहस को पुरस्कृत करके...या विद्रोह, अविश्वास और कायरता को दंडित करके।",
    zh_title: "Zài rénlèi zhōng dédào róngguāng",
    zh_content: "Shàngdì jiāng zài rénlèi zhōng dédào róngguāng: huòzhě tōngguò jiǎngshǎng shùncóng, xìnyǎng hé yǒngqì...huòzhě tōngguò chéngfá pànluàn, bù xìn hé qiènuò."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GLORIFIED IN HUMANITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->GLORIFIED IN HUMANITY"
RETURN t, parent;
```
