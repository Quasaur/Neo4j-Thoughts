---
type: THOUGHT
name: "thought.MYSTERY"
alias: "Thought: Mystery"
parent: "topic.PSYCHOLOGY"
tags: ["wife", "mystery", "understanding", "life", "gift"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.MYSTERY",
    alias: "Thought: Mystery",
    parent: "topic.PSYCHOLOGY",
    tags: ["wife", "mystery", "understanding", "life", "gift"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MYSTERY",
    ctype: "THOUGHT",
    en_title: "Mystery",
    en_content: "",
    es_title: "MISTERIO",
    es_content: "Hay tantas cosas sobre mi esposa que no entiendo...
...pero cuando estamos solos y en silencio, ¡ella me da VIDA!",
    fr_title: "MYSTÈRE",
    fr_content: "Il y a tellement de choses sur ma femme que je ne comprends pas...
...mais quand nous sommes seuls ensemble et tranquilles, elle me donne la VIE !",
    hi_title: "रहस्य",
    hi_content: "मेरी पत्नी के बारे में बहुत सी बातें हैं जो मुझे समझ नहीं आती...
...लेकिन जब हम एक साथ अकेले और शांत होते हैं, तो वह मुझे जीवन देती है!",
    zh_title: "shén mì",
    zh_content: "wǒ de qī zǐ yǒu hěn duō shì qíng wǒ bù míng bái ......
... dàn shì dāng wǒ men dān dú ān jìng dì zài yì qǐ shí ， tā gěi le wǒ shēng mìng ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MYSTERY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->MYSTERY"
RETURN t, parent;
```
