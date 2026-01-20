---
name: "thought.MASTERING SIN"
alias: "Thought: Mastering Sin"
type: THOUGHT
en_content: "Genesis 4:6,7 God doesn't expect us to eradicate sin (that's His Job)...but He does expect us to master sin."
parent: "topic.MORALITY"
tags:
- sin
- mastery
- morality
- responsibility
- victory
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.MASTERING SIN",
    alias: "Thought: Mastering Sin",
    parent: "topic.MORALITY",
    tags: ['sin', 'mastery', 'morality', 'responsibility', 'victory'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MASTERING SIN",
    en_title: "Mastering Sin",
    en_content: "Genesis 4:6,7 God doesn't expect us to eradicate sin (that's His Job)...but He does expect us to master sin.",
    es_title: "Dominando el Pecado",
    es_content: "Génesis 4:6,7 Dios no espera que erradiquemos el pecado (ese es Su trabajo)... pero sí espera que dominemos el pecado.",
    fr_title: "Maîtriser le Péché",
    fr_content: "Genèse 4:6,7 Dieu ne s'attend pas à ce que nous éradiquions le péché (c'est Son travail)... mais Il s'attend à ce que nous maîtris ions le péché.",
    hi_title: "पाप पर विजय पाना",
    hi_content: "उत्पत्ति 4:6,7 परमेश्वर हमसे यह उम्मीद नहीं करते कि हम पाप को मिटा दें (यह उनका काम है)... लेकिन वे उम्मीद करते हैं कि हम पाप पर विजय पाएं।",
    zh_title: "Zhàngwò zuìzhèng 掌握罪政",
    zh_content: "Chuàngshì jì 4:6,7 Shàngdì bù qīwàng wǒmen gēnchú zuìzhèng (nà shì tā de gōngzuò)... dàn tā quèshí qīwàng wǒmen zhàngwò zuìzhèng. 创世记4:6,7 上帝不期望我们根除罪政（那是他的工作）...但他确实期望我们掌握罪政。"
});

MATCH (t:THOUGHT {name: "thought.MASTERING SIN"})
MATCH (c:CONTENT {name: "content.MASTERING SIN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.MASTERING SIN" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.MASTERING SIN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >MASTERING SIN" }]->(child);
```
