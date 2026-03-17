---
type: THOUGHT
name: "thought.OVERCOMING FEAR BLAME"
alias: "Thought: Overcoming Fear Blame"
parent: "topic.ATTITUDE"
en_content: "If you keep blaming others for your fears, you'll never overcome them."
tags: ["fear", "blame", "attitude", "courage", "character"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.OVERCOMING FEAR BLAME",
    alias: "Thought: Overcoming Fear Blame",
    parent: "topic.ATTITUDE",
    tags: ['fear', 'blame', 'attitude', 'courage', 'character'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OVERCOMING FEAR BLAME",
    ctype: "THOUGHT",
    en_title: "Overcoming Fear Blame",
    en_content: "If you keep blaming others for your fears, you'll never overcome them.",
    es_title: "Superando la Culpa del Miedo",
    es_content: "Si sigues culpando a otros por tus miedos, nunca los superarás.",
    fr_title: "Surmonter le Blâme de la Peur",
    fr_content: "Si tu continues à blâmer les autres pour tes peurs, tu ne les surmonteras jamais.",
    hi_title: "भय के दोषारोपण पर विजय",
    hi_content: "यदि तुम अपने भय के लिए दूसरों को दोष देते रहोगे, तो तुम कभी भी उन पर विजय नहीं पा सकोगे।",
    zh_title: "Kèfú Kǒngjù Zhǐzé",
    zh_content: "Rúguǒ nǐ yīzhí wèi nǐ de kǒngjù zérèn biérén, nǐ jiāng yǒngyuǎn wúfǎ kèfú tāmen."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.OVERCOMING FEAR BLAME"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->OVERCOMING FEAR BLAME"
RETURN t, parent;
```
