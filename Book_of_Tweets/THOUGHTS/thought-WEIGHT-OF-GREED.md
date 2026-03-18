---
type: THOUGHT
name: "thought.WEIGHT OF GREED"
alias: "Thought: Weight Of Greed"
parent: "topic.MORALITY"
en_content: "America is finally buckling under the weight of its own greed."
tags: ["greed", "society", "america", "economics", "judgment"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2011b)
CREATE (t:THOUGHT {    name: "thought.WEIGHT OF GREED",
    alias: "Thought: Weight Of Greed",
    parent: "topic.MORALITY",
    tags: ['greed', 'society', 'america', 'economics', 'judgment'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.WEIGHT OF GREED",
    ctype: "THOUGHT",
    en_title: "Weight Of Greed",
    en_content: "America is finally buckling under the weight of its own greed.",
    es_title: "El Peso de la Codicia",
    es_content: "Estados Unidos finalmente se está derrumbando bajo el peso de su propia codicia.",
    fr_title: "Le Poids de la Cupidité",
    fr_content: "L'Amérique finit par succomber sous le poids de sa propre cupidité.",
    hi_title: "लालच का भार",
    hi_content: "अमेरिका आखिरकार अपने ही लालच के भार तले झुक रहा है।",
    zh_title: "Tānlán de fùdān  tān lán de fù dān",
    zh_content: "Měiguó zhōngyú zài zìjǐ tānlán de fùdān xià bēngkuì.  měi guó zhōng yú zài zì jǐ tān lán de fù dān xià bēng kuì 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WEIGHT OF GREED"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->WEIGHT OF GREED"
RETURN t, parent;
```
