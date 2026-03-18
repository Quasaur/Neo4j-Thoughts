---
type: THOUGHT
name: "thought.GROWTH THROUGH WORD"
alias: "Thought: Growth Through Word"
parent: "topic.SPIRITUALITY"
en_content: "I cannot grow as a Christian without consistently hearing and speaking God's Word."
tags: ["growth", "word", "christianity", "spirituality", "hearing"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Apr-2012c)
CREATE (t:THOUGHT {    name: "thought.GROWTH THROUGH WORD",
    alias: "Thought: Growth Through Word",
    parent: "topic.SPIRITUALITY",
    tags: ['growth', 'word', 'christianity', 'spirituality', 'hearing'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.GROWTH THROUGH WORD",
    ctype: "THOUGHT",
    en_title: "Growth Through Word",
    en_content: "I cannot grow as a Christian without consistently hearing and speaking God's Word.",
    es_title: "Crecimiento a Través de la Palabra",
    es_content: "No puedo crecer como cristiano sin escuchar y hablar consistentemente la Palabra de Dios.",
    fr_title: "Croissance par la Parole",
    fr_content: "Je ne peux pas grandir en tant que chrétien sans entendre et proclamer constamment la Parole de Dieu.",
    hi_title: "वचन के द्वारा विकास",
    hi_content: "मैं परमेश्वर के वचन को लगातार सुने और बोले बिना एक मसीही के रूप में बढ़ नहीं सकता।",
    zh_title: "Tōngguò Shèngdào Chéngzhǎng",
    zh_content: "Rúguǒ bù chíxù tīng hé shuō Shàngdì de huà, wǒ jiù wúfǎ zuòwéi Jīdūtú ér chéngzhǎng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GROWTH THROUGH WORD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->GROWTH THROUGH WORD"
RETURN t, parent;
```
