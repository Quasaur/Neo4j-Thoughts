---
type: THOUGHT
name: "thought.OUR MASTER"
alias: "Thought: Our Master"
parent: "topic.TRUTH"
en_content: "Truth belongs to no one; It is It's own Master...and ours."
tags: ["truth", "master", "seovereign", "veritas", "ultimate"]
ptopic: "[[topic-TRUTH]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.OUR MASTER",
    alias: "Thought: Our Master",
    parent: "topic.TRUTH",
    tags: ["truth", "master", "seovereign", "veritas", "ultimate"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.OUR MASTER",
    ctype: "THOUGHT",
    en_title: "Our Master",
    en_content: "Truth belongs to no one; It is It's own Master...and ours.",
    es_title: "NUESTRO MAESTRO",
    es_content: "La verdad no pertenece a nadie; Es su propio Maestro... y el nuestro.",
    fr_title: "NOTRE MAÎTRE",
    fr_content: "La vérité n’appartient à personne ; C'est son propre Maître... et le nôtre.",
    hi_title: "हमारे स्वामी",
    hi_content: "सत्य किसी का नहीं होता; यह अपना स्वामी है...और हमारा है।",
    zh_title: "wǒ men de dà shī",
    zh_content: "zhēn lǐ bù shǔ yú rèn hé rén ； tā shì tā zì jǐ de zhǔ rén …… yě shì wǒ men de zhǔ rén 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.OUR MASTER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.TRUTH->OUR MASTER"
RETURN t, parent;
```
