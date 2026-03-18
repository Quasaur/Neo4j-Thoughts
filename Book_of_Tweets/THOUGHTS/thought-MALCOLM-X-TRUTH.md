---
type: THOUGHT
name: "thought.MALCOLM X TRUTH"
alias: "Thought: Malcolm X Truth"
parent: "topic.HUMANITY"
en_content: "Malcolm X loved his people enough to tell them the Truth about themselves."
tags: ["truth", "leadership", "love", "humanity", "justice"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-May-2011)
CREATE (t:THOUGHT {    name: "thought.MALCOLM X TRUTH",
    alias: "Thought: Malcolm X Truth",
    parent: "topic.HUMANITY",
    tags: ['truth', 'leadership', 'love', 'humanity', 'justice'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.MALCOLM X TRUTH",
    ctype: "THOUGHT",
    en_title: "Malcolm X Truth",
    en_content: "Malcolm X loved his people enough to tell them the Truth about themselves.",
    es_title: "La Verdad de Malcolm X",
    es_content: "Malcolm X amaba tanto a su gente que les dijo la Verdad acerca de sí mismos.",
    fr_title: "La Vérité de Malcolm X",
    fr_content: "Malcolm X aimait assez son peuple pour leur dire la Vérité sur eux-mêmes.",
    hi_title: "मैल्कम एक्स सत्य",
    hi_content: "मैल्कम एक्स अपने लोगों से इतना प्रेम करते थे कि उन्होंने उन्हें स्वयं के बारे में सत्य बताया।",
    zh_title: "Mǎi'ěrkēmǔ Ài Kèsī Zhēnlǐ",
    zh_content: "Mǎi'ěrkēmǔ Ài Kèsī ài tā de rénmín, zú yǐ gàosù tāmen guānyú zìjǐ de Zhēnlǐ."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MALCOLM X TRUTH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->MALCOLM X TRUTH"
RETURN t, parent;
```
