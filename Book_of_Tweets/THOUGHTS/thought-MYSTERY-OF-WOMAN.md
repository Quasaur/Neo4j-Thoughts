---
type: THOUGHT
name: "thought.MYSTERY OF WOMAN"
alias: "Thought: Mystery Of Woman"
parent: "topic.HUMANITY"
en_content: "Adam did not see Eve being created; therefore Woman will always be a Mystery to Man."
tags: ["woman", "man", "mystery", "creation", "adam"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Jul-2012)
CREATE (t:THOUGHT {    name: "thought.MYSTERY OF WOMAN",
    alias: "Thought: Mystery Of Woman",
    parent: "topic.HUMANITY",
    tags: ['woman', 'man', 'mystery', 'creation', 'adam'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.MYSTERY OF WOMAN",
    ctype: "THOUGHT",
    en_title: "Mystery Of Woman",
    en_content: "Adam did not see Eve being created; therefore Woman will always be a Mystery to Man.",
    es_title: "El Misterio de la Mujer",
    es_content: "Adán no vio a Eva ser creada; por lo tanto, la Mujer siempre será un Misterio para el Hombre.",
    fr_title: "Le Mystère de la Femme",
    fr_content: "Adam n'a pas vu Ève être créée ; par conséquent, la Femme sera toujours un Mystère pour l'Homme.",
    hi_title: "स्त्री का रहस्य",
    hi_content: "आदम ने हव्वा को बनाए जाते नहीं देखा; इसलिए स्त्री हमेशा पुरुष के लिए एक रहस्य रहेगी।",
    zh_title: "Nǚrén de àomì  nǚ rén de ào mì",
    zh_content: "Yàdāng méiyǒu kànjiàn Xiàwá de chuàngzào; yīncǐ nǚrén jiāng yǒngyuǎn shì nánrén de àomì.  yà dāng méi yǒu kàn jiàn xià wá de chuàng zào ； yīn cǐ nǚ rén jiāng yǒng yuǎn shì nán rén de ào mì 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MYSTERY OF WOMAN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->MYSTERY OF WOMAN"
RETURN t, parent;
```
