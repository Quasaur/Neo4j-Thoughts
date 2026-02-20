---
name: "thought.GOD REALITY"
alias: "Thought: God Reality"
type: THOUGHT
en_content: "As I was watching TV I realized: God is real...we're just cartoon characters compared to Him!"
parent: "topic.THE GODHEAD"
tags:
- god
- reality
- perspective
- nature_of_god
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Jul-2010)
CREATE (t:THOUGHT {
    name: "thought.GOD REALITY",
    alias: "Thought: God Reality",
    parent: "topic.THE GODHEAD",
    tags: ["god", "reality", "perspective", "nature_of_god", "divinity"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD REALITY",
    en_title: "God Reality",
    en_content: "As I was watching TV I realized: God is real...we're just cartoon characters compared to Him!",
    es_title: "La Realidad de Dios",
    es_content: "Mientras miraba la televisión me di cuenta: Dios es real... ¡somos solo personajes de dibujos animados comparados con Él!",
    fr_title: "La Réalité de Dieu",
    fr_content: "En regardant la télévision, j'ai réalisé : Dieu est réel... nous ne sommes que des personnages de dessins animés comparés à Lui !",
    hi_title: "परमेश्वर वास्तविकता",
    hi_content: "जब मैं टीवी देख रहा था तो मुझे एहसास हुआ: परमेश्वर वास्तविक हैं... उनके सामने हम केवल कार्टून पात्र हैं!",
    zh_title: "Shàngdì de zhēnshíxìng 上帝的真实性",
    zh_content: "Dāng wǒ kàn diànshì shí wǒ yìshí dào: Shàngdì shì zhēnshí de... yǔ tā xiāngbǐ, wǒmen zhǐ shì dònghuà rénwù! 当我看电视时我意识到：上帝是真实的...与他相比，我们只是动画人物！"
});

MATCH (t:THOUGHT {name: "thought.GOD REALITY"})
MATCH (c:CONTENT {name: "content.GOD REALITY"})
MERGE (t)-[:HAS_CONTENT {name: "edge.GOD REALITY"}]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD REALITY"})
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GODHEAD->GOD REALITY"}]->(child);
```
