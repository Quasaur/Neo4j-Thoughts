---
type: THOUGHT
name: "thought.ACCOUNTABILITY"
alias: "Thought: Accountability"
parent: "topic.MORALITY"
en_content: "God doesn't spare you the consequences of my actions."
tags: ["accountability", "consequences", "morality", "responsibility", "justice"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jul-2011c)
CREATE (t:THOUGHT {    name: "thought.ACCOUNTABILITY",
    alias: "Thought: Accountability",
    parent: "topic.MORALITY",
    tags: ['accountability', 'consequences', 'morality', 'responsibility', 'justice'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.ACCOUNTABILITY",
    ctype: "THOUGHT",
    en_title: "Accountability",
    en_content: "God doesn't spare you the consequences of my actions.",
    es_title: "Responsabilidad",
    es_content: "Dios no te libra de las consecuencias de mis acciones.",
    fr_title: "Responsabilité",
    fr_content: "Dieu ne t'épargne pas les conséquences de mes actions.",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "भगवान आपको मेरे कार्यों के परिणामों से नहीं बचाते।",
    zh_title: "Wènzé zhì",
    zh_content: "Shàngdì bù huì ràng nǐ miǎnshòu wǒ xíngwéi de hòuguǒ."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ACCOUNTABILITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->ACCOUNTABILITY"
RETURN t, parent;
```
