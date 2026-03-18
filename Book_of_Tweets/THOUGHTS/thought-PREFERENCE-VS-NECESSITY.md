---
type: THOUGHT
name: "thought.PREFERENCE VS NECESSITY"
alias: "Thought: Preference Vs Necessity"
parent: "topic.WISDOM"
en_content: "Preference must give way to Necessity."
tags: ["wisdom", "choice", "necessity", "priority", "truth"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jul-2011b)
CREATE (t:THOUGHT {    name: "thought.PREFERENCE VS NECESSITY",
    alias: "Thought: Preference Vs Necessity",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'choice', 'necessity', 'priority', 'truth'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.PREFERENCE VS NECESSITY",
    ctype: "THOUGHT",
    en_title: "Preference Vs Necessity",
    en_content: "Preference must give way to Necessity.",
    es_title: "Preferencia Vs Necesidad",
    es_content: "La preferencia debe ceder ante la necesidad.",
    fr_title: "Préférence Vs Nécessité",
    fr_content: "La préférence doit céder le pas à la nécessité.",
    hi_title: "प्राथमिकता बनाम आवश्यकता",
    hi_content: "प्राथमिकता को आवश्यकता के आगे झुकना चाहिए।",
    zh_title: "Xi Hao Yu Bi Xu",
    zh_content: "Xi hao bi xu rang wei yu bi xu."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PREFERENCE VS NECESSITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->PREFERENCE VS NECESSITY"
RETURN t, parent;
```
