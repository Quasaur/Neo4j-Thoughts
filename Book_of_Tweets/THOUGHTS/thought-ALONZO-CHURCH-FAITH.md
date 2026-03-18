---
type: THOUGHT
name: "thought.ALONZO CHURCH FAITH"
alias: "Thought: Alonzo Church Faith"
parent: "topic.RELIGION"
en_content: "Alonzo Church Ph.D, Inventor of the lambda calculus, was a devout Christian...who says science and faith don't mix?"
tags: ["science", "faith", "alonzo_church", "logic", "religion"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Oct-2013b)
CREATE (t:THOUGHT {    name: "thought.ALONZO CHURCH FAITH",
    alias: "Thought: Alonzo Church Faith",
    parent: "topic.RELIGION",
    tags: ['science', 'faith', 'alonzo_church', 'logic', 'religion'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.ALONZO CHURCH FAITH",
    ctype: "THOUGHT",
    en_title: "Alonzo Church Faith",
    en_content: "Alonzo Church Ph.D, Inventor of the lambda calculus, was a devout Christian...who says science and faith don't mix?",
    es_title: "La Fe de Alonzo Church",
    es_content: "Alonzo Church Ph.D, inventor del cálculo lambda, era un cristiano devoto... ¿quién dice que la ciencia y la fe no se mezclan?",
    fr_title: "La Foi d'Alonzo Church",
    fr_content: "Alonzo Church Ph.D, inventeur du lambda-calcul, était un chrétien fervent... qui dit que la science et la foi ne se mélangent pas ?",
    hi_title: "एलोंजो चर्च की आस्था",
    hi_content: "एलोंजो चर्च पीएच.डी., लैम्ब्डा कैलकुलस के आविष्कारक, एक समर्पित ईसाई थे... कौन कहता है कि विज्ञान और आस्था मिश्रित नहीं होते?",
    zh_title: "Ālóngzuǒ qiūqí xìnyǎng",
    zh_content: "Ālóngzuǒ qiūqí bóshì, λ yǎnsuàn de fāmíngzhě, shì yīwèi qiánchéng de jīdūtú... shéi shuō kēxué hé xìnyǎng bùnéng gòngcún?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ALONZO CHURCH FAITH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->ALONZO CHURCH FAITH"
RETURN t, parent;
```
