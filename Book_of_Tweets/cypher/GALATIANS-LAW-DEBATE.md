---
name: "thought.GALATIANS LAW DEBATE"
alias: "Thought: Galatians Law Debate"
type: THOUGHT
en_content: "The debate of Galatians is not over the law, but whether or not keeping the law will save one WHO HAS ALREADY BROKEN IT."
parent: "topic.RELIGION"
tags:
- galatians
- law
- grace
- bible
- debate
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Apr-2013)
CREATE (t:THOUGHT {
    name: "thought.GALATIANS LAW DEBATE",
    alias: "Thought: Galatians Law Debate",
    parent: "topic.RELIGION",
    tags: ['galatians', 'law', 'grace', 'bible', 'debate'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GALATIANS LAW DEBATE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GALATIANS LAW DEBATE" AND c.name = "content.GALATIANS LAW DEBATE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GALATIANS LAW DEBATE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.GALATIANS LAW DEBATE"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >GALATIANS LAW DEBATE" }]->(child);
```
