---
name: "thought.TRANSGENDER RESTROOM DEBATE"
alias: "Thought: Transgender Restroom Debate"
type: THOUGHT
en_content: "A bill that lets a transgendered male into a girls' restroom is one thing; getting that male past the girl's father is another."
parent: "topic.MORALITY"
tags:
- morality
- gender
- society
- father
- safety
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.TRANSGENDER RESTROOM DEBATE",
    alias: "Thought: Transgender Restroom Debate",
    parent: "topic.MORALITY",
    tags: ['morality', 'gender', 'society', 'father', 'safety'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TRANSGENDER RESTROOM DEBATE",
    en_title: "Transgender Restroom Debate",
    en_content: "A bill that lets a transgendered male into a girls' restroom is one thing; getting that male past the girl's father is another.",
    es_title: "Debate sobre Baños para Transgénero",
    es_content: "Una ley que permite a un hombre transgénero entrar al baño de niñas es una cosa; hacer que ese hombre pase al padre de la niña es otra.",
    fr_title: "Débat sur les Toilettes Transgenres",
    fr_content: "Un projet de loi qui permet à un homme transgenre d'entrer dans les toilettes des filles est une chose ; faire passer cet homme devant le père de la fille en est une autre.",
    hi_title: "ट्रांसजेंडर शौचालय बहस",
    hi_content: "एक बिल जो एक ट्रांसजेंडर पुरुष को लड़कियों के शौचालय में जाने देता है वह एक बात है; उस पुरुष को लड़की के पिता के पास से निकालना दूसरी बात है।",
    zh_title: "Kuaxing Bie Cesuo Zhengbian",
    zh_content: "Yi xiang yunxu kuaxingbie nanxing jinru nü'er cesuo de faan shi yi hui shi; rang na ge nanxing tongguo nü'er fuqin shi ling yi hui shi."
});

MATCH (t:THOUGHT {name: "thought.TRANSGENDER RESTROOM DEBATE"})
MATCH (c:CONTENT {name: "content.TRANSGENDER RESTROOM DEBATE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRANSGENDER RESTROOM DEBATE" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.TRANSGENDER RESTROOM DEBATE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->TRANSGENDER RESTROOM DEBATE" }]->(child);
```
