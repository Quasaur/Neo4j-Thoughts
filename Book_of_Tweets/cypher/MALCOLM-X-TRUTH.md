---
name: "thought.MALCOLM X TRUTH"
alias: "Thought: Malcolm X Truth"
type: THOUGHT
en_content: "Malcolm X loved his people enough to tell them the Truth about themselves."
parent: "topic.HUMANITY"
tags:
- truth
- leadership
- love
- humanity
- justice
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-May-2011)
CREATE (t:THOUGHT {
    name: "thought.MALCOLM X TRUTH",
    alias: "Thought: Malcolm X Truth",
    parent: "topic.HUMANITY",
    tags: ['truth', 'leadership', 'love', 'humanity', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MALCOLM X TRUTH",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MALCOLM X TRUTH" AND c.name = "content.MALCOLM X TRUTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MALCOLM X TRUTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.MALCOLM X TRUTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >MALCOLM X TRUTH" }]->(child);
```
