---
name: "thought.BETTER TREATMENT JESUS"
alias: "Thought: Better Treatment Jesus"
type: THOUGHT
en_content: "Jesus treats me FAR BETTER than I've treated Him. I crucified Him; He gave me LIFE!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- life
- treatment
- grace
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.BETTER TREATMENT JESUS",
    alias: "Thought: Better Treatment Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'life', 'treatment', 'grace', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.BETTER TREATMENT JESUS",
    en_title: "Better Treatment Jesus",
    en_content: "Jesus treats me FAR BETTER than I've treated Him. I crucified Him; He gave me LIFE!",
    es_title: "Mejor Trato de Jesús",
    es_content: "Jesús me trata MUCHO MEJOR de lo que yo lo he tratado a Él. Yo lo crucifiqué; ¡Él me dio VIDA!",
    fr_title: "Meilleur Traitement de Jésus",
    fr_content: "Jésus me traite BIEN MIEUX que je ne l'ai traité. Je l'ai crucifié ; Il m'a donné la VIE !",
    hi_title: "यीशु का बेहतर व्यवहार",
    hi_content: "यीशु मेरे साथ उससे कहीं बेहतर व्यवहार करते हैं जितना मैंने उनके साथ किया है। मैंने उन्हें सूली पर चढ़ाया; उन्होंने मुझे जीवन दिया!",
    zh_title: "Yēsū de gèng hǎo dàiyù 耶稣的更好待遇",
    zh_content: "Yēsū duì wǒ de dàiyù yuǎn bǐ wǒ duì Tā de dàiyù hǎo de duō. Wǒ jiāng Tā dīng zài shízìjià shàng; Tā què gěi le wǒ shēngmìng! 耶稣对我的待遇远比我对祂的待遇好得多。我将祂钉在十字架上；祂却给了我生命！"
});

MATCH (t:THOUGHT {name: "thought.BETTER TREATMENT JESUS"})
MATCH (c:CONTENT {name: "content.BETTER TREATMENT JESUS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.BETTER TREATMENT JESUS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.BETTER TREATMENT JESUS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->BETTER TREATMENT JESUS" }]->(child);
```
