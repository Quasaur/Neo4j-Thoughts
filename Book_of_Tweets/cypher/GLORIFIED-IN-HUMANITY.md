---
name: "thought.GLORIFIED IN HUMANITY"
alias: "Thought: Glorified In Humanity"
type: THOUGHT
en_content: "God WILL be glorified in Humanity: either by rewarding obedience, faith and courage...or by punishing rebellion, unbelief and cowardice."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- glory
- humanity
- obedience
- rebellion
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Mar-2014)
CREATE (t:THOUGHT {
    name: "thought.GLORIFIED IN HUMANITY",
    alias: "Thought: Glorified In Humanity",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['glory', 'humanity', 'obedience', 'rebellion'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLORIFIED IN HUMANITY",
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

MATCH (t:THOUGHT {name: "thought.GLORIFIED IN HUMANITY"})
MATCH (c:CONTENT {name: "content.GLORIFIED IN HUMANITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GLORIFIED IN HUMANITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.GLORIFIED IN HUMANITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >GLORIFIED IN HUMANITY" }]->(child);
```
