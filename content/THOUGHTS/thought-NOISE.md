---
type: THOUGHT
name: "thought.NOISE"
alias: "Thought: Noise"
parent: "topic.GRACE"
tags: ["heart", "noise", "voice_of_god", "hearing", "holy_spirit"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.NOISE",
    alias: "Thought: Noise",
    parent: "topic.GRACE",
    tags: ["heart", "noise", "voice_of_god", "hearing", "holy_spirit"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOISE",
    ctype: "THOUGHT",
    en_title: "Noise",
    en_content: "",
    es_title: "RUIDO",
    es_content: "¡Es difícil escuchar la Voz de Dios cuando mi corazón hace tanto ruido!",
    fr_title: "BRUIT",
    fr_content: "C'est difficile d'entendre la Voix de Dieu quand mon cœur fait autant de bruit !",
    hi_title: "शोर",
    hi_content: "जब मेरा दिल इतना शोर कर रहा हो तो भगवान की आवाज़ सुनना कठिन है!",
    zh_title: "zào yīn",
    zh_content: "dāng wǒ de xīn fā chū rú cǐ dà de zào yīn shí ， hěn nán tīng dào shàng dì de shēng yīn ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NOISE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->NOISE"
RETURN t, parent;
```
