---
name: "thought.CHANGE OTHERS NOT SELF"
alias: "Thought: Change Others Not Self"
type: THOUGHT
en_content: We want God to change everyone but ourselves; for the truth is that change can be a painful process...even when God is performing it.
parent: topic.ATTITUDE
tags:
  - change
  - growth
  - attitude
  - pain
  - transformation
level: 3
neo4j: false
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.CHANGE OTHERS NOT SELF",
    alias: "Thought: Change Others Not Self",
    parent: "topic.ATTITUDE",
    tags: ['change', 'growth', 'attitude', 'pain', 'transformation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHANGE OTHERS NOT SELF",
    en_title: "Change Others Not Self",
    en_content: "We want God to change everyone but ourselves; for the truth is that change can be a painful process...even when God is performing it.",
    es_title: "Cambiar a Otros No a Uno Mismo",
    es_content: "Queremos que Dios cambie a todos menos a nosotros mismos; porque la verdad es que el cambio puede ser un proceso doloroso... incluso cuando Dios lo está realizando.",
    fr_title: "Changer les Autres Pas Soi-Même",
    fr_content: "Nous voulons que Dieu change tout le monde sauf nous-mêmes ; car la vérité est que le changement peut être un processus douloureux... même lorsque Dieu l'accomplit.",
    hi_title: "दूसरों को बदलना स्वयं को नहीं",
    hi_content: "हम चाहते हैं कि परमेश्वर सभी को बदल दे लेकिन खुद को नहीं; क्योंकि सच्चाई यह है कि परिवर्तन एक दर्दनाक प्रक्रिया हो सकती है... तब भी जब परमेश्वर इसे कर रहे हों।",
    zh_title: "Gǎibiàn Tārén Bù Gǎibiàn Zìjǐ",
    zh_content: "Wǒmen xīwàng Shàngdì gǎibiàn suǒyǒu rén chúle wǒmen zìjǐ; Yīnwèi shìshí shì gǎibiàn kěnéng shì yīgè tòngkǔ de guòchéng... Jíshǐ shì Shàngdì zài jìnxíng shí."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CHANGE OTHERS NOT SELF" AND c.name = "content.CHANGE OTHERS NOT SELF"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHANGE OTHERS NOT SELF" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.CHANGE OTHERS NOT SELF"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >CHANGE OTHERS NOT SELF" }]->(child);
```
