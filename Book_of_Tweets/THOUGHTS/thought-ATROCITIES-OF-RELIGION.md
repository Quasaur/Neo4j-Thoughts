---
type: THOUGHT
name: "thought.ATROCITIES OF RELIGION"
alias: "Thought: Atrocities Of Religion"
parent: "topic.RELIGION"
en_content: "It's amazing what atrocities religion will allow."
tags: ["religion", "atrocity", "character", "failure", "judgment"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Mar-2012b)
CREATE (t:THOUGHT {    name: "thought.ATROCITIES OF RELIGION",
    alias: "Thought: Atrocities Of Religion",
    parent: "topic.RELIGION",
    tags: ['religion', 'atrocity', 'character', 'failure', 'judgment'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.ATROCITIES OF RELIGION",
    ctype: "THOUGHT",
    en_title: "Atrocities Of Religion",
    en_content: "It's amazing what atrocities religion will allow.",
    es_title: "Atrocidades de la Religión",
    es_content: "Es asombroso las atrocidades que la religión permitirá.",
    fr_title: "Atrocités de la Religion",
    fr_content: "C'est étonnant les atrocités que la religion permettra.",
    hi_title: "धर्म के अत्याचार",
    hi_content: "यह आश्चर्यजनक है कि धर्म किन अत्याचारों की अनुमति देगा।",
    zh_title: "Zōngjiào de bàoxíng",
    zh_content: "Lìngrén jīngyà de shì zōngjiào huì yǔnxǔ shénme yàng de bàoxíng."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ATROCITIES OF RELIGION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->ATROCITIES OF RELIGION"
RETURN t, parent;
```
