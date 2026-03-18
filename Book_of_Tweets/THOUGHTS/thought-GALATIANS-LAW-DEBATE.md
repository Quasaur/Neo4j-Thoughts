---
type: THOUGHT
name: "thought.GALATIANS LAW DEBATE"
alias: "Thought: Galatians Law Debate"
parent: "topic.RELIGION"
en_content: "The debate of Galatians is not over the law, but whether or not keeping the law will save one WHO HAS ALREADY BROKEN IT."
tags: ["galatians", "law", "grace", "bible", "debate"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Apr-2013)
CREATE (t:THOUGHT {    name: "thought.GALATIANS LAW DEBATE",
    alias: "Thought: Galatians Law Debate",
    parent: "topic.RELIGION",
    tags: ['galatians', 'law', 'grace', 'bible', 'debate'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.GALATIANS LAW DEBATE",
    ctype: "THOUGHT",
    en_title: "Galatians Law Debate",
    en_content: "The debate of Galatians is not over the law, but whether or not keeping the law will save one WHO HAS ALREADY BROKEN IT.",
    es_title: "Debate de la Ley en Gálatas",
    es_content: "El debate de Gálatas no es sobre la ley, sino sobre si guardar la ley salvará o no a alguien QUE YA LA HA QUEBRANTADO.",
    fr_title: "Débat de la Loi dans Galates",
    fr_content: "Le débat des Galates ne porte pas sur la loi, mais sur la question de savoir si l'observance de la loi sauvera quelqu'un QUI L'A DÉJÀ TRANSGRESSÉE.",
    hi_title: "गलातियों की व्यवस्था बहस",
    hi_content: "गलातियों की बहस व्यवस्था के बारे में नहीं है, बल्कि इस बारे में है कि क्या व्यवस्था का पालन करना उस व्यक्ति को बचाएगा जिसने इसे पहले ही तोड़ दिया है।",
    zh_title: "Jialataishu Lüfa Zhengbian",
    zh_content: "Jialataishu de zhengbian bushi guanyu lüfa, er shi guanyu zunxing lüfa shifou neng zhengjiù yige YI JING WEIFAN LE LÜFA de ren."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GALATIANS LAW DEBATE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->GALATIANS LAW DEBATE"
RETURN t, parent;
```
