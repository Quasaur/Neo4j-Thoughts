---
type: THOUGHT
name: "thought.HUMANITARIANISM"
alias: "Thought: Humanitarianism"
parent: "topic.RELIGION"
tags: ["humanity", "self_worship", "god", "judgment", "accountable"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HUMANITARIANISM",
    alias: "Thought: Humanitarianism",
    parent: "topic.RELIGION",
    tags: ["humanity", "self_worship", "god", "judgment", "accountable"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HUMANITARIANISM",
    ctype: "THOUGHT",
    en_title: "Humanitarianism",
    en_content: "",
    es_title: "HUMANITARISMO",
    es_content: "Sin responsabilidad, el hombre puede llamarse Dios (humanitarismo, hermana gemela de la evolución).",
    fr_title: "HUMANITARISME",
    fr_content: "Sans responsabilité, l'homme peut s'appeler Dieu (l'humanitarisme, la sœur jumelle de l'évolution).",
    hi_title: "मानवतावाद",
    hi_content: "जवाबदेही के बिना, मनुष्य स्वयं को भगवान (मानवतावाद, विकासवाद की जुड़वां बहन) कह सकता है।",
    zh_title: "rén dào zhǔ yì",
    zh_content: "méi yǒu zé rèn ， rén kě yǐ chēng zì jǐ wèi shàng dì （ rén dào zhǔ yì ， jìn huà lùn de luán shēng jiě mèi ）。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HUMANITARIANISM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->HUMANITARIANISM"
RETURN t, parent;
```
