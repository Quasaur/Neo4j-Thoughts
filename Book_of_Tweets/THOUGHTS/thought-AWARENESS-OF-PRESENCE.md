---
type: THOUGHT
name: "thought.AWARENESS OF PRESENCE"
alias: "Thought: Awareness Of Presence"
parent: "topic.THE GODHEAD"
en_content: "Many believe they are aware of God's Wrath but few are aware of God's Loving Presence."
tags: ["presence", "wrath", "awareness", "god", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013b)
CREATE (t:THOUGHT {    name: "thought.AWARENESS OF PRESENCE",
    alias: "Thought: Awareness Of Presence",
    parent: "topic.THE GODHEAD",
    tags: ['presence', 'wrath', 'awareness', 'god', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.AWARENESS OF PRESENCE",
    ctype: "THOUGHT",
    en_title: "Awareness Of Presence",
    en_content: "Many believe they are aware of God's Wrath but few are aware of God's Loving Presence.",
    es_title: "Conciencia de la Presencia",
    es_content: "Muchos creen que son conscientes de la Ira de Dios, pero pocos son conscientes de la Presencia Amorosa de Dios.",
    fr_title: "Conscience de la Présence",
    fr_content: "Beaucoup croient être conscients de la Colère de Dieu, mais peu sont conscients de la Présence Aimante de Dieu.",
    hi_title: "उपस्थिति की जागरूकता",
    hi_content: "बहुत से लोग मानते हैं कि वे परमेश्वर के क्रोध के बारे में जानते हैं, लेकिन कुछ ही लोग परमेश्वर की प्रेमपूर्ण उपस्थिति के बारे में जानते हैं।",
    zh_title: "Duì cúnzài de yìshí  duì cún zài de yì shí",
    zh_content: "Xǔduō rén xiāngxìn tāmen yìshí dào Shàngdì de fènnù, dàn hěn shǎo rén yìshí dào Shàngdì chōngmǎn ài de cúnzài.  xǔ duō rén xiāng xìn tā men yì shí dào shàng dì de fèn nù ， dàn hěn shǎo rén yì shí dào shàng dì chōng mǎn ài de cún zài 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.AWARENESS OF PRESENCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->AWARENESS OF PRESENCE"
RETURN t, parent;
```
