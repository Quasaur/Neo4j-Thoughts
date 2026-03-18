---
type: THOUGHT
name: "thought.CHANGE OTHERS NOT SELF"
alias: "Thought: Change Others, Not Self"
parent: "topic.ATTITUDE"
en_content: "We want God to change everyone but ourselves; for the truth is that change can be a painful process...even when God is performing it."
tags: ["change", "growth", "attitude", "pain", "transformation"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.CHANGE OTHERS NOT SELF",
    alias: "Thought: Change Others, Not Self",
    parent: "topic.ATTITUDE",
    tags: ["change", "growth", "attitude", "pain", "transformation"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHANGE OTHERS NOT SELF",
    ctype: "THOUGHT",
    en_title: "Thought: Change Others, Not Self",
    en_content: "We want God to change everyone but ourselves; for the truth is that change can be a painful process...even when God is performing it.",
    es_title: "Pensamiento: Cambiar a Otros No a Uno Mismo",
    es_content: "Queremos que Dios cambie a todos menos a nosotros mismos; porque la verdad es que el cambio puede ser un proceso doloroso... incluso cuando Dios lo está realizando.",
    fr_title: "Pensée : Changer les Autres Pas Soi-Même",
    fr_content: "Nous voulons que Dieu change tout le monde sauf nous-mêmes ; car la vérité est que le changement peut être un processus douloureux... même lorsque Dieu l'accomplit.",
    hi_title: "विचार: दूसरों को बदलें, स्वयं को नहीं",
    hi_content: "हम चाहते हैं कि परमेश्वर सभी को बदल दे लेकिन खुद को नहीं; क्योंकि सच्चाई यह है कि परिवर्तन एक दर्दनाक प्रक्रिया हो सकती है... तब भी जब परमेश्वर इसे कर रहे हों।",
    zh_title: "sī xiǎng : Gǎibiàn Tārén Bù Gǎibiàn Zìjǐ",
    zh_content: "Wǒmen xīwàng Shàngdì gǎibiàn suǒyǒu rén chúle wǒmen zìjǐ; Yīnwèi shìshí shì gǎibiàn kěnéng shì yīgè tòngkǔ de guòchéng... Jíshǐ shì Shàngdì zài jìnxíng shí."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CHANGE OTHERS NOT SELF"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->CHANGE OTHERS NOT SELF"
RETURN t, parent;
```
