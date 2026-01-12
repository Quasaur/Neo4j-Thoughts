---
name: "thought.ATROCITIES OF RELIGION"
alias: "Thought: Atrocities Of Religion"
type: THOUGHT
en_content: "It's amazing what atrocities religion will allow."
parent: "topic.RELIGION"
tags:
- religion
- atrocity
- character
- failure
- judgment
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Mar-2012b)
CREATE (t:THOUGHT {
    name: "thought.ATROCITIES OF RELIGION",
    alias: "Thought: Atrocities Of Religion",
    parent: "topic.RELIGION",
    tags: ['religion', 'atrocity', 'character', 'failure', 'judgment'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ATROCITIES OF RELIGION",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ATROCITIES OF RELIGION" AND c.name = "content.ATROCITIES OF RELIGION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ATROCITIES OF RELIGION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.ATROCITIES OF RELIGION"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >ATROCITIES OF RELIGION" }]->(child);
```
