---
type: THOUGHT
name: "thought.MASTERING SIN"
alias: "Thought: Mastering Sin"
parent: "topic.MORALITY"
en_content: "Genesis 4:6,7 God doesn't expect us to eradicate sin (that's His Job)...but He does expect us to master sin."
tags: ["sin", "mastery", "morality", "responsibility", "victory"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Sep-2010)
CREATE (t:THOUGHT {    name: "thought.MASTERING SIN",
    alias: "Thought: Mastering Sin",
    parent: "topic.MORALITY",
    tags: ['sin', 'mastery', 'morality', 'responsibility', 'victory'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.MASTERING SIN",
    ctype: "THOUGHT",
    en_title: "Mastering Sin",
    en_content: "Genesis 4:6,7 God doesn't expect us to eradicate sin (that's His Job)...but He does expect us to master sin.",
    es_title: "Dominando el Pecado",
    es_content: "Génesis 4:6,7 Dios no espera que erradiquemos el pecado (ese es Su trabajo)... pero sí espera que dominemos el pecado.",
    fr_title: "Maîtriser le Péché",
    fr_content: "Genèse 4:6,7 Dieu ne s'attend pas à ce que nous éradiquions le péché (c'est Son travail)... mais Il s'attend à ce que nous maîtris ions le péché.",
    hi_title: "पाप पर विजय पाना",
    hi_content: "उत्पत्ति 4:6,7 परमेश्वर हमसे यह उम्मीद नहीं करते कि हम पाप को मिटा दें (यह उनका काम है)... लेकिन वे उम्मीद करते हैं कि हम पाप पर विजय पाएं।",
    zh_title: "Zhàngwò zuìzhèng  zhǎng wò zuì zhèng",
    zh_content: "Chuàngshì jì 4:6,7 Shàngdì bù qīwàng wǒmen gēnchú zuìzhèng (nà shì tā de gōngzuò)... dàn tā quèshí qīwàng wǒmen zhàngwò zuìzhèng.  chuàng shì jì 4:6,7  shàng dì bù qī wàng wǒ men gēn chú zuì zhèng （ nà shì tā de gōng zuò ）... dàn tā què shí qī wàng wǒ men zhǎng wò zuì zhèng 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MASTERING SIN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->MASTERING SIN"
RETURN t, parent;
```
