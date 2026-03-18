---
type: THOUGHT
name: "thought.KNOWING JESUS NAME"
alias: "Thought: Knowing Jesus Name"
parent: "topic.THE GODHEAD"
en_content: "Matthew 7:22, 23 -- Using Jesus' Name doesn't mean you know Jesus."
tags: ["jesus", "identity", "knowledge", "lord", "relationship"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Nov-2011a)
CREATE (t:THOUGHT {    name: "thought.KNOWING JESUS NAME",
    alias: "Thought: Knowing Jesus Name",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'identity', 'knowledge', 'lord', 'relationship'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.KNOWING JESUS NAME",
    ctype: "THOUGHT",
    en_title: "Knowing Jesus Name",
    en_content: "Matthew 7:22, 23 -- Using Jesus' Name doesn't mean you know Jesus.",
    es_title: "Conocer el Nombre de Jesús",
    es_content: "Mateo 7:22, 23 -- Usar el Nombre de Jesús no significa que conozcas a Jesús.",
    fr_title: "Connaître le Nom de Jésus",
    fr_content: "Matthieu 7:22, 23 -- Utiliser le Nom de Jésus ne signifie pas que vous connaissez Jésus.",
    hi_title: "यीशु का नाम जानना",
    hi_content: "मत्ती 7:22, 23 -- यीशु का नाम लेने का मतलब यह नहीं है कि आप यीशु को जानते हैं।",
    zh_title: "Rènshí Yēsū de míng  rèn shí yē sū de míng",
    zh_content: "Mǎdù fùyīn 7:22, 23 -- Shǐyòng Yēsū de míng bù dàibiǎo nǐ rènshi Yēsū.  mǎ tài fú yīn  7:22, 23 -- shǐ yòng yē sū de míng bù dài biǎo nǐ rèn shí yē sū 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.KNOWING JESUS NAME"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->KNOWING JESUS NAME"
RETURN t, parent;
```
