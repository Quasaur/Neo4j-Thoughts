---
name: "thought.PREFERENCE VS NECESSITY"
alias: "Thought: Preference Vs Necessity"
type: THOUGHT
en_content: "Preference must give way to Necessity."
parent: "topic.WISDOM"
tags:
- wisdom
- choice
- necessity
- priority
- truth
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jul-2011b)
CREATE (t:THOUGHT {
    name: "thought.PREFERENCE VS NECESSITY",
    alias: "Thought: Preference Vs Necessity",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'choice', 'necessity', 'priority', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PREFERENCE VS NECESSITY",
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

MATCH (t:THOUGHT {name: "thought.PREFERENCE VS NECESSITY"})
MATCH (c:CONTENT {name: "content.PREFERENCE VS NECESSITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PREFERENCE VS NECESSITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.WISDOM"})
MATCH (child:THOUGHT {name: "thought.PREFERENCE VS NECESSITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >PREFERENCE VS NECESSITY" }]->(child);
```
