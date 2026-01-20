---
name: "thought.ALONZO CHURCH FAITH"
alias: "Thought: Alonzo Church Faith"
type: THOUGHT
en_content: "Alonzo Church Ph.D, Inventor of the lambda calculus, was a devout Christian...who says science and faith don't mix?"
parent: "topic.RELIGION"
tags:
- science
- faith
- alonzo_church
- logic
- religion
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Oct-2013b)
CREATE (t:THOUGHT {
    name: "thought.ALONZO CHURCH FAITH",
    alias: "Thought: Alonzo Church Faith",
    parent: "topic.RELIGION",
    tags: ['science', 'faith', 'alonzo_church', 'logic', 'religion'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ALONZO CHURCH FAITH",
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

MATCH (t:THOUGHT {name: "thought.ALONZO CHURCH FAITH"})
MATCH (c:CONTENT {name: "content.ALONZO CHURCH FAITH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALONZO CHURCH FAITH" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.ALONZO CHURCH FAITH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >ALONZO CHURCH FAITH" }]->(child);
```
