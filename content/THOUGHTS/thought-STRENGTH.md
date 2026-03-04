---
type: THOUGHT
name: "thought.STRENGTH"
alias: "Thought: Strength"
parent: "topic.ATTITUDE"
tags: ["power", "virtue", "strength", "endurance", "jesus_christ"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
---

```Cypher
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
 es_title: "FORTALEZA",
 fr_title: "FORCE",
 hi_title: "ताकत",
 zh_title: "lì liàng",
    en_content: "",
 es_content: "En 61 años nunca he conocido a un cristiano fuerte.
Sin embargo, en ese mismo tiempo, me he encontrado con unos pocos cristianos débiles que se han sometido a la Fortaleza de Jesús.
“Bienaventurados los pobres de espíritu”. - Mateo 5:3",
 fr_content: "En 61 ans, je n’ai jamais rencontré un chrétien fort.
Pourtant, au même moment, j’ai rencontré quelques précieux chrétiens faibles qui se sont soumis à la force de Jésus !
« Bienheureux les pauvres en esprit. » - Matthieu 5:3",
 hi_content: "61 वर्षों में मैं कभी किसी मजबूत ईसाई से नहीं मिला।
फिर भी, उसी समय में, मुझे कुछ अनमोल कमजोर ईसाई मिले हैं जिन्होंने खुद को यीशु की ताकत के सामने समर्पित कर दिया है!
\"धन्य हैं वे जो आत्मा में गरीब हैं।\" - मत्ती 5:3"धन्य हैं वे जो आत्मा में गरीब हैं।\" - मत्ती 5:3"धन्य हैं वे जो आत्मा में गरीब हैं।\" - मत्ती 5:3"धन्य हैं वे जो आत्मा में गरीब हैं।\" - मत्ती 5:3",
 zh_content: "61 nián lái wǒ cóng wèi yù dào guò jiān qiáng de jī dū tú 。
 rán ér ， yǔ cǐ tóng shí ， wǒ yù dào le yī xiē bǎo guì de ruǎn ruò jī dū tú ， tā men shùn fú le yē sū de lì liàng ！
“ jīng shén pín qióng de rén yǒu fú le 。” -  mǎ tài fú yīn  5:3"धन्य हैं वे जो आत्मा में गरीब हैं।\" - मत्ती 5:3"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.STRENGTH" AND c.name = "content.STRENGTH"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.STRENGTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.STRENGTH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->STRENGTH"}]->(child);
```