---
type: THOUGHT
name: "thought.STRENGTH"
alias: "Thought: Strength"
parent: "topic.ATTITUDE"
tags: ["power", "virtue", "strength", "endurance", "jesus_christ"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.STRENGTH",
    alias: "Thought: Strength",
    parent: "topic.ATTITUDE",
    tags: ["power", "virtue", "strength", "endurance", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.STRENGTH",
    ctype: "THOUGHT",
    en_title: "Strength",
    en_content: "",
    es_title: "FORTALEZA",
    es_content: "En 61 años nunca he conocido a un cristiano fuerte.
Sin embargo, en ese mismo tiempo, me he encontrado con unos pocos cristianos débiles que se han sometido a la Fortaleza de Jesús.
“Bienaventurados los pobres de espíritu”. - Mateo 5:3",
    fr_title: "FORCE",
    fr_content: "En 61 ans, je n’ai jamais rencontré un chrétien fort.
Pourtant, au même moment, j’ai rencontré quelques précieux chrétiens faibles qui se sont soumis à la force de Jésus !
« Bienheureux les pauvres en esprit. » - Matthieu 5:3",
    hi_title: "ताकत",
    hi_content: "61 वर्षों में मैं कभी किसी मजबूत ईसाई से नहीं मिला।
फिर भी, उसी समय में, मुझे कुछ अनमोल कमजोर ईसाई मिले हैं जिन्होंने खुद को यीशु की ताकत के सामने समर्पित कर दिया है!
\\\"धन्य हैं वे जो आत्मा में गरीब हैं।\\\" - मत्ती 5:3",
    zh_title: "lì liàng",
    zh_content: "61 nián lái wǒ cóng wèi yù dào guò jiān qiáng de jī dū tú 。
 rán ér ， yǔ cǐ tóng shí ， wǒ yù dào le yī xiē bǎo guì de ruǎn ruò jī dū tú ， tā men shùn fú le yē sū de lì liàng ！
“ jīng shén pín qióng de rén yǒu fú le 。” -  mǎ tài fú yīn  5:3"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.STRENGTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->STRENGTH"
RETURN t, parent;
```
