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
 es_title: "RUIDO",
 fr_title: "BRUIT",
 hi_title: "शोर",
 zh_title: "zào yīn",
    en_content: "",
 es_content: "¡Es difícil escuchar la Voz de Dios cuando mi corazón hace tanto ruido!",
 fr_content: "C'est difficile d'entendre la Voix de Dieu quand mon cœur fait autant de bruit !",
 hi_content: "जब मेरा दिल इतना शोर कर रहा हो तो भगवान की आवाज़ सुनना कठिन है!",
 zh_content: "dāng wǒ de xīn fā chū rú cǐ dà de zào yīn shí ， hěn nán tīng dào shàng dì de shēng yīn ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOISE" AND c.name = "content.NOISE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.NOISE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.NOISE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->NOISE"}]->(child);
```